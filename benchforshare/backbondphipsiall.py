import MDAnalysis as mda
from MDAnalysis.analysis import dihedrals
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  # Optional if using pandas

# Load your Tinker trajectory and topology files
u = mda.Universe('9_topology.pdb', 'Input_final.arc')

# Select the backbone atoms for the Ramachandran plot
bb = u.select_atoms('protein and backbone')

# Calculate the phi/psi angles
rama = dihedrals.Ramachandran(bb).run(start=2500)

# Extract phi and psi angles (flattening over all frames)
phi_psi_angles = rama.angles.reshape(-1, 2)  # Combine all frames and residues into one array

# Extract phi and psi angles from the reshaped array
phi = phi_psi_angles[:, 0]  # Phi angles
psi = phi_psi_angles[:, 1]  # Psi angles

# Save the phi and psi angles into a CSV file using numpy
np.savetxt('phi_psi_angles_all.csv', phi_psi_angles, delimiter=',', header='phi,psi', comments='')
