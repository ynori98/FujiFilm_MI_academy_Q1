from rdkit import Chem
from rdkit.Chem import Descriptors
import numpy as np
import pandas as pd
import sys

#分子量を数える関数
def calc_molecular_weight(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        molecular_weight = Descriptors.MolWt(mol)
        return molecular_weight
    else:
        return None

def main(file_name):
    with open(file_name,'r') as file:
        for line in file:
            smiles = line.strip()
            molecular_weight = calc_molecular_weight(smiles)

            if molecular_weight is not None:
                print(molecular_weight)
            else:
                print(0)

if __name__ == '__main__':
    main(sys.argv[1])