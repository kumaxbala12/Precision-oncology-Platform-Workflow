[![CI](https://img.shields.io/github/actions/workflow/status/your-username/precision-oncology-platform/ci.yml?branch=main)](https://github.com/your-username/precision-oncology-platform/actions) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![Made with Snakemake](https://img.shields.io/badge/pipeline-Snakemake-blue)](#) [![Docker](https://img.shields.io/badge/container-Docker-informational)](containers/Dockerfile)

# Precision Oncology Platform (Capstone)
Reproducible end-to-end platform showcasing bulk RNA-seq classification, multi-omics integration, drug response prediction, and survival modeling — with pipelines (Snakemake/Nextflow), Docker, tests, and a Streamlit dashboard.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r dev-requirements.txt
snakemake -s workflow/snakemake/Snakefile -j 1
streamlit run app/streamlit_app.py
```

## Running on HPC (SLURM) or AWS Batch

### Option A — Snakemake on SLURM (HPC)
Snakemake can submit jobs to SLURM using `--cluster` or a profile. Example (simple inline submit):
```bash
snakemake -s workflow/snakemake/Snakefile \  -j 50 \  --use-conda \  --cluster "sbatch -A <ACCOUNT> -t 02:00:00 -c 4 --mem=8G"
```
Tips:
- Replace `<ACCOUNT>` and resources with your cluster’s settings.
- Prefer **profiles** for cleaner configs (e.g., a `profiles/slurm/` folder with `cluster.yaml`).

### Option B — Nextflow with SLURM
We include a minimal Nextflow stub and a `slurm` profile in `workflow/nextflow/nextflow.config`.
```bash
cd workflow/nextflow
nextflow -C nextflow.config run main.nf -profile slurm
```
This will use `process.executor = 'slurm'` for submitted processes.

### Option C — Nextflow on AWS Batch
You’ll need an AWS Batch **compute environment**, **job queue**, and **job definition**.
1. Configure AWS credentials on your machine (`aws configure`) and ensure permissions.
2. Edit `workflow/nextflow/nextflow.config` to include an `awsbatch` profile:
```groovy
profiles {
  awsbatch {
    process.executor = 'awsbatch'
    aws.region = '<your-region>'
    aws.batch.queue = '<your-queue>'
    aws.batch.cliPath = 'aws'
  }
}
```
3. Run:
```bash
cd workflow/nextflow
nextflow -C nextflow.config run main.nf -profile awsbatch
```
Notes:
- Make sure your S3 buckets and ECR/Docker images (if any) are accessible.
- For real workloads, containerize each process and pin software versions.
