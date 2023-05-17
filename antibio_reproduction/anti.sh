#!/bin/bash
#$ -N antibiotic_training
#$ -q honda
##$ -l gpu=1
#$ -pe honda 28
##$ -l hostname=!k224.hn.org
#$ -o /home/shxie/aiddsummary/antibio_reproduction/out
#$ -e /home/shxie/aiddsummary/antibio_reproduction/error
#$ -wd /home/shxie/aiddsummary/antibio_reproduction

python antibio_pred.py