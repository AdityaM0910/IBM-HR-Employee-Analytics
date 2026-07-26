"""
IBM HR Attrition — Logistic Regression
----------------------------------------
Goal: Predict attrition (Yes/No) using a small, defensible set of features,
      and interpret the coefficients in plain business language.

We deliberately keep the feature set small (5-6 features) instead of dumping
in everything. A model you can explain in an interview beats a model with
higher accuracy that you can't defend.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, classification_report
)
from sklearn.preprocessing import StandardScaler

pd.set_option("display.width", 120)

# ---------------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------------
df = pd.read_csv("D:\\project\\IBM-HR-Employee-Analytics\\python\\HR_employee_ibm_dataset.csv")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Target already exists as Attrition_fixed (1 = left, 0 = stayed)
target = "Attrition_fixed"
print("\nClass balance:")
print(df[target].value_counts(normalize=True).round(3))
# -> This will show attrition is imbalanced (~16% Yes). Important to note
#    in the interview: accuracy alone is a misleading metric here.

# ---------------------------------------------------------------
# 2. FEATURE SELECTION (small, explainable, business-relevant)
# ---------------------------------------------------------------
# Numeric features
num_features = ["MonthlyIncome", "TotalWorkingYears", "DistanceFromHome"]

# Categorical features to encode
cat_features = ["OverTime", "JobSatisfaction", "MaritalStatus"]

use_cols = num_features + cat_features
model_df = df[use_cols + [target]].copy()

# JobSatisfaction is ordinal 1-4, keep as numeric
model_df["JobSatisfaction"] = model_df["JobSatisfaction"].astype(int)

# One-hot encode OverTime and MaritalStatus (drop_first avoids dummy trap)
model_df = pd.get_dummies(
    model_df, columns=["OverTime", "MaritalStatus"], drop_first=True
)

print("\nFinal feature set:")
print([c for c in model_df.columns if c != target])

# ---------------------------------------------------------------
# 3. TRAIN/TEST SPLIT
# ---------------------------------------------------------------
X = model_df.drop(columns=[target])
y = model_df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Scale numeric features (helps coefficient comparison + convergence)
scaler = StandardScaler()
num_cols_present = [c for c in num_features if c in X_train.columns]
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()
X_train_scaled[num_cols_present] = scaler.fit_transform(X_train[num_cols_present])
X_test_scaled[num_cols_present] = scaler.transform(X_test[num_cols_present])

# ---------------------------------------------------------------
# 4. FIT MODEL WITH STATSMODELS (for clean p-values / coefficients)
# ---------------------------------------------------------------
X_train_sm = sm.add_constant(X_train_scaled.astype(float))
logit_model = sm.Logit(y_train, X_train_sm)
result = logit_model.fit(disp=False)
print("\n" + "=" * 70)
print("STATSMODELS SUMMARY (coefficients + significance)")
print("=" * 70)
print(result.summary())

# Odds ratios — easier to explain to a business stakeholder than log-odds
odds_ratios = np.exp(result.params)
conf = np.exp(result.conf_int())
conf.columns = ["OR_2.5%", "OR_97.5%"]
odds_table = pd.concat([odds_ratios.rename("Odds_Ratio"), conf], axis=1)
print("\nODDS RATIOS (>1 = increases attrition odds, <1 = decreases):")
print(odds_table.round(3))

# ---------------------------------------------------------------
# 5. FIT MODEL WITH SKLEARN (for standard classification metrics)
# ---------------------------------------------------------------
clf = LogisticRegression(max_iter=1000, class_weight="balanced")
clf.fit(X_train_scaled, y_train)
y_pred = clf.predict(X_test_scaled)
y_proba = clf.predict_proba(X_test_scaled)[:, 1]

print("\n" + "=" * 70)
print("CLASSIFICATION METRICS (test set, class_weight='balanced')")
print("=" * 70)
print(f"Accuracy : {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall   : {recall_score(y_test, y_pred):.3f}")
print(f"F1       : {f1_score(y_test, y_pred):.3f}")
print(f"ROC AUC  : {roc_auc_score(y_test, y_proba):.3f}")
print("\nConfusion matrix [[TN, FP],[FN, TP]]:")
print(confusion_matrix(y_test, y_pred))
print("\n", classification_report(y_test, y_pred, target_names=["Stayed", "Left"]))

# ---------------------------------------------------------------
# 6. SAVE MODEL VISUALIZATIONS
# ---------------------------------------------------------------

import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import RocCurveDisplay

# Create images folder
os.makedirs("images", exist_ok=True)

# -----------------------------
# 1. Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Stayed", "Left"],
    yticklabels=["Stayed", "Left"]
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("images/confusion_matrix.png", dpi=300)
plt.close()

# -----------------------------
# 2. ROC Curve
# -----------------------------
plt.figure(figsize=(6,5))
RocCurveDisplay.from_predictions(y_test, y_proba)
plt.title(f"ROC Curve (AUC = {roc_auc_score(y_test, y_proba):.3f})")
plt.tight_layout()
plt.savefig("images/roc_curve.png", dpi=300)
plt.close()

# -----------------------------
# 3. Feature Importance
# -----------------------------
feature_names = X_train_scaled.columns
coefficients = clf.coef_[0]

coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

coef_df = coef_df.reindex(
    coef_df.Coefficient.abs().sort_values(ascending=True).index
)

plt.figure(figsize=(8,5))
plt.barh(coef_df["Feature"], coef_df["Coefficient"])
plt.xlabel("Coefficient")
plt.title("Feature Importance (Logistic Regression)")
plt.tight_layout()
plt.savefig("images/feature_importance.png", dpi=300)
plt.close()

# -----------------------------
# 4. Model Performance
# -----------------------------
metrics = {
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score", "ROC AUC"],
    "Score": [
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred),
        roc_auc_score(y_test, y_proba)
    ]
}

metrics_df = pd.DataFrame(metrics)

fig, ax = plt.subplots(figsize=(5,2.2))
ax.axis("off")

table = ax.table(
    cellText=[[m, f"{s:.3f}"] for m, s in zip(metrics_df["Metric"], metrics_df["Score"])],
    colLabels=["Metric", "Score"],
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.5)

plt.savefig("images/model_metrics.png", dpi=300, bbox_inches="tight")
plt.close()

