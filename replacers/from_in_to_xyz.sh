#!/bin/sh

for file in *.in
do
	molsimplify -i "$file"
done

mkdir /Users/vladimirlevchenko/DokumenterHD/programming/Python/scaffolds/CCNAu/mono_subst/mono_subs_input/geometries_xyz  
cd /Users/vladimirlevchenko/Runs
find . -type f -name "*.xyz" -exec cp {} /Users/vladimirlevchenko/DokumenterHD/programming/Python/scaffolds/CCNAu/mono_subst/mono_subs_input/geometries_xyz \;
rm -r *

 

