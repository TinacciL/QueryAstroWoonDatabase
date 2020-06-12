def test(directory):
    num = ['0','1','2','3','4','5','6','7','8','9']
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
            path = os.getcwd()
            tmp_files = os.listdir()
            out_file = item + '.out'
            info_file = item + '.info'
            if out_file in tmp_files:
                with open(out_file,"r") as data:
                    lines = data.readlines()
                    tmp_start = False
                    tmp_end = False
                    tmp_ok = False
                    data_occ = []
                    ref_line = '-'*61
                    for j,item_j in enumerate(lines):
                        if 'Orbital Energies and Occupations' in item_j:
                            tmp_start = True
                        if tmp_start == True and ref_line in item_j and tmp_ok == True:
                            tmp_end = True
                            tmp_start = False
                            tmp_ok = False
                        elif tmp_start == True and ref_line in item_j and tmp_ok == False:
                            tmp_ok = True
                        if tmp_ok == True and ref_line not in item_j:
                            tmp_d = item_j.strip().split()
                            if len(tmp_d[0]) == 1:
                                if tmp_d[0] in num:
                                    if len(tmp_d[1]) > 6:
                                        tmp_d.insert(1,'0.0000')
                                    data_occ.append(tmp_d)
                            if len(tmp_d[0]) == 2:
                                if tmp_d[0][0] in num:
                                    if len(tmp_d[1]) > 6:
                                        tmp_d.insert(1,'0.0000')
                                    data_occ.append(tmp_d)
                    if len(data_occ) != 0:
                        spin_m = str(FromXtbToSpinM(data_occ))
                    else:
                        spin_m = 'error'
                    print(item, spin_m)
            os.chdir(tmp_dir)
        os.chdir(mol_dir)
    os.chdir(main)
    return(data_occ)

#out_file = 'C3O1_4.out'
#out_file = 'H2N1_0.out'
#out_file = 'H1C1_0.out'          
#out_file = 'C1_0.out'
#out_file = 'O1_0.out'
#out_file = 'H2C3_3.out'
#with open(info_file,"a") as data:
#    data.write('Spin_M: ' + spin_m + '\n')
#tmp_n = lines[9].split()
#tmp_n = tmp_n[1]
#tmp_out = path + '/' + tmp_n + '/' + tmp_n + '.out'
#os.system("cp " + tmp_out + " " + tmp_n[:-4] + ".out")
#tmp_ts = int(float(tmp_s)*2)
#tmp_n = item + '_S_' + str(tmp_ts)

data_occ = test('molecules')


xtb_pwd = df_mol['pwd_xyz_xtb'].tolist()
tmp_s = []
for i,item in enumerate(xtb_pwd):
    tmp = item[0:-11] + '.info'
    with open(tmp,"r") as info:
        lines = info.readlines()
        for j,item_j in enumerate(lines):
            if 'Spin_M:' in item_j:
                tmp_i = item_j.strip().split()
                tmp_s.append(tmp_i[1])
    print(tmp,tmp_s[i])
df_mol['multiplicity_xtb'] = tmp_s
df_mol = df_mol[['name','formula','ID','Na','Mass','state_woon','multiplicity_woon','energy(kJ/mol)_woon','spin_input_xtb','multiplicity_xtb','energy(kJ/mol)_xtb','pwd_xyz_woon','pwd_xyz_xtb']]
with open("/Users/tinaccil/Documents/GitHub/woon_query/data_analysis/dataframe/molecules_info.csv","w+") as output:
	output.write(df_mol.to_csv(sep="\t", index=False))