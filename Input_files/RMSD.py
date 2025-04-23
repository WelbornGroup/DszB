import MDAnalysis as mda
from MDAnalysis.analysis import rms
import pandas as pd
import matplotlib.pyplot as plt

# Load the Tinker trajectory
u = mda.Universe('9_topology.pdb', 'Input_final.arc')


print(f'Number of atoms: {len(u.atoms)}')
print(f'Number of residues: {len(u.residues)}')
print(f'Number of frames: {len(u.trajectory)}')


rmsd_analysis = rms.RMSD(u, select='name CA', ref_frame=0,)

# Run the RMSD calculation
rmsd_analysis.run()

# Inspect the shape of the RMSD results
print(rmsd_analysis.rmsd.shape)

# Create a DataFrame from the RMSD results 
rmsd_df = pd.DataFrame(rmsd_analysis.rmsd, columns=['Frame', 'time', 'name CA'])

# Save the DataFrame to a CSV file
csv_file = 'rmsd.csv'
rmsd_df.to_csv(csv_file, index=False)

print(f"RMSD results saved to {csv_file}")



