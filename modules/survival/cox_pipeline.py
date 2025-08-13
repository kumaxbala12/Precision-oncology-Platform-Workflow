
import argparse, pandas as pd, matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--features', required=True)
    ap.add_argument('--survival', required=True)
    ap.add_argument('--outfig', required=True)
    args = ap.parse_args()

    feats = pd.read_csv(args.features)
    surv = pd.read_csv(args.survival)
    df = surv.merge(feats, left_on='id', right_on='id', how='inner')
    q1, q2 = df['F1'].quantile([1/3, 2/3])
    def grp(v):
        return 'Low' if v<=q1 else ('Mid' if v<=q2 else 'High')
    df['grp'] = df['F1'].apply(grp)

    km = KaplanMeierFitter()
    plt.figure()
    for g in ['Low','Mid','High']:
        sub = df[df['grp']==g]
        km.fit(sub['time'], sub['event'], label=g)
        km.plot_survival_function()
    plt.title('KM by F1 tertiles (demo)')
    plt.xlabel('Time'); plt.ylabel('Survival prob.')
    plt.tight_layout(); plt.savefig(args.outfig, dpi=200)

if __name__ == '__main__':
    main()
