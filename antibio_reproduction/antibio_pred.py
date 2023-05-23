import chemprop
import pandas as pd

df = pd.read_csv("/home/shxie/aiddsummary/antibio_reproduction/pred_smiles.csv")
smiles_list = df.values.tolist()
df1 = df.copy(deep=True)
for i in range(20):
    arguments = [
        '--test_path', '/dev/null',
        '--preds_path', '/dev/null',
        '--checkpoint_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic/model_{}'.format(i)
    ] 
    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args,smiles=smiles_list)
    df1['preds_{}'.format(i)] = [x[0] for x in preds]
temp=df1[['preds_{}'.format(i) for i in range(20)]]
df1["pred_aver"]= temp.mean(axis=1)
df_pred_aver =df1.pred_aver
df1 = df1.drop("pred_aver",axis=1)
df1.insert(1,'pred_aver',df_pred_aver)
df1.to_csv("/home/shxie/aiddsummary/antibio_reproduction/pred_antibio_result.csv",index=0)


df = pd.read_csv("/home/shxie/aiddsummary/antibio_reproduction/pred_smiles.csv")
smiles_list = df.values.tolist()
df1 = df.copy(deep=True)
for i in range(20):
    arguments = [
        '--test_path', '/dev/null',
        '--preds_path', '/dev/null',
        '--features_generator', 'rdkit_2d_normalized',
        '--checkpoint_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic_rdkit/model_{}'.format(i)
    ] 
    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args,smiles=smiles_list)
    df1['preds_{}'.format(i)] = [x[0] for x in preds]
temp=df1[['preds_{}'.format(i) for i in range(20)]]
df1["pred_aver"]= temp.mean(axis=1)
df_pred_aver =df1.pred_aver
df1 = df.drop("pred_aver",axis=1)
df1.insert(1,'pred_aver',df_pred_aver)
df1.to_csv("/home/shxie/aiddsummary/antibio_reproduction/pred_antibio_rdkit_result.csv",index=0)



'''df = pd.read_csv("/home/shxie/aiddsummary/antibio_reproduction/pred_smiles.csv") 
arguments = [
        '--test_path', '/dev/null',
        '--preds_path', '/dev/null',
        '--checkpoint_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic/model_2']

smiles_list = df.values.tolist() 
args = chemprop.args.PredictArgs().parse_args(arguments)
preds = chemprop.train.make_predictions(args=args,smiles=smiles_list)'''



