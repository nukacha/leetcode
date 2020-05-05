n_col=$(head -n 1 file.txt | tr ' ' '\n' | wc -l | sed 's/ //g')
for i in $(seq 1 $n_col)
do cut -f $i -d ' ' file.txt | paste -d ' ' -s -;
done