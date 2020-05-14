import os, shutil
import numpy as np

os.chdir("Python/Subs_maker_Ligs_and_Pos/replacers_UPDATED/double_hetero")

f = open("double_replacer.in","r")
template = f.read()
f.close

ligands_list = ["uthiol",   # all ligands
                "trifluoromethyl",
                "tbutylthiol",
                "ammonia",
                "benzene",
                "bromide",
                "chloride",
                "cyanide",
                "fluoride",
                "water",
                "methanethiol",
                "CH4",
                "nitro",
                "nme3",
                "nme2",
                "nitroso",
                "adamantane",
                "COMe",
                "morph",
                "NEt2",
                "OEt",
                "OMe",
                "phCO",
                "tBu",
                "BnOH",
                "cyclohexane",
                "ethane",
                "phenol",
                "acetylene_L",
                "Smorph"]


positions_list = [14,7,9,19,29]

print("......Files generation.......")
print(" ")



def double_hetero(ligands, positions):
    pos=[]
    # Fixing the unfreezed positions first
    for i in positions_list:
        pos.append([x for x in positions if x != i])
    #return pos
    # Calculating the coeff:
    D = (len(ligands) - len(positions)) + 1

    for ligand in ligands:
        for i in range(len(positions)):
            for j in range(len(ligands)-D):
                if not os.path.exists("double_subs_structures"): os.mkdir("double_subs_structures")
                shutil.copy("double_replacer.in", str(ligand))
                os.chdir("double_subs_structures")
                m = 0
                while m < len(ligands):
                    if ligands[m] == ligand:
                        m = m + 1
                        continue
                    out = open("CCNAu_double_"+str(ligand)+"_"+str(positions[i])+"_"+str(pos[i][j])+"_"+str(ligands[m])+".in","w")
                    template_out = template.replace("ligand_1", ligand).replace(
                    "position_1", str(positions[i])).replace("position_2", str(pos[i][j])).replace(
                    "ligand_2", str(ligands[m])
                    ).replace("name_here", str("CCNAu_double_"+str(ligand)+"_"+str(positions[i])+"_"+str(pos[i][j])+"_"+str(ligands[m])))
                    m = m + 1
                    out.write(template_out)
                    out.close
                os.chdir("..")
                os.remove(str(ligand))
    return "Files generated"


if __name__ == "__main__":
    double_hetero(ligands_list,positions_list)
