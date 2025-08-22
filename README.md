# COVID-19 Global Vaccination Trends | מגמות חיסונים לקורונה בעולם

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Data Source](https://img.shields.io/badge/Data-Kaggle-orange.svg)

**A comprehensive data analysis project showcasing COVID-19 vaccination trends worldwide**  
**פרויקט ניתוח נתונים מקיף המציג מגמות חיסונים לקורונה ברחבי העולם**

[English](#english) | [עברית](#hebrew)

</div>

---

## English

### 🎯 Project Overview

This open-source project demonstrates a complete **ETL → Data Processing → Analytics → Dashboard** pipeline for COVID-19 vaccination trends across all countries and regions. Built with real-world data from Kaggle's *COVID-19 World Vaccination Progress* dataset by **gpreda**, originally sourced from **Our World in Data**.

> 💼 **Professional Portfolio Project**: Designed to showcase data engineering and BI skills with clean repository structure, production-ready ETL code, interactive visualizations, and comprehensive documentation.

### 🏗️ Project Architecture

```
covid19-vax-trends/
├── 📁 data/
│   ├── raw/              # Raw CSV files from Kaggle
│   └── processed/        # Cleaned data ready for BI tools
├── 📁 src/
│   └── covid_vax/
│       ├── etl.py        # Complete ETL pipeline
│       ├── utils.py      # Helper functions
│       └── __init__.py
├── 📁 app/
│   └── streamlit_app.py  # Interactive dashboard
├── 📁 .vscode/
│   ├── launch.json       # Debug configurations
│   └── settings.json     # IDE settings
├── 📄 requirements.txt   # Python dependencies
├── 📄 .gitignore        # Git ignore rules
└── 📄 README.md         # This file
```

### 🚀 Quick Start

#### Prerequisites
- Python 3.11+
- Kaggle account (for data download)

#### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/MaorKadosh/covid19-vax-trends-starter.git
cd covid19-vax-trends-starter

# Create virtual environment
python -m venv .venv

# Activate environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Data Acquisition

**Option A: Kaggle CLI (Recommended)**
```bash
# Configure Kaggle API (one-time setup)
# 1. Go to https://www.kaggle.com/settings/account
# 2. Create new API token
# 3. Place kaggle.json in ~/.kaggle/ directory

# Download dataset
kaggle datasets download -d gpreda/covid-world-vaccination-progress -p data/raw
```

**Option B: Manual Download**
1. Visit: https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress
2. Download the dataset
3. Extract files to `data/raw/` directory

#### 3. Run ETL Pipeline
```bash
python -m src.covid_vax.etl --raw-dir data/raw --out-dir data/processed
```

#### 4. Launch Dashboard
```bash
streamlit run app/streamlit_app.py
```

### 📊 Generated Outputs

The ETL pipeline produces three key datasets:

1. **`country_daily_metrics.csv`** - Daily vaccination metrics per country/region
2. **`global_time_series.csv`** - Global aggregated time series data
3. **`top_countries_latest.csv`** - Country rankings by vaccination rates

### 📈 Key Performance Indicators (KPIs)

- **People Vaccinated %** - Population with at least one dose
- **Fully Vaccinated %** - Population with complete initial protocol
- **Daily Vaccinations per Million** - Daily vaccination rate
- **Total Doses Administered** - Cumulative doses (including boosters)
- **Vaccination Progress by Region** - Continental and income-level breakdowns

### 🛠️ Technical Features

- **Robust ETL Pipeline**: Handles missing data, data quality validation, and flexible schema detection
- **Interactive Dashboard**: Built with Streamlit for real-time data exploration
- **Production Ready**: Includes logging, error handling, and configurable parameters
- **VS Code Integration**: Pre-configured debug settings and launch configurations
- **Data Quality Assurance**: Automated validation and cleansing processes

### 🔧 Development

#### Running Tests
```bash
python -m pytest tests/
```

#### Code Quality
```bash
# Format code
black src/ app/

# Lint code
flake8 src/ app/
```

### 📝 License

MIT License - Free to use with attribution to data sources.

---

## Hebrew

### 🎯 סקירת הפרויקט

פרויקט קוד פתוח המדגים צינור עבודה מלא של **ETL ← עיבוד נתונים ← אנליטיקה ← דאשבורד** עבור מגמות חיסונים לקורונה בכל המדינות והאזורים. בנוי עם נתונים אמיתיים ממאגר Kaggle *COVID-19 World Vaccination Progress* מאת **gpreda**, שמקורו ב-**Our World in Data**.

> 💼 **פרויקט תיק עבודות מקצועי**: מיועד להדגמת כישורי הנדסת נתונים ו-BI עם מבנה רפוזיטורי נקי, קוד ETL מוכן לייצור, הדמיות אינטראקטיביות ותיעוד מקיף.

### 🏗️ ארכיטקטורת הפרויקט

```
covid19-vax-trends/
├── 📁 data/
│   ├── raw/              # קבצי CSV גולמיים מקגל
│   └── processed/        # נתונים מנוקים מוכנים לכלי BI
├── 📁 src/
│   └── covid_vax/
│       ├── etl.py        # צינור ETL מלא
│       ├── utils.py      # פונקציות עזר
│       └── __init__.py
├── 📁 app/
│   └── streamlit_app.py  # דאשבורד אינטראקטיבי
├── 📁 .vscode/
│   ├── launch.json       # הגדרות דיבאג
│   └── settings.json     # הגדרות IDE
├── 📄 requirements.txt   # תלויות Python
├── 📄 .gitignore        # כללי התעלמות Git
└── 📄 README.md         # קובץ זה
```

### 🚀 התחלה מהירה

#### דרישות מוקדמות
- Python 3.11+
- חשבון Kaggle (להורדת נתונים)

#### 1. הגדרת סביבה
```bash
# שכפול הרפוזיטורי
git clone https://github.com/MaorKadosh/covid19-vax-trends-starter.git
cd covid19-vax-trends-starter

# יצירת סביבה וירטואלית
python -m venv .venv

# הפעלת הסביבה
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# התקנת תלויות
pip install -r requirements.txt
```

#### 2. השגת נתונים

**אפשרות א': Kaggle CLI (מומלץ)**
```bash
# הגדרת Kaggle API (חד פעמי)
# 1. עבור ל: https://www.kaggle.com/settings/account
# 2. צור API token חדש
# 3. שמור את kaggle.json בתיקייה ~/.kaggle/

# הורדת מאגר הנתונים
kaggle datasets download -d gpreda/covid-world-vaccination-progress -p data/raw
```

**אפשרות ב': הורדה ידנית**
1. בקר ב: https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress
2. הורד את מאגר הנתונים
3. חלץ את הקבצים לתיקייה `data/raw/`

#### 3. הרצת צינור ETL
```bash
python -m src.covid_vax.etl --raw-dir data/raw --out-dir data/processed
```

#### 4. הפעלת הדאשבורד
```bash
streamlit run app/streamlit_app.py
```

### 📊 פלטים שנוצרים

צינור ה-ETL מייצר שלושה מאגרי נתונים מרכזיים:

1. **`country_daily_metrics.csv`** - מדדי חיסון יומיים לכל מדינה/אזור
2. **`global_time_series.csv`** - נתוני סדרות זמן גלובליים מצטברים
3. **`top_countries_latest.csv`** - דירוג מדינות לפי שיעורי חיסון

### 📈 מדדי ביצוע מרכזיים (KPIs)

- **אחוז מחוסנים** - אוכלוסייה עם לפחות מנה אחת
- **אחוז מחוסנים במלואם** - אוכלוסייה עם פרוטוקול ראשוני מלא
- **חיסונים יומיים למיליון** - קצב חיסון יומי
- **סך מנות שניתנו** - מנות מצטברות (כולל חיזוקים)
- **התקדמות חיסון לפי אזור** - פילוח לפי יבשות ורמת הכנסה

### 🛠️ תכונות טכניות

- **צינור ETL חזק**: מטפל בנתונים חסרים, אימות איכות נתונים וזיהוי סכמה גמיש
- **דאשבורד אינטראקטיבי**: בנוי עם Streamlit לחקירת נתונים בזמן אמת
- **מוכן לייצור**: כולל לוגים, טיפול בשגיאות ופרמטרים הניתנים להגדרה
- **אינטגרציה עם VS Code**: הגדרות דיבאג והפעלה מוגדרות מראש
- **הבטחת איכות נתונים**: תהליכי אימות וניקוי אוטומטיים

### 🔧 פיתוח

#### הרצת בדיקות
```bash
python -m pytest tests/
```

#### איכות קוד
```bash
# עיצוב קוד
black src/ app/

# בדיקת קוד
flake8 src/ app/
```

### 📝 רישוי

רישיון MIT - שימוש חופשי עם ציון מקורות הנתונים.

---

<div align="center">

**Made with ❤️ for the data community**  
**נוצר באהבה עבור קהילת הנתונים**

</div>