#!/bin/bash
#$ -N chemprop
#$ -q honda
##$ -l gpu=1
#$ -pe honda 28
##$ -l hostname=!k224.hn.org
#$ -o /home/shxie/aiddsummary/antibio_reproduction/out
#$ -e /home/shxie/aiddsummary/antibio_reproduction/error
#$ -wd /home/shxie/aiddsummary/antibio_reproduction

python antibiotic.py
python antibio_pred.py
python antibiotic_total.py
python pred_zinc.py