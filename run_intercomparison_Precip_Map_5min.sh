#!/bin/bash 
#BSUB -q short-serial 
#BSUB -o intercomparison_Precip_Map_5min.out 
#BSUB -e intercomparison_Precip_Map_5min.err 
#BSUB -W 06:00


source activate ACPC_intercomparison
conda env list
pwd
python I_Precip_Map_5min.py


