
import streamlit as st
from pathlib import Path

st.title("Precision Oncology Platform — Dashboard (Demo)")

res_dir = Path("results")
models_dir = res_dir / "models"
fig_dir = res_dir / "figures"

st.subheader("Models")
models = [str(p) for p in models_dir.glob("*.joblib")]
st.write(models if models else "No models yet — run `make demo`.")

st.subheader("Figures")
for fig in sorted(fig_dir.glob("*.png")):
    st.image(str(fig), caption=fig.name)
