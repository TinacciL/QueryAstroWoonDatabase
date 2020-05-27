import os
import pandas as pd
import networkx as nx
from IG_lib import mol_graph_image
from mol_lib import FromXYZtoGraph, chem_formula, CorrectErrorPwdMolecules

pwd_main = os.getcwd()

with open("dataframe/neutral_isomers.csv","r") as data:
	df_net = pd.read_csv(data, delimiter = '\t')
with open("dataframe/Woon_molecules.csv","r") as data:
	df_woon = pd.read_csv(data, delimiter = '\t')

for index, rows in df_woon.iterrows():
    try:
        tmp_f = rows.formula
        tmp_pwd = rows.pwd_xyz
        tmp_e = rows.energy
        df_woon_tmp = df_woon[df_woon['pwd_xyz'] == tmp_pwd]
        df_net_tmp = df_net[df_net['formula'] == tmp_f]
        if df_net_tmp.shape[0] > 0:
            tmp_pwd_net = df_net_tmp['pwd_struct'].tolist()
            tmp_id_net = df_net_tmp['ID'].tolist()
            tmp_con = []
            for i,item in enumerate(tmp_pwd_net):
                tmp_item = '/Users/tinaccil/Documents/GitHub/tmp/network/' + CorrectErrorPwdMolecules(item)
                xyz_pre = FromXYZtoGraph(tmp_pwd)
                xyz_opt = FromXYZtoGraph(tmp_item)
                nm = nx.algorithms.isomorphism.categorical_node_match('atom','atom')
                if nx.is_isomorphic(xyz_pre,xyz_opt, node_match=nm):
                    con = True
                else:
                    con = False
                tmp_con.append(con)
            df_net_tmp['Connectivity'] = tmp_con
            df_net_tmp = df_net_tmp[df_net_tmp['Connectivity'] == True]
            if df_net_tmp.shape[0] > 0:
                tmp_id_ok = df_net_tmp['ID'].tolist()[0]
            else:
                tmp_id_ok = 'NoConnettivity'
        else:
            tmp_id_ok = 'NoFormulaMatching'
        df_woon_tmp['ID'] = tmp_id_ok
        if index == 0:
            mol_woon_id = df_woon_tmp.copy()
        else:
            mol_woon_id = pd.concat([mol_woon_id,df_woon_tmp],ignore_index=True)
            mol_woon_id.reset_index(drop=True, inplace=True) 
        del df_woon_tmp
    except:
        print(rows.formula)

mol_woon_id.sort_values(by=['Na',"Mass"], inplace=True)
mol_woon_id.reset_index(drop=True, inplace=True)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(mol_woon_id)
with open("dataframe/Woon_molecules_new.csv","w+") as output:
	output.write(mol_woon_id.to_csv(sep="\t", index=False))
mol_woon_id = mol_woon_id[mol_woon_id['Na'] <6]
mol_woon_id = mol_woon_id[mol_woon_id['formula'] != 'ERROR']
mol_woon_id = mol_woon_id[mol_woon_id['ID'] != 'NoFormulaMatching']
mol_woon_id = mol_woon_id[mol_woon_id['ID'] != 'NoConnettivity']
mol_woon_id.reset_index(drop=True, inplace=True)
with open("dataframe/Woon_molecules_isomers_matching.csv","w+") as output:
	output.write(mol_woon_id.to_csv(sep="\t", index=False))