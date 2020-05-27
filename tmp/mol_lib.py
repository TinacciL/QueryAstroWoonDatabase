import numpy as np
import networkx as nx
import itertools
import os
import pandas as pd
from rdkit import Chem
from IG_lib import isomers_generator, tree_image, mol_graph_image, atoms_property
from rdkit.Chem import AllChem
from openbabel import openbabel
from ase import io, neighborlist

def FromHeToKJmol(Eh):
    tmp = Eh *  6.02214076 * 100 * 4.359748199
    return(tmp)

def FromKJmolToK(KJmol):
    tmp = KJmol / 0.0083144621
    return(tmp)

def FromFormulaToMass(formula):
	atoms = ['H','C','N','O']
	num = ['0','1','2','3','4','5','6','7','8','9']
	n_n = [1.00784,12.0107,14.0067,15.999]
	n_a = [0,0,0,0]
	if formula == 'ERROR':
		tmp_m  = 0
	else:
		for j in range(len(formula)):
			for k in range(len(atoms)):
				if formula[j] == atoms[k]:
					if j + 3 == len(formula):
						if formula[j+1] in num and formula[j+2] in num:
							n_a[k] = int(formula[j+1]+formula[j+2])
					elif j + 2 == len(formula):
						n_a[k] = int(formula[j+1])
					else:
						if formula[j+1] in num and formula[j+2] in num:
							n_a[k] = int(formula[j+1]+formula[j+2])
						elif formula[j+1] in num:
							n_a[k] = int(formula[j+1])
		tmp_m = n_a[0] * n_n [0] + n_a[1] * n_n [1] + n_a[2] * n_n [2] + n_a[3] * n_n [3]
	return(tmp_m)

def FromFormulaToNa(formula):
	atoms = ['H','C','N','O']
	num = ['0','1','2','3','4','5','6','7','8','9']
	n_at = [1,6,7,8]
	n_a = [0,0,0,0]
	if formula == 'ERROR':
		tmp_na = 0
	else:
		for j in range(len(formula)):
			for k in range(len(atoms)):
				if formula[j] == atoms[k]:
					if j + 3 == len(formula):
						if formula[j+1] in num and formula[j+2] in num:
							n_a[k] = int(formula[j+1]+formula[j+2])
					elif j + 2 == len(formula):
						n_a[k] = int(formula[j+1])
					else:
						if formula[j+1] in num and formula[j+2] in num:
							n_a[k] = int(formula[j+1]+formula[j+2])
						elif formula[j+1] in num:
							n_a[k] = int(formula[j+1])
		tmp_na = n_a[0] + n_a[1] + n_a[2] + n_a[3]
	return(tmp_na)

def MolFromGraphs(G):
	'''
	Function that takes as input the networkx graph (each node must have an atom property H,N,C,O etc) and return the mol (rdkit) object
	the function dont discriminate between different type of bond, it care only about the connectivity
	'''
	#https://stackoverflow.com/questions/51195392/smiles-from-graph
	# extract the adjacency matrix and the list of atoms
	adjacency_matrix = nx.adjacency_matrix(G).todense().tolist()
	node_list = []
	for i,node in enumerate(G):
		node_list.append(G.nodes[i]['atom'])
	# create empty editable mol object
	mol = Chem.RWMol()
	# add atoms to mol and keep track of index
	node_to_idx = {}
	for i in range(len(node_list)):
		a = Chem.Atom(node_list[i])
		molIdx = mol.AddAtom(a)
		node_to_idx[i] = molIdx
	# add bonds between adjacent atoms
	for ix, row in enumerate(adjacency_matrix):
		for iy, bond in enumerate(row):
			# only traverse half the matrix
			if iy >= ix:
				break
			# add relevant bond type (there are many more of these)
			if bond == 0:
				continue
			else:
				bond_type = Chem.rdchem.BondType.SINGLE
				mol.AddBond(node_to_idx[ix], node_to_idx[iy], bond_type)
			#elif bond == 2:
			#    bond_type = Chem.rdchem.BondType.DOUBLE
			#    mol.AddBond(node_to_idx[ix], node_to_idx[iy], bond_type)
	mol.UpdatePropertyCache(strict=False)
	for at in mol.GetAtoms():
		if at.GetAtomicNum() == 7 and at.GetExplicitValence()==4 and at.GetFormalCharge()==0:
			at.SetFormalCharge(1)
	#Chem.SanitizeMol(mol,Chem.SANITIZE_SYMMRINGS|Chem.SANITIZE_SETCONJUGATION|Chem.SANITIZE_SETHYBRIDIZATION)       
	Chem.SanitizeMol(mol)
	return mol

