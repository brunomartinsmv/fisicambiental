# Reprodutibilidade / Reproducibility

**PT**
Este documento descreve o ambiente, dependencias e passos minimos para reproduzir o estudo.

**EN**
This document describes the environment, dependencies, and minimum steps to reproduce the study.

## Ambiente / Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Se o Matplotlib nao conseguir escrever cache, defina:
```bash
export MPLCONFIGDIR=/tmp/mpl-cache
```

## Pipeline
```bash
python -m scripts.cli all --year 2024
```

## Saidas esperadas
- `data/cleaned/*_daily.csv`
- `outputs/results/*_rolling_7d.csv`
- `outputs/results/*_monthly_totals.csv`
- `outputs/tables/*_metrics_*.csv`
- `outputs/figures/<site>/*.png`
