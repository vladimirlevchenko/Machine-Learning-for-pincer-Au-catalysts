import fileinput
import os, shutil

print(os.getcwd())
os.chdir("Python/HPC_file_generator/HPC_submition/batch_generator")
current_path = os.getcwd()
print(current_path)

def batch_maker(batch_size):
    folder_count = 1
    file = 1
    for filename in os.listdir(current_path):
        if filename.endswith(".com"):
            if not os.path.exists("Batch_" + str(folder_count)): os.mkdir("Batch_" + str(folder_count))
            if file == batch_size + 1:
                folder_count += 1
                os.mkdir("Batch_" + str(folder_count))
                shutil.move(filename, "Batch_" + str(folder_count))
                file = 2
            else:
                shutil.move(filename, "Batch_" + str(folder_count))
                file += 1
batch_maker(4)