def FromXYZtoGraph(input_file):
    atoms = ['H','C','N','O']
    atomic_numb = [1,6,7,8]

    mol = io.read(input_file)
    #compute neighbor of the atoms in xyz format
    cutOff = neighborlist.natural_cutoffs(mol)
    neighborList = neighborlist.NeighborList(cutOff, self_interaction=False, bothways=True)
    neighborList.update(mol)
    #compure adjacency matrix and atoms list
    adj_matrix = neighborList.get_connectivity_matrix(sparse=False)
    Natom_list = mol.get_atomic_numbers()
    atoms_list = []
    for i,item in enumerate(Natom_list):
        for k in range(len(atomic_numb)):
            if item == atomic_numb[k]:
                atoms_list.append(atoms[k]) 
    #convert in networkx-molecules graph
    G=nx.from_numpy_matrix(adj_matrix)
    for i,item in enumerate(atoms_list):
        tmp_attr = {'atom': item}
        G.nodes[i].update(tmp_attr.copy())
    return(G)

def chem_formula(form):
	charge = ''
	if form[-1] == '+' or form[-1] == '-':
		charge = form[-1]
		form = form[:-1]

	num = ['0','1','2','3','4','5','6','7','8','9']
	atoms = ['H','C','N','O']
	n_a = [0,0,0,0]
	name = ''
	for j in range(len(form)):
		if form[j] in atoms:
			if j == len(form) - 1:
				for k in range(len(atoms)):
					if form[j] == atoms[k]:
						n_a[k] = n_a[k] + 1
			elif j == len(form) - 2:
				if form[j+1] in num:
					tmp_n = int(form[j+1])
					for k in range(len(atoms)):
						if form[j] == atoms[k]:
							n_a[k] = n_a[k] + tmp_n
				else:
					for k in range(len(atoms)):
						if form[j] == atoms[k]:
							n_a[k] = n_a[k] + 1
			else:
				if form[j+1] in num and form[j+2] in num:
					tmp_n = int(form[j+1]+form[j+2])
					for k in range(len(atoms)):
						if form[j] == atoms[k]:
							n_a[k] = n_a[k] + tmp_n
				elif form[j+1] in num:
					tmp_n = int(form[j+1])
					for k in range(len(atoms)):
						if form[j] == atoms[k]:
							n_a[k] = n_a[k] + tmp_n
				else:
					for k in range(len(atoms)):
						if form[j] == atoms[k]:
							n_a[k] = n_a[k] + 1
		elif form[j] in num:
			continue 					        
		else:
			name = 'ERROR'
			break

	if name != 'ERROR':		
		for i,ix in enumerate(atoms):
			if n_a[i] != 0:
				name = name + ix + str(n_a[i])
		name  = name + charge		
	return(name)

def extract_raw(df,query):
    tmp_i = None
    for i in range(df.shape[0]):
        if df.iloc[i,0] == query:
            tmp_i = i
    if tmp_i == None:
        print("Not found")
    else:    
        print(df.iloc[tmp_i,0])     
    return(tmp_i)

class reaction:
	def __init__(self,rct):
		#Reactants rct[0:3] deleting empty element
		if type(rct[0]) != list:
			if rct[1] == 'nan' and rct[2] == 'nan':
				self.reactants    = [rct[0]]
			elif rct[1] != 'nan' and rct[2] == 'nan':
				self.reactants    = rct[0:2]
			else:
				self.reactants    = rct[0:3]

			if   rct[4] == 'nan' and rct[5] == 'nan' and rct[6] == 'nan':
				self.products     = [rct[3]]
			elif rct[4] != 'nan' and rct[5] == 'nan' and rct[6] == 'nan':
				self.products     = rct[3:5]
			elif rct[4] != 'nan' and rct[5] != 'nan' and rct[6] == 'nan':
				self.products     = rct[3:6]
			else:
				self.products     = rct[3:7]
		else:
			self.reactants    = rct[0]
			self.products     = rct[1]	

