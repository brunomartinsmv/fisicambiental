from __future__ import annotations

import numpy as np
import pandas as pd


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def mbe(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(y_pred - y_true))


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) < 2:
        return float("nan")
    if np.std(y_true, ddof=1) == 0 or np.std(y_pred, ddof=1) == 0:
        return float("nan")
    corr = np.corrcoef(y_true, y_pred)[0, 1]
    if not np.isfinite(corr):
        return float("nan")
    return float(corr ** 2)


def willmott_d(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_mean = np.mean(y_true)
    denom = np.sum((np.abs(y_pred - y_mean) + np.abs(y_true - y_mean)) ** 2)
    if denom == 0:
        return float("nan")
    return float(1 - np.sum((y_pred - y_true) ** 2) / denom)


def compute_metrics(df: pd.DataFrame, ref_col: str, method_cols: list[str]) -> pd.DataFrame:
    rows = []

    for col in method_cols:
        ref = df[ref_col].to_numpy()
        series = df[col].to_numpy()
        mask = np.isfinite(ref) & np.isfinite(series)
        ref = ref[mask]
        series = series[mask]
        rows.append(
            {
                "method": col,
                "rmse": rmse(ref, series),
                "mae": mae(ref, series),
                "mbe": mbe(ref, series),
                "r2": r2_score(ref, series),
                "willmott_d": willmott_d(ref, series),
            }
        )

    return pd.DataFrame(rows)
