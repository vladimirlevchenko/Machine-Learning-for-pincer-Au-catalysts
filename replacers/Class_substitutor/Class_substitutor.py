import os, shutil
import numpy as np

os.chdir("Python/Subs_maker_Ligs_and_Pos/replacers_UPDATED/generalized_in_Class")

# opens a template for generation of mono subtituted complexes
f2 = open("mono_replacer.in","r")
template2 = f2.read()
f2.close

# opens a template for generation of double subtituted complexes
f = open("double_replacer.in","r")
template = f.read()
f.close

# opens a template for generation of three subtituted complexes
f3 = open("triple_replacer.in","r")
template3 = f3.read()
f3.close

# list of substituents to be intorduced
ligands_list = ["uthiol",
                "trifluoromethyl",
                "tbutylthiol",
                "ammonia",
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

# positions on the core to be substituted by the substituents
positions_list = [14,7,9,19,29]

print("......Files generation.......")
print(" ")


class Substitutor():
    """
    Class containing substitutions methods: mono-, di- and three-substitution.
    Generates mono-substituted .in files for molSimplify;
    Requires an input file named mono/double/three_replacer.in with a core written on which
    the substitution will take place.

    """
    def __init__(self,ligands,positions):
        self.ligands = ligands
        self.positions = positions
        self.pos = []

    def mono(self):
        """
        Requires a proper name of the core that is going to be in the name.
        Here it is a CCNAu_ core as an example.
        rep_position = a position where the substitution will take place
        name_here = name of the complex
        ligand_name = substituent that is going to be introduced into the core

        """
        for i in self.ligands:
            for position in self.positions:
                #create dir with position as a name
                if not os.path.exists("mono_subs_structures"): os.mkdir("mono_subs_structures")
                #copy the file into the new dir
                shutil.copy("mono_replacer.in", str(position))
                os.chdir("mono_subs_structures")
                #get the templ and replace the rep_position
                out = open("CCNAu_mono_"+str(position)+"_"+ str(i)+".in","w")
                template_out = template2.replace("rep_position",
                str(position)).replace("name_here",
                str("CCNAu_L_" + str(position)+"_"+str(i))).replace("ligand_name", i)
                out.write(template_out)
                out.close
                #go to the original dir
                os.chdir("..")
                os.remove(str(position))

    def double_hetero(self):
        # Fixing the unfreezed positions first
        for i in positions_list:
            self.pos.append([x for x in self.positions if x != i])
        #return self.pos
        # Calculating the coeff:
        self.D = (len(self.ligands) - len(self.positions)) + 1

        for ligand in self.ligands:
            for i in range(len(self.positions)): # 0 1 2 3
                for j in range(len(self.ligands)-self.D):
                    if not os.path.exists("double_subs_structures"): os.mkdir("double_subs_structures")
                    shutil.copy("double_replacer.in", str(ligand))
                    os.chdir("double_subs_structures")
                    m = 0
                    while m < len(self.ligands):
                        if self.ligands[m] == ligand:
                            m = m + 1
                            continue
                        out = open("CCNAu_double_"+str(ligand)+"_"+str(self.positions[i])+"_"+str(self.pos[i][j])+"_"+str(self.ligands[m])+".in","w")
                        template_out = template.replace("ligand_1", ligand).replace(
                        "position_1", str(self.positions[i])).replace("position_2", str(self.pos[i][j])).replace(
                        "ligand_2", str(self.ligands[m])
                        ).replace("name_here", str("CCNAu_double_"+str(ligand)+"_"+str(self.positions[i])+"_"+str(self.pos[i][j])+"_"+str(self.ligands[m])))
                        m = m + 1
                        out.write(template_out)
                        out.close
                    os.chdir("..")
                    os.remove(str(ligand))
        return "Files generated"

    def substitutor_homo(self):
        # First comes the unfreezed positions:
        for i in self.positions:
            self.pos.append([x for x in self.positions if x != i])
        # Now the file generation
        for ligand in self.ligands:
            for i in range(len(self.positions)): # 0 1 2 3
                for j in range(len(self.pos[i])): # before :    for j in range(len(ligands)):
                    if not os.path.exists("double_input"): os.mkdir("double_input")
                    shutil.copy("double_replacer.in", str(ligand))
                    os.chdir("double_input")

                    out = open("CCNAu_double_" + str(ligand)+"_"+str(self.positions[i])+"_"+str(self.pos[i][j])+"_"+str(ligand)+".in","w")
                    template_out = template.replace("ligand_1", ligand).replace(
                    "position_1", str(self.positions[i])).replace("position_2", str(self.pos[i][j])).replace(
                    "ligand_2", str(ligand)
                    ).replace("name_here", str("CCNAu_double_") + (str(ligand)+"_"+str(self.positions[i])+"_"+str(self.pos[i][j])+"_"+str(ligand)))

                    out.write(template_out)
                    out.close
                    os.chdir("..")
                os.remove(str(ligand))

    def duplicate_removal():
        os.chdir("/Users/vladimirlevchenko/DokumenterHD/programming/Python")
        new_path = os.chdir("CCNAu/double_subst/similar_subs/double_input")
        current_path = os.getcwd()

        empty = []
        for filename in os.listdir(current_path):
            if filename.endswith(".in"):
                no_extension = os.path.splitext(filename)[0]
                splitted_name = set(no_extension.split("_"))

                if splitted_name in empty:
                    os.remove(filename)

                empty.append(splitted_name)

    def triple(self):
        for ligand in self.ligands:
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
    a = Substitutor(ligands_list, positions_list)
    #print(a.mono())
    print(a.double_hetero())
    #print(a.double_homo())
    #print(a.duplicate_removal())
    #print(a.triple())
