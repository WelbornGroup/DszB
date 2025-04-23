#!/bin/bash
#SBATCH --account=welbornlab
#SBATCH --partition=v100_dev_q
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00

# Each node type has different modules avilable. Resetting makes the appropriate stack available
module reset
module load infer-skylake_v100/tinker9/1.4.0-nvhpc-21.11

# Run the example
echo "-------- Starting tinker9: `date` -------"

tinker9 minimize Input_final.xyz -k tinker.key 0.1 > min.log

echo "------- tinker9 has exited: `date` --------"
