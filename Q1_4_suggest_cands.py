from rdkit import Chem
from rdkit.Chem import Descriptors
import numpy as np
import pandas as pd
import sys

#候補を見つける関数
def suggest_cands(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        molecular_weight = Descriptors.MolWt(mol)
        ring_count = Descriptors.RingCount(mol) 
        logP = Descriptors.MolLogP (mol)
        num_h_donors = Descriptors.NumHDonors(mol)
        num_h_acceptors = Descriptors.NumHAcceptors(mol)
        #条件に当てはまるものを絞りこむ
        if molecular_weight < 500 and ring_count <= 4 and 1 <= logP <= 5 and (num_h_donors + num_h_acceptors) <= 10:
            return True
        else:
            return False
    else:
        return False

def main(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            smiles = line.strip()
            if suggest_cands(smiles):
                print("TRUE")
            else:
                print("FALSE")

if __name__ == '__main__':
    main(sys.argv[1])