import os, shutil
import random, csv, fnmatch

os.chdir("Python/for_GitHub/data_analysis")
current_path = os.getcwd()
print(current_path)



def csv_generator():
    with open("RESULT_" + str(folder) + ".csv", "w") as f:
        f.write("*\n")
        failed_calc = 0
        for filename in os.listdir(current_path + "/" + str(folder)):
            if filename.endswith(".log"):
                no_extension = os.path.splitext(filename)[0]
                f.write(no_extension + ",")
                with open(filename) as f_2:
                    energies = []
                    n = 0
                    e = False
                    line_reader = f_2.readlines()
                    for line in line_reader:
                        if "Normal" in line:
                            n = n + 1
                            f.write("Normal")
                            f.write(",")
                        if "Done:" in line:
                            e = True
                            energies.append(line.split()[4])
                            new_l = energies
                if n == 0:
                    failed_calc = failed_calc + 1
                    f.write("FAILED,")
                if e is True:
                    f.write(new_l.pop())
                    f.write("\n")
                    f_2.close()
                else:
                    f.write("NONE")
                    f.write("\n")
                    f_2.close()
        f.write("\n")
        f.write("*\n")
        f.write("Total calculations," + str(len(fnmatch.filter(os.listdir(current_path + "/" + str(folder)), "*.log"))))
        f.write("\n")
        f.write("Failed calculations," + str(failed_calc))
    f.close()


if __name__ == "__main__":
    for folder in os.listdir(current_path):
        if "batch" in folder:
            os.chdir(folder)
            csv_generator()
            os.chdir("..")
            print(folder + "  -> " + "DONE")
