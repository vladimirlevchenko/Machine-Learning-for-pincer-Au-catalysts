import os, shutil
import numpy as np

print(os.getcwd())
os.chdir("/Users/vladimirlevchenko/DokumenterHD/programming/Python/Subs_maker_Ligs_and_Pos/replacers_UPDATED/double_homo")

f = open("double_replacer.in","r")
template = f.read()
f.close

ligands_list = ["benzene",
                "bromide",
                "fluoride",
                "CH4",
                "nitro",
                "OMe",
                "phCO",
                "tBu",
                "phenol",
                "HSO2Me"]

positions_list = [28,30,29,26,19,9,7,16,14,20,11]

#print("..........Coefficient calculations..........")
#D = (len(ligands_list) - len(positions_list)) + 1

print("......Files generation.......")
print(" ")
print("len ligands", len(ligands_list))

def substitutor_double(ligands, positions):
    # First comes the unfreezed positions:
    pos = []
    for i in positions_list:
        pos.append([x for x in positions_list if x != i])
    # Now the file generation
    print(pos)
    for ligand in ligands:
        for i in range(len(positions)):
            for j in range(len(pos[i])):
                if not os.path.exists("double_input"): os.mkdir("double_input")
                shutil.copy("double_replacer.in", str(ligand))
                os.chdir("double_input")

                out = open("CCNAu_double_" + str(ligand)+"_"+str(positions[i])+"_"+str(pos[i][j])+"_"+str(ligand)+".in","w")
                template_out = template.replace("ligand_1", ligand).replace(
                "position_1", str(positions[i])).replace("position_2", str(pos[i][j])).replace(
                "ligand_2", str(ligand)
                ).replace("name_here", str("CCNAu_double_") + (str(ligand)+"_"+str(positions[i])+"_"+str(pos[i][j])+"_"+str(ligand)))

                out.write(template_out)
                out.close
                os.chdir("..")
            os.remove(str(ligand))

def duplicate_removal():
    """
    Removing complexes that are similarly substituted, for example complex with
    substitution pattern _Br_11_7_Br_ is equivalent to _Br_7_11_Br

    """
    os.chdir("/Users/vladimirlevchenko/DokumenterHD/programming/Python")
    new_path = os.chdir("Subs_maker_Ligs_and_Pos/replacers_UPDATED/double_homo/double_input")
    current_path = os.getcwd()
    print("-------REMOVING DUBLICATES-------")

    empty = []
    for filename in os.listdir(current_path):
        if filename.endswith(".in"):
            no_extension = os.path.splitext(filename)[0]
            splitted_name = set(no_extension.split("_"))

            if splitted_name in empty:
                os.remove(filename)

            empty.append(splitted_name)


print(" ")

if __name__ == "__main__":
    substitutor_double(ligands_list,positions_list)
    duplicate_removal()