def xtb_isomers(formula):
	charge = 0
	formula_r = formula
	if '+' in formula:
		charge = +1
		formula_r = formula[:-1]
	elif '-' in formula:
		charge = -1
		formula_r = formula[:-1]

	atoms = ['H','C','N','O']
	n_a = [0,0,0,0]
	for j in range(0,len(formula_r),2):
		for k in range(len(atoms)):
			if formula_r[j] == atoms[k]:
				n_a[k] = int(formula_r[j+1])

	n_electron = n_a[0] * 1 + n_a[1] * 4 + n_a[2] * 5 + n_a[3] * 6 - charge
	if n_electron % 2 == 0:
		spin = [0,2]
	else:
		spin = [1,3]	
	special_mol = ['H1','H2','C1','C2','N1','N2','O1','O2', 'C1O1']
	if formula_r in special_mol:
		spin = [0,1,2,3]

	n_t = n_a[0] + n_a[1] + n_a[2] + n_a[3]   
	name  = formula_r

	if n_t == n_a[0]:
		if n_a[0] == 1:
			G = nx.Graph()
			G.add_node(0)
			tmp_attr = {'atom': 'H'}
			G.nodes[0].update(tmp_attr.copy())
			struct = [G]
		elif n_a[0] == 2:
			G = nx.Graph()
			G.add_node(0)
			G.add_node(1)
			tmp_attr = {'atom': 'H'}
			G.nodes[0].update(tmp_attr.copy())
			G.nodes[1].update(tmp_attr.copy())
			G.add_edge(0,1)
			mol_graph_image(G)
			struct = [G]
	else:	
		tree = isomers_generator(n_a[0],n_a[1],n_a[2],n_a[3])
		struct = []
		for i,node in enumerate(tree):
			if tree.nodes[i]['block'] == 'hydrogen':
				struct.append(tree.nodes[i]['graph'].copy())
				#mol_graph_image(tree.nodes[i]['graph'].copy())

	mols = []
	for i,item in enumerate(struct):
		tmp_mol = MolFromGraphs(item)
		#tmp_sml = Chem.MolToSmiles(tmp_mol)
		AllChem.EmbedMolecule(tmp_mol)
		AllChem.UFFOptimizeMolecule(tmp_mol)
		#tmp_mol.SetProp('_Name',tmp_sml)
		tmp_name = name + '_' + str(i) + '.mol'
		mols.append(tmp_name[:-4])
		tmp_name = name + '_' + str(i) + '.xyz'	
		with open(tmp_name, "w+") as file_mol:
			file_mol.write(Chem.MolToXYZBlock(tmp_mol))	
		if tmp_mol.GetNumAtoms() != n_t:
			print(tmp_name,'Error: number atoms in rdkit transformation to mol not conserved')     
		
	main  = os.getcwd()
	os.system("mkdir " + formula)
	for i,item in enumerate(mols):
		os.system("mv " + item + ".xyz " + formula)
	os.chdir(formula)
	sub_main = os.getcwd()

	for i,item in enumerate(mols):
		os.system("mkdir " + item)
		os.system("mv " + item + ".xyz " + item)
		os.chdir(item)
		iso_dir = os.getcwd()
		info_mols = []
		for j in range(len(spin)):
			tmp_name = item + '_S_' + str(spin[j])
			os.system("mkdir " + tmp_name)
			os.system("cp " + item + ".xyz " + tmp_name + ".xyz")
			os.system("mv " + tmp_name + ".xyz " + tmp_name)
			os.chdir(tmp_name)
			tmp_n = tmp_name + ".xyz"
			tmp_i = tmp_name + ".input"
			tmp_c = tmp_name + ".CHRG"
			tmp_u = tmp_name + ".UHF"
			with open(tmp_i, "w+") as xctrl:
				xctrl.write("$thermo\n")
				xctrl.write("temp=298.15,120,100,80,60,40,20,10\n")
				xctrl.write("$chrg " + str(charge) +  "\n")
				xctrl.write(str(charge) + "\n")
				xctrl.write("$spin " + str(spin[j]) + "\n")
				xctrl.write(str(spin[j]) + "\n")	
			os.system("xtb " + "--input " + tmp_i + " " + tmp_n + " --ohess " + "--molden " + "--namespace " + tmp_name + " > " + tmp_name + ".out output.out" )
			info_mols.append(xtbInfoFile(tmp_name))
			os.chdir(iso_dir)
		tmp_xtb = ChooseXtbCalculation(info_mols)
		if tmp_xtb != None:
			path = tmp_xtb[0] + '/' + tmp_xtb[0]
			os.system("cp " + path + ".info " + tmp_xtb[0][:-4] + ".info")
			os.system("cp " + path + ".xtbopt.xyz " + tmp_xtb[0][:-4] + ".xtbopt.xyz")	
		os.chdir(sub_main)
	os.chdir(main)
	return()

