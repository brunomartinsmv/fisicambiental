from __future__ import annotations

import pandas as pd


def add_month(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "date" in df.columns:
        df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    return df


def rolling_mean(df: pd.DataFrame, window: int = 7) -> pd.DataFrame:
    df = df.copy()
    if "date" in df.columns:
        df = df.sort_values("date")
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].rolling(window=window, min_periods=1).mean()
    return df


def monthly_sum(df: pd.DataFrame, value_cols: list[str]) -> pd.DataFrame:
    df = add_month(df)
    if "month" not in df.columns:
        raise ValueError("No 'month' column available for aggregation")

    agg = df.groupby("month")[value_cols].sum().reset_index()
    return agg
