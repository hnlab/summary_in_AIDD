import chemprop
import pandas as pd
df = pd.read_csv("/home/shxie/aiddsummary/antibio_reproduction/zinc.csv")
smiles_list = df.values.tolist()
for i in range(20):
    arguments = [
        '--test_path', '/dev/null',
        '--preds_path', '/dev/null',
        '--checkpoint_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic_total/model_{}'.format(i)
    ]
    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args,smiles=smiles_list)
    df['preds_{}'.format(i)] = [x[0] for x in preds]
temp=df[['preds_{}'.format(i) for i in range(20)]]
df["pred_aver"]= temp.mean(axis=1)
df_pred_aver =df.pred_aver
df = df.drop("pred_aver",axis=1)
df.insert(1,'pred_aver',df_pred_aver)
df.to_csv("/home/shxie/aiddsummary/antibio_reproduction/pred_antibio_zinc_result.csv",index=0)

df = pd.read_csv("/home/shxie/aiddsummary/antibio_reproduction/zinc.csv")
smiles_list = df.values.tolist()
for i in range(20):
    arguments = [
        '--test_path', '/dev/null',
        '--preds_path', '/dev/null',
        "--features_generator","rdkit_2d_normalized"
        '--checkpoint_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic_rdkit_total/model_{}'.format(i)
    ]
    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args,smiles=smiles_list)
    df['preds_{}'.format(i)] = [x[0] for x in preds]
temp=df[['preds_{}'.format(i) for i in range(20)]]
df["pred_aver"]= temp.mean(axis=1)
df_pred_aver =df.pred_aver
df = df.drop("pred_aver",axis=1)
df.insert(1,'pred_aver',df_pred_aver)
df.to_csv("/home/shxie/aiddsummary/antibio_reproduction/pred_antibio_zinc_rdkit_result.csv",index=0)