def ChooseXtbCalculation(info_mols):
    info = []
    for i,item in enumerate(info_mols):
        #delete no succesfull optimization
        if item[5] == 'error':
            continue
        #delete optimization with different connectivity from starting isomer    
        if item[1] == 'False':
            continue
        info.append(item)
    #choose the right calulation    
    if len(info) == 0:
        return(None)
    if len(info) == 1:
        return(info[0])
    if len(info) > 1:
        tmp = info[0]
        for i,item in enumerate(info):
            if i == 0:
                continue
            # choose isomers more stable, if the isomer with higher spin molteplicity is more stable I choose it only if it is more stable then 1e-5
            # the accuracy of xtb is 1e-12 
            if (float(tmp[5]) - float(item[5])) < 1e-5:
                continue
            else:
                tmp = item    
        return(tmp)

def xtbInfoFile(name):
	list_file = os.listdir()
	name_out = name + '.out'
	name_xyz = name + ".xyz"
	name_opt = name + ".xtbopt.xyz"
	if name_out in list_file and name_opt in list_file and name_xyz in list_file:
		with open(name_out,"r") as data:
			lines = data.readlines()
			tmp_t = False
			for i,item in enumerate(lines):
				if i == 63:
					tmp = item.split()
					electron = tmp[4]
				if i == 64:
					tmp = item.split()
					if len(tmp[2]) == 1:
						tmp[2] = '+' + tmp[2]
					charge = tmp[2]
				if i == 65:
					tmp = item.split()
					spin = tmp[2]
				if 'THERMODYNAMIC' in item:
					tmp  = lines[i+2].split()
					G_10 = tmp[4]
					tmp  = lines[i+4].split()
					E_t  = tmp[3]
					tmp  = lines[i+5].split()
					ZPE = tmp[4]
					H_0 = str(float(E_t) + float(ZPE))
					tmp_t = True
				if 'TOTAL ENTHALPY'	in item:
					tmp  = item.split()
					H_10 = tmp[3]	
			if tmp_t == False:
				electron = 'error'
				charge = 'error'
				spin = 'error'                
				G_10 = 'error'
				H_10 = 'error'                
				H_0 = 'error'
				ZPE = 'error'
				E_t = 'error'
		xyz_pre = FromXYZtoGraph(name_xyz)
		xyz_opt = FromXYZtoGraph(name_opt)
		nm = nx.algorithms.isomorphism.categorical_node_match('atom','atom')
		if nx.is_isomorphic(xyz_pre,xyz_opt, node_match=nm):
			con = "True"
		else:
			con = "False"
	else:
		con = 'error'
		electron = 'error'
		charge = 'error'
		spin = 'error'                
		G_10 = 'error'
		H_10 = 'error'                
		H_0 = 'error'
		ZPE = 'error'
		E_t = 'error'
		print("error in " + name)

	with open(name + '.info',"w+") as data:
		data.write('Opt_connettivity: ' + con + '\n')
		data.write('Electron: ' + electron + '\n')    
		data.write('Charge: ' + charge + '\n')
		data.write('Spin: ' + spin + '\n')
		data.write('E_tot: ' + E_t + '\n')    
		data.write('ZPE: ' + ZPE + '\n')
		data.write('H(0K): ' + H_0 + '\n')
		data.write('H(10K): ' + H_10 + '\n')
		data.write('G(10K): ' + G_10 + '\n')
	return([name,con,electron,charge,spin,E_t])

