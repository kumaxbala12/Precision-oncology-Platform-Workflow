
import argparse, pandas as pd, numpy as np, joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNetCV
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--expr', required=True)
    ap.add_argument('--resp', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    expr = pd.read_csv(args.expr)
    resp = pd.read_csv(args.resp)
    df = resp.merge(expr, on='sample_id', how='inner')
    y = df['response'].astype(float).values
    X = np.log1p(df.drop(columns=['sample_id','drug','response']).astype(float).values)

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)
    sc = StandardScaler(); X_tr = sc.fit_transform(X_tr); X_te = sc.transform(X_te)

    model = ElasticNetCV(cv=3, max_iter=2000, n_jobs=-1).fit(X_tr, y_tr)
    Path(Path(args.out).parent).mkdir(parents=True, exist_ok=True)
    joblib.dump(model, args.out)

if __name__ == '__main__':
    main()
