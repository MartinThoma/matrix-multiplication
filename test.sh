#!/bin/bash
# -i inputFile

usage()
{
cat << EOF
usage: $0 options

Run some tests with the the specified program

OPTIONS:
   -h      Show this message
   -i      Input file
   -n      Number of executions
   -p      Program call with flags
EOF
}

INPUTFILE=
PROGRAMCALL=
N=
while getopts "hi:p:n:" OPTION
do
     case $OPTION in
         h)  usage
             exit 1;;
         i)  INPUTFILE=$OPTARG;;
         p)  PROGRAMCALL=$OPTARG;;
         n)  N=$OPTARG;;
         ?)  usage
             exit;;
     esac
done

if [[ -z $INPUTFILE ]] || [[ -z $PROGRAMCALL ]] || [[ -z $N ]]
then
     usage
     exit 1
fi
TMP="$PROGRAMCALL -i $INPUTFILE > TMPcurrentFileResult.out"

echo "Executing: $TMP"

START=$(date +%s)
MIN=1000000
MAX=0
for (( i=1; i<=$N; i++ ))
do
	STARTE=$(date +%s)
	eval $TMP
	ENDE=$(date +%s)
	DIFFE=$(( $ENDE - $STARTE ))

	if [ $DIFFE -lt $MIN ]
	  then
		MIN=$DIFFE
	fi
	if [ $DIFFE -gt $MAX ]
	  then
		MAX=$DIFFE
	fi
	echo $i
done
END=$(date +%s)

DIFF=$(( $END - $START ))
echo "It took $DIFF seconds for $N executions"
echo "MIN: $MIN seconds"
echo "MAX: $MAX seconds"
