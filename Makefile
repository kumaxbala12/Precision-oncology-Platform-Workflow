
.PHONY: setup test lint demo app

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt -r dev-requirements.txt

test:
	pytest -q

lint:
	flake8 modules

demo:
	snakemake -s workflow/snakemake/Snakefile -j 1

app:
	streamlit run app/streamlit_app.py
