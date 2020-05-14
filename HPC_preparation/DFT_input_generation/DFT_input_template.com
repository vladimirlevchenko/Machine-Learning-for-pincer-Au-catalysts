%mem=16000MB
%chk=file_name.chk
#p pbepbe/def2SVP opt int=ultrafine
empiricaldispersion=gd3

file_name

1 1
xyz_coordinates
--Link1--
%mem=16000MB
%chk=file_name.chk
#p pbepbe/def2SVP pop=npa int=ultrafine
empiricaldispersion=gd3 scrf(smd,solvent=aceticacid) geom=check guess=read

file_name

1 1
