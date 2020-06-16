import os
import pandas as pd
import numpy as np
from mol_lib import CorrectErrorPwdMolecules, FromHeToKJmol, FromNetworkDataFrameToNetworkClassList

with open("/Users/tinaccil/Documents/GitHub/woon_query/tmp/dataframe/Woon_molecules_isomers_matching.csv","r") as data:
	df_woon_mol = pd.read_csv(data, delimiter = '\t')
with open("/Users/tinaccil/Documents/GitHub/woon_query/tmp/dataframe/neutral_isomers.csv","r") as data:
	df_mol_xtb = pd.read_csv(data, delimiter = '\t')
with open("/Users/tinaccil/Documents/GitHub/woon_query/tmp/dataframe/network_isomers_woon.csv","r") as data:
	df_net_woon = pd.read_csv(data, delimiter = '\t')

df_net_woon = df_net_woon.drop(columns="Reaction_Energy")
df_net_woon = df_net_woon.drop(columns="Reaction_Energy_Woon")
df_net_woon.rename(columns={'Reaction_Energy(kJ/mol)':'Reaction_Energy(kJ/mol)_xtb','Reaction_Energy_Woon(kJ/mol)':'Reaction_Energy(kJ/mol)_Woon','ID':'ID_kida'}, inplace=True)

df_woon_mol['energy(kJ/mol)_woon'] = df_woon_mol.apply(lambda row: FromHeToKJmol(row['energy']), axis=1)
df_woon_mol = df_woon_mol.drop(columns="energy")

tmp_state_list = df_woon_mol['state'].tolist()
tmp_spin = []
num = ['0','1','2','3','4','5','6','7','8','9']
for i,item in enumerate(tmp_state_list):
	if item[0] in num:
		tmp_spin.append(item[0])
	else:
		tmp_spin.append('ERROR')
df_woon_mol['multiplicity_woon'] = tmp_spin
df_woon_mol.rename(columns={'pwd_xyz':'pwd_xyz_woon'}, inplace=True)
df_woon_mol.rename(columns={'state':'state_woon'}, inplace=True)
df_woon_mol = df_woon_mol[['name','formula','ID','Na','Mass','state_woon','multiplicity_woon','pwd_xyz_woon','energy(kJ/mol)_woon']]

tmp_pwd_net = df_mol_xtb['pwd_struct'].tolist()
tmp_pwd = []
for i,item in enumerate(tmp_pwd_net):
	tmp_pwd.append('/Users/tinaccil/Documents/GitHub/molecules_database/' + CorrectErrorPwdMolecules(item))
df_mol_xtb = df_mol_xtb.drop(columns="pwd_struct")
df_mol_xtb['pwd_xyz_xtb'] = tmp_pwd
df_mol_xtb['energy(kJ/mol)_xtb'] = df_mol_xtb.apply(lambda row: FromHeToKJmol(row['E_tot']), axis=1)
df_tmp_n = df_mol_xtb.copy()

df_tmp_n = df_tmp_n.drop(["Mass","Na","H(0K)","formula","E_tot"], axis=1)
df_tmp_n.rename(columns={'Spin':'spin_input_xtb',}, inplace=True)

df_molecules = pd.merge(left=df_woon_mol, right=df_tmp_n, how='left', left_on='ID', right_on='ID')
df_molecules = df_molecules[['name','formula','ID','Na','Mass','state_woon','multiplicity_woon','energy(kJ/mol)_woon','spin_input_xtb','multiplicity_xtb','energy(kJ/mol)_xtb','pwd_xyz_woon','pwd_xyz_xtb']]

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df_net_woon)

net = FromNetworkDataFrameToNetworkClassList(df_net_woon)
tmp_id = []
main = os.getcwd()
os.chdir('reaction_image')
for i,item in enumerate(net):
    #print(net[i].reactants, net[i].products)
    tmp = net[i]
    name = 'reaction_' + str(i) + '.png'
    FromReactionClassToImage(net[i],name,df_molecules)
    tmp_id.append('reaction_' + str(i))
os.chdir(main)
df_net_woon['Reaction_Image'] = tmp_id

with open("dataframe/molecules_info.csv","w+") as output:
	output.write(df_molecules.to_csv(sep="\t", index=False))
with open("dataframe/network.csv","w+") as output:
	output.write(df_net_woon.to_csv(sep="\t", index=False))	