import os, shutil

os.chdir("Python/HPC_file_generator/DFT_and_batch_combined")
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

def batch_maker(batch_size):
    os.chdir("DFT_input_FROM_xyz")

    folder_count = 1
    file = 1
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".com"):
            print("BATCHED", filename)
            if not os.path.exists("Batch_" + str(folder_count)): os.mkdir("Batch_" + str(folder_count))
            if file == batch_size + 1:
                folder_count += 1
                os.mkdir("Batch_" + str(folder_count))
                shutil.move(filename, "Batch_" + str(folder_count))
                file = 2
            else:
                shutil.move(filename, "Batch_" + str(folder_count))
                file += 1

def SLM_copy():
    for batch in os.listdir(os.getcwd()):
        print(batch)

        os.chdir("..")
        shutil.copy("SLM_template.slm", "DFT_input_FROM_xyz/" + str(batch))
        os.chdir("DFT_input_FROM_xyz")

def SLM_creator():
    for batch in os.listdir(os.getcwd()):
        print(batch)
        os.chdir(str(batch))

        with open("SLM_template.slm","r") as f:
            template = f.read()

            template = template.replace("batch_number", str(batch))

        f.close()


        with open("generated_SLIM.slm", "a") as f2:
            f2.write(template)
            f2.write("\n" * 2)
            f2.write("cd $SUBMITDIR" + "\n")

            for filename in os.listdir(current_path):
                if filename.endswith(".com"):
                    no_extension = os.path.splitext(filename)[0]
                    f2.write("cp " + str(no_extension) + ".com $GAUSS_SCRDIR" + "\n")

            f2.write("cd $GAUSS_SCRDIR" + "\n")
            f2.write("\n" * 2)

            for filename in os.listdir(current_path):
                if filename.endswith(".com"):
                    no_extension = os.path.splitext(filename)[0]
                    f2.write("G09.prep.slurm " + str(no_extension) + "\n")
                    f2.write("time g09 < " + str(no_extension) + ".com > $SUBMITDIR/" + str(no_extension) + ".log \n")
            f2.write("\n" * 2)
            f2.write("cd $SUBMITDIR \nrm $GAUSS_SCRDIR/* \nrmdir $GAUSS_SCRDIR")
        f2.close()

        os.chdir("..")
        print("SLM file generated")


if __name__ == "__main__":
    DFT_input_generator()
    batch_maker(2)
    SLM_copy()
    SLM_creator()
