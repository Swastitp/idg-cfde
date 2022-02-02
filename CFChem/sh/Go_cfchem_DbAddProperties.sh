#!/bin/bash
###
# Add molecular properties to all compounds in mols table.
###
#
T0=$(date +%s)
#
DBNAME="cfchemdb"
DBSCHEMA="public"
DBHOST="localhost"
#
TNAME="properties"
#
cwd=$(pwd)
TMPDIR="/tmp/$(basename $0 |sed 's/\..*$//')_$(date +'%Y-%m-%d')"
printf "TMPDIR: ${TMPDIR}\n"
if [ ! -e $TMPDIR ]; then
	mkdir $TMPDIR
fi
#
###
# SMILES from molecules table:
psql -d $DBNAME -c "COPY (SELECT cansmi, id FROM mols ORDER BY id) TO STDOUT WITH (FORMAT CSV,HEADER,DELIMITER E'\t')" \
	>${TMPDIR}/${DBNAME}_mols.smi
#
###
if [ ! "$CONDA_EXE" ]; then
	CONDA_EXE=$(which conda)
fi
if [ ! "$CONDA_EXE" -o ! -e "$CONDA_EXE" ]; then
	echo "ERROR: conda not found."
	exit
fi
#
propfile=${TMPDIR}/${DBNAME}_mols_lipinski_properties.smi
#
if [ ! -e "$propfile" ]; then
	source $(dirname $CONDA_EXE)/../bin/activate rdktools
	python3 -m rdktools.properties.App lipinski \
		--i ${TMPDIR}/${DBNAME}_mols.smi \
		--smilesColumn 0 --nameColumn 1 \
		--o ${propfile} \
		--iheader --oheader
	conda deactivate
	printf "Properties file generated: ${propfile}\n"
else
	printf "Properties file exists: ${propfile}\n"
fi
###
psql -d $DBNAME -c "DROP TABLE IF EXISTS $TNAME"
psql -d $DBNAME -c "CREATE TABLE $TNAME AS SELECT id FROM mols"
#
colnames=$(cat ${propfile} |head -1 |sed 's/\([a-z]\)\([A-Z]\)/\1_\2/g'|tr '[:upper:]' '[:lower:]')
printf "colnames: ${colnames}\n"
propnames=$(echo $colnames |sed 's/smiles\s//' |sed 's/name\s//')
N_props=$(echo $propnames |wc -w)
printf "propnames ($N_props): ${propnames}\n"
for propname in $propnames ; do
	psql -d $DBNAME -c "ALTER TABLE $TNAME ADD COLUMN $propname VARCHAR(32)"
done
#
N=$[$(cat ${propfile} |wc -l)-1]
i=0
while [ $i -lt $N ]; do
        i=$[$i + 1]
        line=$(cat ${propfile} |sed '1d' |sed "${i}q;d")
        mol_id=$(echo "$line" |awk -F '\t' '{print $2}')
	vals=$(echo $line |awk '{$1=$2=""; print $0}')
	vals=$(echo $vals |sed "s/\s/', '/g" |sed "s/^\(.*\)$/'\1'/")
        printf "${i}/${N}. mol_id=${mol_id} (${N_props} properties added)\n"
        psql -d $DBNAME -c "UPDATE $TNAME SET ($(echo $propnames |sed 's/\s/, /g')) = (${vals}) WHERE id = ${mol_id}"
done
#
#rm -rf $TMPDIR
#
printf "Elapsed time: %ds\n" "$[$(date +%s) - ${T0}]"
#