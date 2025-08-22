#!/usr/bin/env python3
"""
ETL Pipeline for COVID-19 Vaccination Data
מעבד נתוני חיסונים מקגל ליצירת מדדי BI
"""

import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Dict, Any
import logging

# הגדרת לוגים
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CovidVaxETL:
    """מחלקה לעיבוד נתוני חיסונים לקורונה"""
    
    def __init__(self, raw_dir: str, output_dir: str):
        self.raw_dir = Path(raw_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def load_raw_data(self) -> pd.DataFrame:
        """טעינת נתונים גולמיים מקגל"""
        csv_files = list(self.raw_dir.glob("*.csv"))
        
        if not csv_files:
            raise FileNotFoundError(f"לא נמצאו קבצי CSV בתיקייה {self.raw_dir}")
            
        # חיפוש קובץ החיסונים הראשי
        main_file = None
        for file in csv_files:
            if "country_vaccinations" in file.name and "manufacturer" not in file.name:
                main_file = file
                break
                
        if not main_file:
            main_file = csv_files[0]  # קח את הראשון אם לא מצאת
            
        logger.info(f"טוען נתונים מ: {main_file}")
        df = pd.read_csv(main_file)
        
        # המרת עמודת תאריך
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
            
        return df
        
    def clean_and_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """ניקוי והמרת נתונים"""
        logger.info("מנקה ומעבד נתונים...")
        
        # מילוי ערכים חסרים במדדים מספריים
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(0)
            
        # חישוב מדדים נוספים
        if 'people_vaccinated_per_hundred' in df.columns:
            df['vaccination_rate_pct'] = df['people_vaccinated_per_hundred']
        elif 'people_vaccinated' in df.columns and 'population' in df.columns:
            df['vaccination_rate_pct'] = (df['people_vaccinated'] / df['population']) * 100
            
        return df
        
    def create_country_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        """יצירת מדדים יומיים למדינות"""
        logger.info("יוצר מדדים יומיים למדינות...")
        
        # בחירת עמודות רלוונטיות
        key_cols = ['country', 'date']
        metric_cols = []
        
        # זיהוי עמודות מדדים קיימות
        possible_metrics = [
            'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
            'daily_vaccinations', 'total_vaccinations_per_hundred',
            'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred',
            'daily_vaccinations_per_million', 'vaccination_rate_pct'
        ]
        
        for col in possible_metrics:
            if col in df.columns:
                metric_cols.append(col)
                
        result_df = df[key_cols + metric_cols].copy()
        result_df = result_df.sort_values(['country', 'date'])
        
        return result_df
        
    def create_global_timeseries(self, df: pd.DataFrame) -> pd.DataFrame:
        """יצירת סדרת זמן גלובלית"""
        logger.info("יוצר סדרת זמן גלובלית...")
        
        # חיפוש נתוני World אם קיימים
        world_data = df[df['country'].str.upper() == 'WORLD'].copy()
        
        if not world_data.empty:
            return world_data.sort_values('date')
        else:
            # אגרגט חלופי - סכום כל המדינות
            logger.info("לא נמצאו נתוני World, מחשב אגרגט...")
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            
            global_agg = df.groupby('date')[numeric_cols].sum().reset_index()
            global_agg['country'] = 'World (Calculated)'
            
            return global_agg.sort_values('date')
            
    def create_top_countries(self, df: pd.DataFrame) -> pd.DataFrame:
        """יצירת דירוג מדינות לפי מדדים עדכניים"""
        logger.info("יוצר דירוג מדינות...")
        
        # קבלת הנתונים העדכניים ביותר לכל מדינה
        latest_data = df.loc[df.groupby('country')['date'].idxmax()].copy()
        
        # סינון מדינות (לא אגרגטים)
        exclude_entities = ['World', 'Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania']
        latest_data = latest_data[~latest_data['country'].isin(exclude_entities)]
        
        # מיון לפי שיעור חיסון
        if 'vaccination_rate_pct' in latest_data.columns:
            latest_data = latest_data.sort_values('vaccination_rate_pct', ascending=False)
        elif 'people_vaccinated_per_hundred' in latest_data.columns:
            latest_data = latest_data.sort_values('people_vaccinated_per_hundred', ascending=False)
            
        return latest_data.head(20)  # טופ 20
        
    def run_etl(self):
        """הרצת תהליך ETL מלא"""
        logger.info("מתחיל תהליך ETL...")
        
        # טעינת נתונים
        df = self.load_raw_data()
        logger.info(f"נטענו {len(df)} שורות נתונים")
        
        # עיבוד
        df_clean = self.clean_and_transform(df)
        
        # יצירת קבצי פלט
        country_metrics = self.create_country_metrics(df_clean)
        global_ts = self.create_global_timeseries(df_clean)
        top_countries = self.create_top_countries(df_clean)
        
        # שמירה
        country_metrics.to_csv(self.output_dir / "country_daily_metrics.csv", index=False)
        global_ts.to_csv(self.output_dir / "global_time_series.csv", index=False)
        top_countries.to_csv(self.output_dir / "top_countries_latest.csv", index=False)
        
        logger.info(f"ETL הושלם בהצלחה! קבצים נשמרו ב: {self.output_dir}")
        
def main():
    parser = argparse.ArgumentParser(description="COVID-19 Vaccination Data ETL")
    parser.add_argument("--raw-dir", default="data/raw", help="תיקיית נתונים גולמיים")
    parser.add_argument("--out-dir", default="data/processed", help="תיקיית פלט")
    
    args = parser.parse_args()
    
    etl = CovidVaxETL(args.raw_dir, args.out_dir)
    etl.run_etl()

if __name__ == "__main__":
    main()