import MDAnalysis as mda
from MDAnalysis.analysis import dihedrals
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  # Optional if using pandas

# Load your Tinker trajectory and topology files
u = mda.Universe('9_topology.pdb', 'Input_final.arc')

start_residue = 180
end_residue = 200

# Select the backbone atoms for the specified range of residues
bb = u.select_atoms(f'protein and resid {start_residue}:{end_residue} and backbone')

# Extract and print the residue names and numbers within the range for double-checking
residues_in_range = bb.residues
print("Residue numbers and names in the specified range:")
for res in residues_in_range:
    print(f"Residue {res.resid}: {res.resname}")

# Calculate the phi/psi angles
rama = dihedrals.Ramachandran(bb).run(start=2500)

# Extract phi and psi angles (flattening over all frames)
phi_psi_angles = rama.angles.reshape(-1, 2)  # Combine all frames and residues into one array

# Extract phi and psi angles from the reshaped array
phi = phi_psi_angles[:, 0]  # Phi angles
psi = phi_psi_angles[:, 1]  # Psi angles

# Save the phi and psi angles into a CSV file using numpy
np.savetxt('phi_psi_anglesloop3.csv', phi_psi_angles, delimiter=',', header='phi,psi', comments='')
