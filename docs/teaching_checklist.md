# Teaching Checklist (PT/EN)

## PT
- Configure o ambiente Python e instale dependencias (`requirements.txt`).
- Execute o pipeline completo: `python -m scripts.cli all --year 2024`.
- Verifique os outputs esperados em `data/cleaned/`, `outputs/results/`, `outputs/tables/`, `outputs/figures/`.
- Leia `docs/methodology.md` antes de interpretar graficos e tabelas.
- Compare metricas diarias e mensais para cada metodo.
- Interprete os diagramas de Taylor (diario e mensal) por localidade.
- Identifique quais metodos funcionam melhor para cada clima e justifique.
- Documente o procedimento e inclua as figuras/tabelas principais.

### Entregaveis minimos
- 1 tabela de metricas diarias e 1 tabela de metricas mensais por localidade.
- 1 diagrama de Taylor diario e 1 mensal por localidade.
- 2 graficos de serie temporal (um por localidade) comparando com Penman-Monteith.
- 1 grafico de dispersao por localidade (metodo vs referencia).
- Relatorio curto (2–4 paginas) com conclusoes.

### Rubrica (sugestao)
- Reprodutibilidade (20%): pipeline executado e outputs organizados.
- Metodologia (20%): uso correto de metodos e justificativas.
- Analise (30%): interpretacao coerente de metricas e Taylor.
- Comunicacao (20%): clareza do texto e figuras.
- Organizacao (10%): estrutura e padrao de nomes.

## EN
- Set up the Python environment and install dependencies (`requirements.txt`).
- Run the full pipeline: `python -m scripts.cli all --year 2024`.
- Validate expected outputs in `data/cleaned/`, `outputs/results/`, `outputs/tables/`, `outputs/figures/`.
- Read `docs/methodology.md` before interpreting figures and tables.
- Compare daily vs monthly metrics for each method.
- Interpret Taylor diagrams (daily and monthly) by site.
- Identify which methods work best for each climate and justify.
- Document the procedure and include key figures/tables.

### Minimum deliverables
- 1 daily metrics table and 1 monthly metrics table per site.
- 1 daily and 1 monthly Taylor diagram per site.
- 2 time series plots (one per site) comparing with Penman-Monteith.
- 1 scatter plot per site (method vs reference).
- Short report (2–4 pages) with conclusions.

### Rubric (suggested)
- Reproducibility (20%): pipeline executed and outputs organized.
- Methodology (20%): correct use of methods and justification.
- Analysis (30%): coherent interpretation of metrics and Taylor.
- Communication (20%): clarity of text and figures.
- Organization (10%): structure and naming consistency.
