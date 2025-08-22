
# מגמות מתחסנים לקורונה בעולם (COVID‑19) — פרויקט דאטה ו‑BI

פרויקט קוד פתוח שמדגים **ETL ➜ עיבוד נתונים ➜ קבצי מדדים ➜ דאשבורדים** עבור מגמות התחסנות לקורונה בכלל המדינות והאגרגטים (World/Continents), על בסיס מאגר Kaggle:
- *COVID‑19 World Vaccination Progress* מאת **gpreda**. ראה מקור הנתונים והסבר מלא בעמוד הדאטה.  
- מומלץ לצרף קרדיט גם ל‑**Our World in Data** שהינו מקור הנתונים הראשוני שאותו Kaggle משכפל.

> ⚠️ הפרויקט מיועד להצגה מקצועית לתפקיד ראש צוות נתונים/BI: מבנה רפוזיטורי נקי, קוד ETL, בדיקות, אפליקציית Streamlit להצגה, והנחיות לבניית דאשבורד ב‑Power BI.
<img width="3679" height="1743" alt="image" src="https://github.com/user-attachments/assets/590a255b-4632-4586-90af-74edf11bfd35" />

## מבנה הפרויקט
```
.
├─ data/
│  ├─ raw/                # קבצי CSV שהורדת מקגל
│  └─ processed/          # קבצי עיבוד (csv/parquet) לשימוש BI
├─ src/
│  └─ covid_vax/
│     ├─ etl.py           # תהליך ETL מלא
│     └─ utils.py         # פונקציות עזר
├─ app/
│  └─ streamlit_app.py    # אפליקציית Streamlit להצגת מגמות
├─ dashboards/
│  └─ powerbi/README.md   # מתכון לדאשבורד Power BI
├─ sql/
│  └─ star_schema.sql     # דגם מחסן נתונים (כוכב)
├─ tests/
│  └─ test_etl.py
├─ .github/workflows/ci.yml
├─ requirements.txt
├─ .gitignore
└─ LICENSE
```

## הפעלה מהירה (Quickstart)
1. צריבת סביבת פייתון ותקנות תלויות:
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. הורדת הדאטה מקגל (אחת מהאפשרויות):
   - **דרך אתר Kaggle**: הורד את `country_vaccinations.csv` וגם `country_vaccinations_by_manufacturer.csv` ושמור ב‑`data/raw/`.
   - **דרך Kaggle CLI**:
     ```bash
     kaggle datasets download -d gpreda/covid-world-vaccination-progress -p data/raw
     unzip data/raw/covid-world-vaccination-progress.zip -d data/raw
     ```
3. הרצת ה‑ETL ליצירת קבצי המדדים:
   ```bash
   python -m src.covid_vax.etl --raw-dir data/raw --out-dir data/processed
   ```
4. הרצת האפליקציה להצגה:
   ```bash
   streamlit run app/streamlit_app.py
   ```

## מה מקבלים אחרי ה‑ETL
- `data/processed/country_daily_metrics.csv` — טבלה יומית לכל מדינה/אגרגט עם מדדים עיקריים.
- `data/processed/global_time_series.csv` — סדרת זמן של World (אם קיימת) או חישוב מצטבר חלופי.
- `data/processed/top_countries_latest.csv` — דירוג מדינות לפי שיעור התחסנות/קצב יומי בתאריך העדכני לכל מדינה.

## KPI-ים מומלצים לדאשבורד
- **People Vaccinated %** — לפחות מנת חיסון אחת.
- **Fully Vaccinated %** — סיום פרוטוקול ראשוני.
- **Daily Vaccinations / 1M** — קצב יומי.
- **Total Doses** — סך המנות שניתנו (כולל בוסטרים).
- פילוחים: יבשות/הכנסה (אם קיים), מדינות, סוגי חיסונים.

## הערות איכות וסניטציה
- קוד ה‑ETL מזהה שמות עמודות נפוצים מהסט של Kaggle (לדוגמה: `people_vaccinated_per_hundred`), ומטפל בחסרים וחריגים.
- אם קיימת ישות `World` בקובץ — נעשה בה שימוש ל‑global KPIs. אם לא, מופעל אגרגט חלופי זהיר (הסברים ב‑etl.py).

## רישוי
MIT — שימוש חופשי עם קרדיט מקורות הדאטה.
