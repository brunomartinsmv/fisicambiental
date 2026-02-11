from __future__ import annotations

import pandas as pd


def clean_daily(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "date" in df.columns:
        df = df.sort_values("date")

    # Interpolate numeric columns
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].interpolate(method="linear", limit_direction="both")

    # Drop duplicated dates if any
    if "date" in df.columns:
        df = df.drop_duplicates(subset=["date"], keep="first")

    return df
