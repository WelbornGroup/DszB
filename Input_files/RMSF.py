import MDAnalysis as mda
from MDAnalysis.analysis import rms, align
from MDAnalysis.analysis.rms import RMSF
import matplotlib.pyplot as plt
import numpy as np
import csv


# import nglview as nv

import warnings
# suppress some MDAnalysis warnings about writing PDB files
warnings.filterwarnings('ignore')

# Load the Tinker XYZ file and the corresponding ARC file
u = mda.Universe('9_topology.pdb', 'Input_final.arc')


print(f'Number of atoms: {len(u.atoms)}')
print(f'Number of residues: {len(u.residues)}')
print(f'Number of frames: {len(u.trajectory)}')

num_equil_frames = 2500

#calculate the average structure of the C-alpha
average = align.AverageStructure(u, u, select='protein and name CA', ref_frame=0).run()


#store this structure as new universe
ref = average.results.universe

#align the trajectory to the reference structure
aligner = align.AlignTraj(u, ref, select='protein and name CA',  in_memory=True).run()

c_alphas = u.select_atoms('protein and name CA')


R = rms.RMSF(c_alphas).run(start=num_equil_frames)




# Define the file name for CSV output
csv_file = 'rmsf.csv'

# Write RMSF values to CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['residues', 'RMSF (Å)'])
    for i, value in enumerate(R.rmsf):
        writer.writerow([i + 1, f'{value:.3f}'])

print(f"RMSF values have been saved to '{csv_file}'")

