import chemprop
arguments = [
        '--data_path', '/home/shxie/aiddsummary/antibio_reproduction/reprod_total.csv',
        '--dataset_type', 'classification',
        '--save_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic_rdkit_total/model_single',
        '--epochs', '30',
        '--save_smiles_splits',
        #"--split_sizes","0.9","0.1","0",
        "--features_generator","rdkit_2d_normalized"
        "--config_path","/home/shxie/aiddsummary/antibio_reproduction/configew.json"
        ]

args = chemprop.args.TrainArgs().parse_args(arguments)
mean_score, std_score = chemprop.train.cross_validate(args=args, train_funccd=chemprop.train.run_training)

arguments = [
        '--data_path', '/home/shxie/aiddsummary/antibio_reproduction/reprod_total.csv',
        '--dataset_type', 'classification',
        '--save_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic_total/model_single',
        '--epochs', '30',
        '--save_smiles_splits',
        #"--split_sizes","0.9","0.1","0",
        #"--features_generator","rdkit_2d_normalized"
        "--config_path","/home/shxie/aiddsummary/antibio_reproduction/configew.json"
        ]

args = chemprop.args.TrainArgs().parse_args(arguments)
mean_score, std_score = chemprop.train.cross_validate(args=args, train_funccd=chemprop.train.run_training)


for i in range(20):
    arguments = [
        '--data_path', '/home/shxie/aiddsummary/antibio_reproduction/reprod_total.csv',
        '--dataset_type', 'classification',
        '--save_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic_rdkit_total/model_{}'.format(i),
        '--epochs', '30',
        '--save_smiles_splits',
        "--split_sizes","0.9","0.1","0",
        "--features_generator","rdkit_2d_normalized"
        "--config_path","/home/shxie/aiddsummary/antibio_reproduction/configew.json"
        ]
    args = chemprop.args.TrainArgs().parse_args(arguments)
    mean_score, std_score = chemprop.train.cross_validate(args=args, train_funccd=chemprop.train.run_training)

for i in range(20):
    arguments = [
        '--data_path', '/home/shxie/aiddsummary/antibio_reproduction/reprod_total.csv',
        '--dataset_type', 'classification',
        '--save_dir', '/home/shxie/aiddsummary/antibio_reproduction/antibiotic_total/model_{}'.format(i),
        '--epochs', '30',
        '--save_smiles_splits',
        "--split_sizes","0.9","0.1","0",
        #"--features_generator","rdkit_2d_normalized"
        "--config_path","/home/shxie/aiddsummary/antibio_reproduction/configew.json"
        ]
    args = chemprop.args.TrainArgs().parse_args(arguments)
    mean_score, std_score = chemprop.train.cross_validate(args=args, train_funccd=chemprop.train.run_training)