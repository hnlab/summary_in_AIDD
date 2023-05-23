#!/bin/bash
#$ -N chemprop_interpret 
#$ -q honda
##$ -l gpu=1
#$ -pe honda 28
##$ -l hostname=!k224.hn.org
#$ -o /home/shxie/aiddsummary/antibaumannii/reproduction/out
#$ -e /home/shxie/aiddsummary/antibaumannii/reproduction/error
#$ -wd /home/shxie/aiddsummary/antibaumannii/reproduction
chemprop_interpret --data_path interpret_train.csv --checkpoint_dir /home/shxie/aiddsummary/antibaumannii/models/final_model --property_id 1 --features_generator rdkit_2d_normalized --no_features_scaling