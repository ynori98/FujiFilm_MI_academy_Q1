from rdkit import Chem
from rdkit.Chem import Descriptors
import numpy as np
import pandas as pd
import sys

def count_carbon_atoms(smiles):
    # SMILES表記をRDKitの分子オブジェクトに変換
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is not None:
        # 炭素原子の数を数える
        carbon_atoms = sum([1 for atom in mol.GetAtoms() if atom.GetAtomicNum() == 6])
        return carbon_atoms
    else:
        return None

def main(file_name):
        # ファイルからSMILES表記の化合物を読み取り、炭素原子の数を数える
    with open(file_name, 'r') as file:
        for line in file:
            smiles = line.strip()
            carbon_atoms = count_carbon_atoms(smiles)
        
            if carbon_atoms is not None:
                print(carbon_atoms)
            else:
                print(0)

if __name__ == '__main__':
    main(sys.argv[1])