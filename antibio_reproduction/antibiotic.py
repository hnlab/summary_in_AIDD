import chemprop
arguments = [
    '--data_path', 'antibiotic_reproduction.csv',
    '--dataset_type', 'classification',
    '--save_dir', 'antibiotic',
    '--epochs', '30',
    '--save_smiles_splits',
    '--ensemble_size','20',
    "--split_sizes","0.9","0.1","0"
    ]
args = chemprop.args.TrainArgs().parse_args(arguments)
mean_score, std_score = chemprop.train.cross_validate(args=args, train_func=chemprop.train.run_training)