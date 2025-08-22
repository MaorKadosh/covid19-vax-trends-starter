"""
פונקציות עזר לעיבוד נתוני חיסונים
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any

def validate_data_quality(df: pd.DataFrame) -> Dict[str, Any]:
    """בדיקת איכות נתונים"""
    report = {
        'total_rows': len(df),
        'missing_values': df.isnull().sum().to_dict(),
        'date_range': {
            'min_date': df['date'].min() if 'date' in df.columns else None,
            'max_date': df['date'].max() if 'date' in df.columns else None
        },
        'unique_countries': df['country'].nunique() if 'country' in df.columns else 0
    }
    return report

def format_numbers(value: float, format_type: str = 'default') -> str:
    """עיצוב מספרים להצגה"""
    if pd.isna(value):
        return "N/A"
        
    if format_type == 'percentage':
        return f"{value:.1f}%"
    elif format_type == 'thousands':
        return f"{value:,.0f}"
    elif format_type == 'millions':
        return f"{value/1_000_000:.1f}M"
    else:
        return f"{value:,.0f}"