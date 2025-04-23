#!/bin/bash
#SBATCH --account=welbornlab
#SBATCH --partition=v100_normal_q
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=1
#SBATCH --time=24:59:59

# Each node type has different modules avilable. Resetting makes the appropriate stack available
module reset
module load infer-skylake_v100/tinker9/1.4.0-nvhpc-21.11

# Run the example
echo "-------- Starting tinker9: `date` -------"

tinker9 dynamic  Input_final.xyz_3  80000000 1 20 4 300 1 > dynamics.log

echo "------- tinker9 has exited: `date` --------"