def ExtractDataFrameFromMolecules(directory):
	df_isomers = pd.DataFrame(columns = ['formula', 'E_tot', 'H(0K)', 'Spin','pwd_struct'])
	main = os.getcwd()
	os.chdir(directory)
	mol_dir = os.getcwd()
	mol_file_list = os.listdir()
	if '.DS_Store' in mol_file_list:
		mol_file_list.remove('.DS_Store')
	for k,mol in enumerate(mol_file_list):
		os.chdir(mol)
		tmp_dir = os.getcwd()
		list_file = os.listdir()
		if '.DS_Store' in list_file:
			list_file.remove('.DS_Store')
		for i,item in enumerate(list_file):
			os.chdir(item)
			tmp_files = os.listdir()
			info_file = item + '.info'
			if info_file in tmp_files:
				with open(info_file,"r") as data:
					lines = data.readlines()
					tmp_e = lines[4].split()
					tmp_e = tmp_e[1]
					tmp_s = lines[3].split()
					tmp_s = tmp_s[1]
					tmp_h = lines[6].split()
					tmp_h = tmp_h[1]
					tmp_p = 'molecules' + '/' + mol + '/' + item + '.xtbopt.xyz'
				tmp_df = pd.DataFrame()
				tmp_df['formula'] = [mol]
				tmp_df['E_tot']   = [tmp_e]
				tmp_df['H(0K)']   = [tmp_h]
				tmp_df['Spin']    = [tmp_s]
				tmp_df['pwd_struct'] = [tmp_p]    
				df_isomers = pd.concat([df_isomers,tmp_df],ignore_index=True)
				df_isomers.reset_index(drop=True, inplace=True) 
				del tmp_df
			os.chdir(tmp_dir)
		os.chdir(mol_dir)
	os.chdir(main)
	return(df_isomers)

def FromReactionClassToKidaDataFrame(network):
	tmp_R1 = []
	tmp_R2 = []
	tmp_R3 = []
	tmp_P1 = []
	tmp_P2 = []
	tmp_P3 = []
	tmp_P4 = []
	tmp_P5 = []

	if len(network.reactants) == 3:
		tmp_R1.append(network.reactants[0])
		tmp_R2.append(network.reactants[1])
		tmp_R3.append(network.reactants[2])
	elif len(network.reactants) == 2:
		tmp_R1.append(network.reactants[0])
		tmp_R2.append(network.reactants[1])
		tmp_R3.append('')
	elif len(network.reactants) == 1:
		tmp_R1.append(network.reactants[0])
		tmp_R2.append('')
		tmp_R3.append('')
	else:
		tmp_R1.append('')
		tmp_R2.append('')
		tmp_R3.append('')

	if len(network.products) == 5:
		tmp_P1.append(network.products[0])
		tmp_P2.append(network.products[1])
		tmp_P3.append(network.products[2])
		tmp_P4.append(network.products[3])
		tmp_P5.append(network.products[4])
	elif len(network.products) == 4:
		tmp_P1.append(network.reactants[0])
		tmp_P2.append(network.reactants[1])
		tmp_P3.append(network.reactants[2])
		tmp_P4.append(network.reactants[3])
		tmp_P5.append('')
	elif len(network.products) == 3:
		tmp_P1.append(network.products[0])
		tmp_P2.append(network.products[1])
		tmp_P3.append(network.products[2])
		tmp_P4.append('')
		tmp_P5.append('')
	elif len(network.products) == 2:
		tmp_P1.append(network.products[0])
		tmp_P2.append(network.products[1])
		tmp_P3.append('')
		tmp_P4.append('')
		tmp_P5.append('')
	elif len(network.products) == 1:
		tmp_P1.append(network.products[0])
		tmp_P2.append('')
		tmp_P3.append('')
		tmp_P4.append('')
		tmp_P5.append('')
	else:
		tmp_P1.append('')
		tmp_P2.append('')
		tmp_P3.append('')
		tmp_P4.append('')
		tmp_P5.append('')

	df_network = pd.DataFrame()
	df_network['R1'] = tmp_R1
	df_network['R2'] = tmp_R2
	df_network['R3'] = tmp_R3
	df_network['P1'] = tmp_P1
	df_network['P2'] = tmp_P2
	df_network['P3'] = tmp_P3
	df_network['P4'] = tmp_P4
	df_network['P5'] = tmp_P5
	return(df_network)

