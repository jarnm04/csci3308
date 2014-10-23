#! /bin/bash
fileName=${1}

echo ''

if [[ "$#" -ne 1 ]];
then
	echo "Usage: Grades.sh filename"
else
	while read line
	do
		grade1=$(echo "$line" | cut -d' ' -f4)
		grade2=$(echo "$line" | cut -d' ' -f5)
		grade3=$(echo "$line" | cut -d' ' -f6)
		avgGrade=$((($grade1 + $grade2 +$grade3) / 3))
		echo $avgGrade [$(echo "$line" | cut -d' ' -f1)] $(echo "$line" | cut -d' ' -f3), $(echo "$line" | cut -d' ' -f2)
	done < $fileName | sort -t ' ' -k 3,3 -k 4,4 -k 2,2
fi

echo ''