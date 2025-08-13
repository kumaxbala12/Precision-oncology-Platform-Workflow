
# System Diagram (Text)
raw data (tiny CSV) --> Snakemake
  - bulk_rnaseq/train_classifier.py  -> results/models/bulk_clf.joblib
  - survival/cox_pipeline.py         -> results/figures/survival_km.png
  - drug_response/train_elasticnet   -> results/models/drug_elasticnet.joblib
  - multiomics/integrate_cca         -> results/figures/cca_scatter.png

Streamlit app reads `results/`.
