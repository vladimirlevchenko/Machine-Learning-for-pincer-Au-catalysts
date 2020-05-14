import fileinput
import os, shutil

print(os.getcwd())
os.chdir("Python/HPC_file_generator/from_xyz_to_com")
current_path = os.getcwd()
print(current_path)


# open a template input file for content reading
with open("DFT_input_template.com","r") as f:
    template = f.read()
f.close()

def DFT_input_generator():
    # Looping over .xyz files in the folder
    for filename in os.listdir(current_path):
        # and getting the name of the xyz files
        if filename.endswith(".xyz"):
            # names of the xyz files without the extension
            no_extension = os.path.splitext(filename)[0]

            # reading the xyz files and trimming of the first two lines
            with open(filename, "r") as xyz_file:
                template_fin2 = xyz_file.readlines()
            xyz_file.close()
            del template_fin2[:2]

            #creating a new file with the same name as given xyz file
            with open(no_extension + ".com", "w") as out:
                #and writing the contents of the input template to the new file with subs
                template_out = template.replace(
                "xyz_coordinates", ' '.join(template_fin2)).replace(
                "file_name",no_extension)
                out.write(template_out)
            out.close()
    os.mkdir("DFT_input_FROM_xyz")
    for filename in os.listdir(current_path):
        if filename.endswith(".com") and "template" not in filename:
            shutil.move(filename, "DFT_input_FROM_xyz")

    return "Successfully generated HPC input files"

if __name__ == "__main__":
    DFT_input_generator()
