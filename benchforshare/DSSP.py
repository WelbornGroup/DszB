import MDAnalysis as mda
from MDAnalysis.analysis.dssp import DSSP
import pandas as pd

# Load entire system
u = mda.Universe("9_topology.pdb", "Input_final.arc")

# Select just the protein residues
protein = u.select_atoms("protein")
print(f"Protein Residues: {len(protein.residues)}")

# Run DSSP on the protein selection
dssp_analysis = DSSP(protein)
dssp_analysis.run()

# The DSSP result is a list of strings, one per frame, one character per protein residue
all_dssp = dssp_analysis.results.dssp

# Create a DataFrame
#   - each row = one frame
#   - each column = one protein residue
dssp_matrix = [list(frame_dssp) for frame_dssp in all_dssp]

# Make residue labels (e.g., 351A, 352A, etc. or resname+resid, etc.)
res_labels = [f"{res.resname}{res.resid}" for res in protein.residues]

df = pd.DataFrame(dssp_matrix, columns=res_labels)
df.index.name = "Frame"

df.to_csv("protein_secondary_structure.csv")
print("Saved DSSP assignments to protein_secondary_structure.csv")

