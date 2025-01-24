#Python code for extracting PLEC fingerprints

#Please cite: Tran-Nguyen, V.K., Camproux, A.C. & Taboureau, O. ClassyPose: A Machine-Learning Classification Model for Ligand Pose Selection Applied to Virtual Screening in Drug Discovery.

#The protocol-env environment must be set up to run this Python code. Please use the file protocol-env.yml in our MLSF-protocol repository: https://github.com/vktrannguyen/MLSF-protocol.

import pandas as pd
import oddt
import oddt.pandas as opd
from oddt.pandas import ChemDataFrame
from oddt.fingerprints import PLEC
from joblib import Parallel, delayed
from tqdm import tqdm

mol2 = opd.read_mol2("Pathway_to_the_(multi)mol2_file_containing_ligand_pose(s)")
mol2.columns = ['mol', 'mol_name']
mols = mol2['mol']
receptor = next(oddt.toolkit.readfile('mol2', 'Pathway_to_the_receptor_mol2_file'))

def parallel_plec(mol):
    feature = PLEC(mol, protein = receptor, size = 4096,
                  depth_protein = 4, depth_ligand = 2,
                  distance_cutoff = 4.5, sparse = False)
    return feature

num_cores = 20
features = Parallel(n_jobs = num_cores, backend = "multiprocessing")(delayed(parallel_plec)(mol) for mol in tqdm(mols))

d_plec = pd.DataFrame(features)
d_plec.to_csv('Pathway_to_the_CSV_file_containing_the_resulting_PLEC_fingerprint(s)', index=False, header=False)
