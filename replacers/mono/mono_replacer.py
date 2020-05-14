import os, shutil

#################################################
#
# "CCNAu_OAc_mono_" should be substituted with a name of the scaffold
# that this script is run on. For example, if the scaffold is naphP_Ph,
# then it should be changed to "naph_Ph_OAc_mono_"
#
#################################################


# defining the pathway to the script file
os.chdir("/Users/vladimirlevchenko/DokumenterHD/programming/Python")
os.chdir("Subs_maker_Ligs_and_Pos/replacers_UPDATED/mono")
print(os.getcwd())

# open a replacement template
f = open("replacer_mono.in","r")
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

def substitutor_mono(ligands, positions):
    for i in ligands:
        for position in positions:
            #create dir with position as a name
            if not os.path.exists("mono_subs_input"): os.mkdir("mono_subs_input")
            #copy the file into the new dir
            shutil.copy("replacer_mono.in", str(position))
            os.chdir("mono_subs_input")

            #get the templ and replace the rep_position
            out = open("CCNAu_OAc_mono_"+str(position)+"_"+ str(i)+".in","w")
            template_out = template.replace("rep_position",
            str(position)).replace("name_here",
            str("CCNAu_OAc_mono_" + str(position)+"_"+str(i))).replace("ligand_name", i)

            out.write(template_out)
            out.close
            os.chdir("..")
            os.remove(str(position))


if __name__ == "__main__":
    substitutor_mono(ligands_list, positions_list)
