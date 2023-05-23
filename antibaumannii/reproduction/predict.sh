#!/bin/bash
#$ -N chemprop_interpret 
#$ -q honda
##$ -l gpu=1
#$ -pe honda 28
##$ -l hostname=!k224.hn.org
#$ -o /home/shxie/aiddsummary/antibaumannii/reproduction/out
#$ -e /home/shxie/aiddsummary/antibaumannii/reproduction/error
#$ -wd /home/shxie/aiddsummary/antibaumannii/reproduction
chemprop_predict --test_path ../data/combine_pos_smiles.csv.csv --checkpoint_dir ../models/final_model --preds_path predictions_pos_combine.csv --features_generator rdkit_2d_normalized --no_features_scaling
chemprop_predict --test_path ../data/combine_neg_smiles.csv.csv --checkpoint_dir ../models/final_model --preds_path predictions_neg_combine.csv --features_generator rdkit_2d_normalized --no_features_scaling