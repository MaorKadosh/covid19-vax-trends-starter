#!/usr/bin/env python3
"""
אפליקציית Streamlit להצגת מגמות חיסונים לקורונה
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import sys

# הוספת נתיב לחבילה
sys.path.append(str(Path(__file__).parent.parent))
from src.covid_vax.utils import format_numbers

st.set_page_config(
    page_title="מגמות חיסונים COVID-19",
    page_icon="💉",
    layout="wide"
)

@st.cache_data
def load_data():
    """טעינת נתונים מעובדים"""
    data_dir = Path("data/processed")
    
    try:
        country_metrics = pd.read_csv(data_dir / "country_daily_metrics.csv")
        global_ts = pd.read_csv(data_dir / "global_time_series.csv")
        top_countries = pd.read_csv(data_dir / "top_countries_latest.csv")
        
        # המרת תאריכים
        country_metrics['date'] = pd.to_datetime(country_metrics['date'])
        global_ts['date'] = pd.to_datetime(global_ts['date'])
        
        return country_metrics, global_ts, top_countries
    except FileNotFoundError:
        st.error("קבצי נתונים לא נמצאו! הרץ תחילה: python -m src.covid_vax.etl")
        return None, None, None

def main():
    st.title("📊 מגמות חיסונים COVID-19 בעולם")
    st.markdown("---")
    
    # טעינת נתונים
    country_data, global_data, top_countries = load_data()
    
    if country_data is None:
        st.stop()
    
    # סייד בר לבחירות
    st.sidebar.header("🎛️ הגדרות")
    
    # בחירת מדינות
    countries = sorted(country_data['country'].unique())
    selected_countries = st.sidebar.multiselect(
        "בחר מדינות:",
        countries,
        default=['Israel', 'United States', 'United Kingdom'] if any(c in countries for c in ['Israel', 'United States', 'United Kingdom']) else countries[:3]
    )
    
    # מדדים זמינים
    metric_cols = [col for col in country_data.columns if col not in ['country', 'date']]
    selected_metric = st.sidebar.selectbox(
        "בחר מדד:",
        metric_cols,
        index=0 if metric_cols else None
    )
    
    # עמודות ראשיות
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 מגמות לפי מדינות")
        
        if selected_countries and selected_metric:
            # סינון נתונים
            filtered_data = country_data[
                country_data['country'].isin(selected_countries)
            ]
            
            # גרף קווים
            fig = px.line(
                filtered_data,
                x='date',
                y=selected_metric,
                color='country',
                title=f"מגמת {selected_metric} לפי מדינות",
                labels={'date': 'תאריך', selected_metric: selected_metric}
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("בחר מדינות ומדד להצגת הגרף")
    
    with col2:
        st.subheader("🏆 מדינות מובילות")
        
        if not top_countries.empty:
            # הצגת טופ 10
            display_cols = ['country']
            if 'vaccination_rate_pct' in top_countries.columns:
                display_cols.append('vaccination_rate_pct')
            elif 'people_vaccinated_per_hundred' in top_countries.columns:
                display_cols.append('people_vaccinated_per_hundred')
                
            top_10 = top_countries[display_cols].head(10)
            st.dataframe(top_10, use_container_width=True)
    
    # מגמה גלובלית
    if not global_data.empty:
        st.subheader("🌍 מגמה גלובלית")
        
        # בחירת מדד גלובלי
        global_metrics = [col for col in global_data.columns if col not in ['country', 'date']]
        if global_metrics:
            selected_global_metric = st.selectbox(
                "מדד גלובלי:",
                global_metrics,
                key="global_metric"
            )
            
            fig_global = px.line(
                global_data,
                x='date',
                y=selected_global_metric,
                title=f"מגמה גלובלית - {selected_global_metric}",
                labels={'date': 'תאריך', selected_global_metric: selected_global_metric}
            )
            fig_global.update_layout(height=300)
            st.plotly_chart(fig_global, use_container_width=True)
    
    # סטטיסטיקות
    st.markdown("---")
    st.subheader("📊 סטטיסטיקות כלליות")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("מדינות במערך", len(countries))
    
    with col2:
        date_range = country_data['date'].max() - country_data['date'].min()
        st.metric("טווח תאריכים", f"{date_range.days} ימים")
    
    with col3:
        total_records = len(country_data)
        st.metric("סך רשומות", f"{total_records:,}")
    
    with col4:
        latest_date = country_data['date'].max().strftime('%Y-%m-%d')
        st.metric("עדכון אחרון", latest_date)

if __name__ == "__main__":
    main()