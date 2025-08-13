
import argparse, pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cross_decomposition import CCA

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--expr', required=True)
    ap.add_argument('--meth', required=True)
    ap.add_argument('--labels', required=True)
    ap.add_argument('--outfig', required=True)
    args = ap.parse_args()

    expr = pd.read_csv(args.expr).sort_values('sample_id')
    meth = pd.read_csv(args.meth).sort_values('sample_id')
    labs = pd.read_csv(args.labels).sort_values('sample_id')

    X1 = np.log1p(expr.drop(columns=['sample_id']).astype(float).values)
    X2 = meth.drop(columns=['sample_id']).astype(float).values
    y = labs['label'].astype(str).values

    s1 = StandardScaler(); s2 = StandardScaler()
    X1s = s1.fit_transform(X1); X2s = s2.fit_transform(X2)
    k = min(2, X1s.shape[1], X2s.shape[1])
    cca = CCA(n_components=k, max_iter=1000)
    U, V = cca.fit_transform(X1s, X2s)
    comps = np.hstack([U, V])

    le = LabelEncoder(); y_enc = le.fit_transform(y)
    import matplotlib.pyplot as plt
    plt.figure()
    plt.scatter(comps[:,0], comps[:,1], c=y_enc, alpha=0.8)
    plt.xlabel('CCA1'); plt.ylabel('CCA2'); plt.title('CCA components (demo)')
    plt.tight_layout(); plt.savefig(args.outfig, dpi=200)

if __name__ == '__main__':
    main()
