#!/bin/bash 
#BSUB -q short-serial 
#BSUB -o intercomparison_OLR_hrly.out 
#BSUB -e intercomparison_OLR_hrly.err 
#BSUB -W 06:00


source activate ACPC_intercomparison
python I_OLR_hrly.py


