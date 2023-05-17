import chemprop
import pandas as pd

arguments = [
    '--test_path', 'antibiotic/fold_0/val_smiles.csv',
    '--preds_path', 'pred_antibio.csv',
    '--checkpoint_dir', 'antibiotic'
]
df = pd.read_csv("pred_antibio.csv")
args = chemprop.args.PredictArgs().parse_args(arguments)
preds = chemprop.train.make_predictions(args=args)
df['preds'] = [x[0] for x in preds]
df.to_csv("pred_antibio_result.csv")