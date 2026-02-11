# data/cleaned

**PT**
Dados corrigidos/interpolados. Aqui ficam arquivos resultantes do tratamento de falhas, padronizacao de colunas e conversoes. Estes dados sao a base para agregacoes e metricas.

**EN**
Corrected/interpolated data. Files here result from cleaning missing values, standardizing columns, and conversions. These are the inputs for aggregation and metrics.

## Como reproduzir / How to reproduce
```bash
python -m scripts.cli clean --input data/raw/Evapo.xlsx --output data/cleaned
```
