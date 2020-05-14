import os, shutil
import numpy as np

print(os.getcwd())
os.chdir("/Users/vladimirlevchenko/DokumenterHD/programming/Python")
print(os.getcwd())

os.chdir("for_GitHub/acetylenizer")
current_path = os.getcwd()
print(current_path)

f = open("replacer.in","r")
template = f.read()
f.close

CCN_chn = {'mono': 38, 'double': 37}
CCNAu = {'mono': 32, 'double': 31}
N_naph_py = {'mono': 37, 'double': 36}
N_naph_cyclic = {'mono': 39, 'double': 38}
naphN_Ph = {'mono': 28, 'double': 27} #should be 28 and 28
naphP_Ph = {'mono': 39, 'double': 38}
NHC_Ph = {'mono': 54, 'double': 53}
oxaz_Au = {'mono': 39, 'double': 38}
P_naph_cyclic = {'mono': 39, 'double': 38}
P_naph_py_Au = {'mono': 37, 'double': 36}
Ph_phtrAu = {'mono': 36, 'double': 35}
Tilset_Au = {'mono': 34, 'double': 33}
print(CCN_chn["mono"])

if not os.path.exists("acet_func_input"): os.mkdir("acet_func_input")
for file in os.listdir(current_path):
        if file.endswith(".xyz"):
            no_extension = os.path.splitext(file)[0]
            shutil.copy("replacer.in", "temp_file")
            os.chdir("acet_func_input")

            if "CCN_chn" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(CCN_chn["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "CCN_chn" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(CCN_chn["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "CCNAu" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(CCNAu["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "CCNAu" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(CCNAu["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "N_naph_py" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(N_naph_py["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "N_naph_py" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(N_naph_py["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "N_naph_cyclic" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(N_naph_cyclic["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "N_naph_cyclic" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(N_naph_cyclic["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "naphN_Ph" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(naphN_Ph["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "naphN_Ph" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(naphN_Ph["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "naphP_Ph" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(naphP_Ph["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "naphP_Ph" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(naphP_Ph["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "NHC_Ph" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(NHC_Ph["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "NHC_Ph" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(NHC_Ph["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "oxaz_Au" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(oxaz_Au["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "oxaz_Au" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(oxaz_Au["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "P_naph_cyclic" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(P_naph_cyclic["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "P_naph_cyclic" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(P_naph_cyclic["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "P_naph_py_Au" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(P_naph_py_Au["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "P_naph_py_Au" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(P_naph_py_Au["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "Ph_phtrAu" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(Ph_phtrAu["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "Ph_phtrAu" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(Ph_phtrAu["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            if "Tilset_Au" in no_extension and "mono" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(Tilset_Au["mono"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close
            if "Tilset_Au" in no_extension and "double" in no_extension:
                print(no_extension)
                new_name = str(no_extension) + "_" + "ins"
                out = open(new_name + ".in","w")
                template_out = template.replace("pos",str(Tilset_Au["double"])).replace(
                "name_here",(str(no_extension) + "_" + "ins")).replace(
                "CoreName", file)
                out.write(template_out)
                out.close

            os.chdir("..")
            os.remove("temp_file")
