#!/bin/bash 
#BSUB -q short-serial 
#BSUB -o intercomparison_Precip_Map_hrly.out 
#BSUB -e intercomparison_Precip_Map_hrly.err 
#BSUB -W 06:00


source activate ACPC_intercomparison
python I_Precip_Map_hrly.py


