import chemprop
arguments = [
    '--data_path', 'antibiotic_reproduction.csv',
    '--dataset_type', 'classification',
    '--num_iters', '20',
    "--config_save_path","/home/shxie/aiddsummary/antibio_reproduction/config.json"
    ]
args=chemprop.args.HyperoptArgs().parse_args(arguments)
chemprop.hyperparameter_optimization.hyperopt(args)
