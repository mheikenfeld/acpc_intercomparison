#!/bin/bash 
#BSUB -q short-serial 
#BSUB -o intercomparison_all.out 
#BSUB -e intercomparison_all.err 
#BSUB -W 12:00

source activate ACPC_intercomparison
python I_OLR_5min.py