def FromNetworkFormulaToListNetworkID(tmp_n,df_isomers):
	tmp_l = []
	for i,item in enumerate(tmp_n.reactants):
		df_tmp = df_isomers[df_isomers['formula'] == item]
		tmp_r = df_tmp['ID'].tolist()
		tmp_l.append(tmp_r)
	for i,item in enumerate(tmp_n.products):
		df_tmp = df_isomers[df_isomers['formula'] == item]
		tmp_p = df_tmp['ID'].tolist()
		tmp_l.append(tmp_p)
	tmp_rl = []
	for item in itertools.product(*tmp_l):
		tmp_rl.append(item)
	tmp_list_net = []
	for k,rec in enumerate(tmp_rl):
		tmp_net = []
		tmp = []
		for i,item in enumerate(tmp_n.reactants):
			tmp.append(rec[i])
			tmp_i = i +1
		tmp_net.append(tmp.copy())
		tmp = []
		for i,item in enumerate(tmp_n.products):
			tmp.append(rec[i+tmp_i])
		tmp_net.append(tmp.copy())
		tmp_list_net.append(tmp_net)
	network_list = []
	for i,item in enumerate(tmp_list_net):
		network_list.append(reaction(item.copy()))
	return(network_list)

def ReactionEnthalpyCalculation(net,df_isomers):
	ent = []
	for i,items in enumerate(net):
		tmp_r = 0
		for j,item in enumerate(net[i].reactants):
			tmp = df_isomers.loc[df_isomers['ID'] == net[i].reactants[j]]
			if tmp.shape[0] != 0:
				if tmp.iloc[0,1] != None:
					tmp_r +=  float(tmp.iloc[0,1])
				else:
					tmp_r = None
					break
			else:
				tmp_r = None
				break
		tmp_p = 0    
		for j,item in enumerate(net[i].products):
			tmp = df_isomers.loc[df_isomers['ID'] == net[i].products[j]]
			if tmp.shape[0] != 0:
				if tmp.iloc[0,1] != None:
					tmp_p +=  float(tmp.iloc[0,1])
				else:
					tmp_p = None
					break
			else:
				tmp_p = None
				break
		if tmp_r is None or tmp_p is None:
			ent.append(None)
		else:
			tmp_e = tmp_p - tmp_r
			ent.append(tmp_e)
	return(ent)

def FromNetworkDataFrameToNetworkClassList(df_net):
    df_net = df_net.astype('str')
    net_list = []
    for index, rows in df_net.iterrows():
        my_list =[rows.R1, rows.R2, rows.R3, rows.P1, rows.P2, rows.P3, rows.P4]
        net_list.append(my_list)
    network = []
    for j,item in enumerate(net_list):
        network.append(reaction(item))
    return(network)

def CorrectErrorPwdMolecules(item):
    #item  = 'molecules/N1O2/N1O2_0.xtbopt.xyz'
    tmp_bl = False
    tmp_item = ''
    tmp_a = ''
    for j,item_j in enumerate(item):
        if j > 9:
            if item_j == '/':
                tmp_bl = True
            if tmp_bl == True:
                tmp_item = tmp_item + item_j
            else:
                tmp_a = tmp_a + item_j
    tmp_bl = True
    tmp_subf = ''
    for j,item_j in enumerate(tmp_item):
        if item_j == '.':
            tmp_bl = False
        if tmp_bl == True:
            tmp_subf = tmp_subf + item_j
    tmp_path  = item[:10] + tmp_a + tmp_subf +  tmp_item
    return(tmp_path)

