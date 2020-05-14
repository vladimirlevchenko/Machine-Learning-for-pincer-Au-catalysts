
import os, shutil
import random

os.chdir("Python/for_GitHub/randomizer")
current_path = os.getcwd()
print(current_path)

# number of randomly selected files
batch_size = 1000

random.seed(987)
# displays all files in the desired folder
files = os.listdir(current_path)
random.shuffle(files)
random_files_list = random.sample(files,k=batch_size)

if not os.path.exists("randomly_selected_files"): os.mkdir("randomly_selected_files")
with open("README_randomly_selected_files.txt","w") as f:
    f.write("Randomly selected files")
    f.write("\n")
    for element in range(len(random_files_list)):
        shutil.move(random_files_list[element], "randomly_selected_files")
        f.write(random_files_list[element])
        f.write("\n")
f.close()
