
import argparse, pandas as pd, numpy as np, joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--expr', required=True)
    ap.add_argument('--labels', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    expr = pd.read_csv(args.expr)
    labs = pd.read_csv(args.labels)
    df = labs.merge(expr, on='sample_id', how='inner')
    y = df['label'].astype(str).values
    X = np.log1p(df.drop(columns=['sample_id','label']).astype(float).values)

    le = LabelEncoder(); y_enc = le.fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.25, random_state=42, stratify=y_enc)
    sc = StandardScaler(); X_train = sc.fit_transform(X_train); X_test = sc.transform(X_test)

    clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    Path(Path(args.out).parent).mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, args.out)

if __name__ == '__main__':
    main()
