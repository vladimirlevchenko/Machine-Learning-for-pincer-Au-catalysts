# Core Generation
To generate scaffolds that are going to be functionalized with substituents, we need to create a simple input file, *input_file.in*:

```markdown
-core au
-geometry oct
-coord 4
-lig CCN,acetate
-ligocc 1 1
-ff MMFF94
-ffoption BA
-spin 1
-oxstate III
-keepHs yes
-name CCNAu_OAc
```

In this example, the input file named *CCNAu_OAc.in* is going to be assembled. The complex will be constructed using two ligands – CCN and acetate, both imported from the library. The name of the output complex matches the name of the file – CCNAu_OAc. 
This file is passed to molSimplify program to assemble the complex as xyz-file with the name specified in the command “name”. 
The resulting geometry looks like this:

![CCNAu_OAc_white](https://user-images.githubusercontent.com/12988626/82842381-9437d400-9ed9-11ea-8f30-2550738082fb.png)

The same procedure is repeated for other 11 scaffolds. As a result, 12 scaffolds are generated:

<img width="561" alt="Scaffolds" src="https://user-images.githubusercontent.com/12988626/82888192-51ade000-9f49-11ea-820f-37355da6d1c4.png">

*CCN_chn_Au_OAc.xyz*

*CCNAu_OAc.xyz*

*N_naph_cyclic_OAc.xyz*

*N_naph_py_Au_OAc.xyz*

*naphN_Ph_OAc.xyz*

*naphP_Ph_OAc.xyz*

*NHC_Ph_OAc.xyz*

*oxaz_Au_OAc.xyz*

*P_naph_cyclic_OAc.xyz*

*P_naph_py_Au_OAc.xyz*

*Ph_phtrAu_OAc.xyz*

*Tilset_Au_OAc.xyz*

These scaffolds represent “naked” frameworks to which the substituents are going to be introduced. 

# Introduction of Substituents

Let us assume that we want to generate a mono substituted CCNAu_OAc complex with a benzene ring in position 7. To do that we would simply set up an input file for *molSimplify* - *CCNAu_OAc_mono_7_benzene.in*. The resulted file would then be executed by *molSimplify* together with its “naked” scaffold *CCNAu_OAc.xyz*. The logic behind this is that *molSimplify* uses the xyz-complex CCNAu_OAc as a core, substitutes its hydrogen atom in the position 7 with benzene and saves the output geometry as *CCNAu_OAc_mono_7_benzene.xyz* file, as demonstrated in Fig. X.  

```markdown
-coord 6
-replig 1
-core CCNAu_OAc.xyz
-ligocc 1
-ccatoms 7
-lig benzene
-geometry oct
-spin 1
-oxstate III
-ff MMFF94
-ffoption Before
-name CCNAu_OAc_mono_7_benzene
-keepHs no
```

Generation of thousands of such complexes with different ligands, positions and scaffolds would require automatization and thus development of an algorithm that does the job for us. 
First define a ligand set. 
Two types of substituents (ligands) we are going to work with – deactivating and activating. In total, there is 10 defined substituents that are going to be introduced.

<img width="794" alt="all_scaffolds_with_ligands" src="https://user-images.githubusercontent.com/12988626/82891189-9dfb1f00-9f4d-11ea-9389-9586afe360b5.png">

**General strategy:** generation of the input files for *molSimplify* (.in files) -> generation of the geometries (.xyz) from the input files. 
Before we move on, it is required to add the desired ligands to the molSimplify’s database. 
Naming – Core name + mono/double/triple + position + substituent + ins (if inserted).

## Mono Substitution

**Required files:** *mono_replacer.py*, replacing template (*replacer_mono.in*) and scaffold’s core xyz file (*CCNAu_OAc.xyz*).

```markdown
-coord 6
-replig 1
-core CCNAu_OAc.xyz
-ligocc 1
-ccatoms **rep_position**
-lig **ligand_name**
-geometry oct
-spin 1
-oxstate III
-ff MMFF94
-ffoption Before
-name **name_here**
-keepHs no
```

The structure of the *replacer_mono.in* is presented in a snippet above. The name of the core, CCNAu_OAc.xyz, needs to be added manually, depending on the scaffold that is going to be used for substituition. For example, if naphN_Ph_OAc is used for generation of substituted complexes, then its core should be specified as “naphN_Ph_OAc.xyz”. **rep_position** is a label of a hydrogen atom that is going to be replaced with a substituent (**ligand_name**). The complex is going to be saved as **name_here**, which is constructed when the python script *mono_replacer.py* is executed.

The structure of *mono_replacer.py* is presented below. The positions for substituents (**positions_lis**) are unique for each complex and have to be updated manually, each time the script is executed for a new scaffold. In this example, 11 positions in the scaffold CCNAu_OAc are going to be substituted with ligands, specified is **ligand_list**.  

```ruby
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

```

Execution of the script *mono_replacer.py* results in a folder “mono_subs_input” with 111 (10 substituents x 11 positions) generated input files for *molSimplify*. To the generated folder with input files (mono_subs_input), we have to copy *CCNAu_OAc.xyz* and a bash script *from_in_to_xyz.sh* and execute the latter. The bash script will generate the geometry of the complexes located in the folder mono_subs_input into a new folder inside it, called “geometries_xyz”.
Generation of 100 complexes takes ca 10 min.  

```markdown
|---CCNAu
	|---mono_subst
		  --- mono_replacer.py (1st)
		  --- replacer_mono.in
		 |--- mono_subs_input
			  --- CCNAu_OAc.xyz (has to be copied here manually)
			  --- from_in_to_xyz.sh (2nd; has to be copied here manually)
			  --- CCNAu_OAc_mono_7_benzene.in
			  	 .
			  	 .
			  	 .
			  --- CCNAu_OAc_mono_30_tBu.in
		 	 |--- geometries_xyz
				    --- CCNAu_OAc_mono_7_benzene.xyz
					    .
					    .
					    .
				    --- CCNAu_OAc_mono_30_tBu.xyz
```

## Double Substitution

Introduction of two substituents to the scaffold can be achieved in two ways: homo- and heterosubstitution. In homosubstitution, both substituents are the same, for example two Cl or two iPr groups. In contrast to heterosubstitution, where two substituents can be different – F and Ph or Et and OH etc. The algorithms for both ways of substitution are slightly different and can be found in *hetero_double_replacer.py* and *homo_double_replacer.py*. In this project, we are going to use homosubstitution.

The input file for the substitution in a single scaffold results in double substituted CCNAu_OAc complex with two Br atoms in positions 30 and 28 (snippet below to the left). This input file can be generalized for the whole scaffold with positions, substituents and name as variables. By varying them, we can introduce as many substituents as we want in the desired positions and in the specified scaffold (snippet to the right):  

```markdown
-coord 6							-coord 6
-replig 1							-replig 1
-core CCNAu_OAc.xyz						-core **CCNAu_OAc.xyz**
-ligocc 1 1							-ligocc 1 1
-ccatoms 30,28							-ccatoms **position_1,position_2**
-lig bromide bromide						-lig **ligand_1 ligand_2**
-geometry oct							-geometry oct
-spin 1								-spin 1
-oxstate III							-oxstate III
-keepHs no no							-keepHs no no
-ff MMFF94							-ff MMFF94
-ffoption Before						-ffoption Before
-name CCNAu_OAc_double_bromide_bromide				-name **name_here**
```

Execution of the script *homo_double_replacer.py* creates a folder with 550 .in files, which are going to be used as input files for the geometry generation. The geometries are then generated executing *from_in_to_xyz.sh* bash script (remember the presence of the core structure, CCNAu_OAc.xyz in the running folder).  
The assembled geometries have specific names, which determine their composition, for example:
CCNAu_double_benzene_7_29_benzene.xyz – means the the core CCNAu_OAc is double substituted with benzene in position 7 and another benzene in position 29.

![CCNAu_OAc_double_benzene_7_29_benzene](https://user-images.githubusercontent.com/12988626/82897796-7bbace80-9f58-11ea-8d6d-02c3e10e1a7d.png)

## Triple Substitution

Introduction of three substituents can be achieved by executing *triple_replacer.py*. One has to manually edit the postions that are going to be substituted. 

# Randomization of Complexes

In total it was produced **5180** complexes (*xyz* geometry files), arising from combination of 12 scaffolds, with mono- and double-substitution (homosubstitution) and 10 substituents. To proceed further with exploration of the complexes with machine learning, we have to **randomly** select 1000 complexes, which is achieved by executing *randomizer.py*. The script chooses random 1000 files and moves them into a new folder. The script also creates a text file with the names of the files that were randomly moved.

```ruby

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

```

The script has to be executed in the folder with all complexes (with 5180 *xyz* geometry files).

# Preparation to HPC subsmission

The next step is to assemble input files to send for DFT calculations to high-performance supercomputer (HPC). Each complex requires its own input file with specifications of the calculations. 

## For a single complex

**General strategy:** take template for DFT calculations -> insert the coordinates from xyz file; keep the same name of the complex -> create SLM file (to submit to HPC) -> submit to HPC (.com and .slm files) 

Attached picture below. Right - the input file for DFT calcualtions for complex named NHC_Ph_OAc_double_HSO2Me_13_18_HSO2Me. Generalized template of the input file to submit to the DFT calculations.

<img width="1174" alt="hpc_picture" src="https://user-images.githubusercontent.com/12988626/82899591-8c207880-9f5b-11ea-9d5e-441b0c6234de.png">

Each xyz file contains the geometry of the complex, which is then copied into the DFT_input_template.com file (field to substitute – “file name”). This DFT input file contains two sections: geometry optimization and single point calculations (followed after “—Link1—” command). Also, the file contains computation details, such as basis set (def2SVP), grid dimention and method (pbepbe). The complex’s geometry is first optimizaed in a gas phase and the optimized energy is then taken into the single point calculations, which are performed in acetic acid (HOAc). 

## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/vladimirlevchenko/Machine-Learning-for-pincer-Au-catalysts/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Core generation
To generate scaffolds that are going to be functionalized with substituents, we need to create a simple input file, input_file.in:
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/vladimirlevchenko/Machine-Learning-for-pincer-Au-catalysts/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
