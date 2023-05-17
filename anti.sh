#!/bin/bash
#$ -N antibiotic_training
#$ -q honda
##$ -l gpu=1
#$ -pe honda 28
##$ -l hostname=!k224.hn.org
#$ -o /home/shxie/little_rubbish_learning/out
#$ -e /home/shxie/little_rubbish_learning/error
#$ -wd /home/shxie/little_rubbish_learning

python antibio_pred.py