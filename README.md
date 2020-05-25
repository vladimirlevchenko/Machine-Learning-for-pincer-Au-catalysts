# Core Generation
To generate scaffolds that are going to be functionalized with substituents, we need to create a simple input file, *input_file.in:

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

In this example, the input file named CCNAu_OAc.in is going to be assembled. The complex will be constructed using two ligands – CCN_chn and acetate, both imported from the library. The name of the output complex matches the name of the file – CCNAu_OAc. 
This file is passed to molSimplify program to assemble the complex as xyz-file with the name specified in the command “name”. 
The resulting geometry looks like this:

![CCNAu_OAc_white](https://user-images.githubusercontent.com/12988626/82842381-9437d400-9ed9-11ea-8f30-2550738082fb.png)

The same procedure is repeated for other 11 scaffolds. As a result, 12 scaffolds are generated:

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

These scaffolds represent “naked” frameworks to which new substituents are going to be introduced. 

# Introduction of Substituents

Let us assume that we want to generate a mono substituted CCNAu_OAc complex with a benzene ring in position 7. To do that we would simply set up an input file for molSimplify - *CCNAu_OAc_mono_7_benzene.in*. The resulted file would then be executed by *molSimplify* together with its “naked” scaffold *CCNAu_OAc.xyz*. The logic behind this is that *molSimplify* uses the xyz-complex CCNAu_OAc as a core, substitutes its hydrogen atom in the position 7 with benzene and saves the output geometry as *CCNAu_OAc_mono_7_benzene.xyz* file, as demonstrated in Fig. X.  

Generation of thousands of such complexes with different ligands, positions and scaffolds would require automatization and thus development of an algorithm that does the job for us. 
First define a ligand set. 
Two types of substituents (ligands) we are going to work with – deactivating and activating. In total, there is 10 defined substituents that are going to be introduced.

Before we move on, it is required to add the desired ligands to the molSimplify’s database. 
Naming – Core name + mono/double/triple + position + substituent + ins (if inserted).

## Mono Substitution

text here

## Double Substitution

text here

## Triple Substitution

text here

# Randomization of Complexes

text here

# Preparation to HPC subsmission

text here

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
