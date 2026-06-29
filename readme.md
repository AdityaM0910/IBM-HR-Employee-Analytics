# 👨‍💼 IBM HR Employee Analytics

![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge\&logo=microsoftexcel\&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge\&logo=postgresql\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-4285F4?style=for-the-badge)

---

# 📌 Project Overview

This project analyzes employee data from the IBM HR Analytics dataset to understand workforce trends and employee attrition. The project combines Excel and PostgreSQL to clean data, build an interactive dashboard, and answer business questions using SQL.

The main goal is to help HR teams understand employee behavior and identify factors related to attrition, salary, experience, and job roles.

---

# 🎯 Objectives

* Clean and prepare HR data for analysis.
* Build an interactive Excel dashboard.
* Analyze employee attrition using SQL.
* Answer business questions with data.
* Find insights that can help HR teams make better decisions.

---

# 📊 Dataset Information

**Dataset:** IBM HR Analytics Employee Attrition & Performance

**Source:** Kaggle

* Records: **1,470**
* Original Columns: **35**

### New Features Created

The following columns were created during data preparation:

* Age Group
* Income Slab
* Experience Group
* Hike Slab
* Attrition Fixed (0 = No, 1 = Yes)

These features made it easier to perform calculations, build dashboard filters, and answer business questions.

---

# 🛠️ Tools Used

* Microsoft Excel
* PostgreSQL
* SQL

---

# 📂 Project Workflow

1. Data Understanding
2. Data Cleaning in Excel
3. Feature Engineering
4. Interactive Dashboard Development
5. SQL Business Analysis
6. Business Insights

---

# 📁 Repository Structure

```text
IBM-HR-Employee-Analytics/

│── data/
│   ├── raw/
│   └── cleaned/
│
│── excel/
│   ├── Data_Cleaning.xlsx
│   └── HR_Dashboard.xlsx
│
│── sql/
│   ├── 01_Database_Setup.sql
│   └── 02_Business_Analysis.sql
│
│── images/
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

---

# 📈 Dashboard KPIs

The dashboard includes the following key performance indicators:

* Total Employees
* Attrition Rate
* Employees Left
* Average Age
* Average Monthly Income
* Average Experience

Interactive slicers allow filtering by:

* Age Group
* Department
* Monthly Income Slab
* Experience Group
* Gender

---

# 📊 Dashboard Visualizations

The dashboard includes the following charts:

* Employee Count and Attrition by Department
* Attrition by Job Role
* Attrition by Age Group
* Attrition by Gender
* Average Age by Department
* Attrition by Education Background
* Attrition by Income Slab
* Department and Gender-wise Attrition

---

# ❓ Business Analysis

Using PostgreSQL, this project answers business questions related to:

* Employee distribution
* Department performance
* Job role analysis
* Salary analysis
* Employee experience
* Education background
* Attrition trends
* Ranking and comparisons
* Department-wise performance
* Employee demographics

The SQL analysis includes:

* GROUP BY
* HAVING
* CASE
* Common Table Expressions (CTEs)
* Window Functions
* ROW_NUMBER()
* RANK()
* DENSE_RANK()
* LAG()
* LEAD()
* NTILE()

A total of **38 business queries** were written to answer different HR-related questions.

---

# 💡 Key Insights

Some important findings from the analysis include:

* Employee attrition varies across departments and job roles.
* Monthly income shows a relationship with employee attrition.
* Younger and less experienced employees have different attrition patterns than senior employees.
* Education background and department influence workforce distribution.
* Average employee age is different across departments.
* Interactive filters make it easy to explore trends for different employee groups.

---

# 📷 Dashboard Preview

The repository includes:

* Interactive Excel Dashboard
* Dashboard screenshots
* SQL analysis
* Data cleaning workbook

---

# 🚀 Future Improvements

Possible improvements for this project include:

* Build the dashboard in Power BI.
* Add predictive models to estimate employee attrition.
* Create automated HR reports.
* Compare trends across multiple companies.
* Add employee performance analysis for deeper insights.

---

# 📬 Contact

If you have any suggestions or feedback, feel free to connect with me through GitHub.
