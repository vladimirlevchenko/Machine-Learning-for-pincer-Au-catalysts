import os, shutil
import numpy as np

os.chdir("Python/Subs_maker_Ligs_and_Pos/replacers_UPDATED/triple")

f3 = open("triple_replacer.in","r")
template3 = f3.read()
f3.close


ligands_list = ["chloride",  # for tripple subst
                "benzene",
                "bromide",
                "cyanide",
                "fluoride",
                "methanethiol",
                "CH4",
                "nitro",
                "nitroso",
                "OEt",
                "OMe",
                "ethane",
                "BnOH"]


positions_list_triple = [7,9,19]

print("......Files generation.......")
print(" ")


def triple_subst(ligands, positions):
    for ligand in ligands:
        if not os.path.exists("triple_structures"): os.mkdir("triple_structures")
        shutil.copy("triple_replacer.in", str(ligand))
        os.chdir("triple_structures")
        out = open("CCNAu_triple_"+str(ligand)+"_"+ str(positions_list_triple[0])+"_"+ str(positions_list_triple[1])+"_"+ str(positions_list_triple[2])+".in","w")
        template_out = template3.replace("ligand_1",
        str(ligand)).replace("position_1",
        str(positions_list_triple[0])).replace("position_2",
        str(positions_list_triple[1])).replace("position_3",
        str(positions_list_triple[2])).replace("name_here",
        str("CCNAu_triple_"+str(ligand) +"_" + str(positions_list_triple[0])+"_" +str(positions_list_triple[1])+"_" + str(positions_list_triple[2])))
        out.write(template_out)
        out.close
        #go to the original dir
        os.chdir("..")
        os.remove(str(ligand))



if __name__ == "__main__":
    triple_subst(ligands_list,positions_list_triple)
