import os
import pandas as pd
import networkx as nx
from IG_lib import mol_graph_image
from mol_lib import FromXYZtoGraph, chem_formula, FromFormulaToMass, FromFormulaToNa
pwd_xyz = '/Users/tinaccil/Documents/GitHub/woon_query/xyz_files'
pwd_main = os.getcwd()
name = []
state = []
formula = []
energy = []
pwd_list = []
os.chdir(pwd_xyz)
list_file = os.listdir()
if '.DS_Store' in list_file:
    list_file.remove('.DS_Store')
for j,mol in enumerate(list_file):
    if '.xyz' in mol:
        path = pwd_xyz + '/' + mol
        with open(path,"r") as data:
            lines = data.readlines()
            for i,item in enumerate(lines):
                if 'Eh' in item:
                    tmp_e  = item.split()
                    tmp_e = tmp_e[2]
        tmp_bl = True
        tmp_mol = ''
        tmp_st = ''
        for i,item in enumerate(mol):
            if item == '_':
                tmp_bl = False
                continue
            if tmp_bl == True:
                tmp_mol = tmp_mol + item
            if tmp_bl == False:
                tmp_st = tmp_st + item
        name.append(tmp_mol)
        state.append(tmp_st[:-4])
        if 'l-' in tmp_mol or 'c-' in tmp_mol:
            tmp_mol = tmp_mol[2:]
        if 'Al' in tmp_mol or 'Si' in tmp_mol or 'P' in tmp_mol or 'S' in tmp_mol or 'F' in tmp_mol or 'Cl' in tmp_mol or 'Na' in tmp_mol or 'Li' in tmp_mol or 'Mg' in tmp_mol:
            tmp_chem = 'ERROR'
        else:
            tmp_chem = chem_formula(tmp_mol)
        formula.append(tmp_chem)
        energy.append(tmp_e)
        pwd_list.append(path)
os.chdir(pwd_main)
df_woonmol = pd.DataFrame()
df_woonmol['name'] = name
df_woonmol['formula'] = formula
df_woonmol['state'] = state
df_woonmol['pwd_xyz'] = pwd_list
df_woonmol['energy'] = energy
df_woonmol['Mass'] = df_woonmol.apply(lambda row: FromFormulaToMass(row['formula']), axis=1)
df_woonmol['Na'] = df_woonmol.apply(lambda row: FromFormulaToNa(row['formula']), axis=1)
df_woonmol.sort_values(by=['Na',"Mass"], inplace=True)
df_woonmol.reset_index(drop=True, inplace=True)
with open("Woon_molecules.csv","w+") as output:
	output.write(df_woonmol.to_csv(sep="\t", index=False))
with open("tmp/dataframe/Woon_molecules.csv","w+") as output:
	output.write(df_woonmol.to_csv(sep="\t", index=False))