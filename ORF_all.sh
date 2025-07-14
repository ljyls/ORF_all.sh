
#!/bin/bash

mkdir ORF
cd ORF
mkdir OUT

#Sequentially cut off the N-terminal protein sequence in front of each Methionine, and output redundant ORF_shift protein sequences

mkdir temp
cd temp

../../app/ORF_all.py

mv ORF_all.table ../

cd ..

rm -rf temp

#Remove duplicates (separated by |) and discard sequences shorter than 20 amino acids

../app/Sequnce_filter.py  --file ORF_all.table --sep "|"

rm -rf ORF_all.table

seqkit tab2fx filtered_ORF_all.table > filtered_ORF_all.fasta

rm -rf ORF_all.table

echo "++++++++++++Predict for signal peptides++++++++++++"

mkdir SignalP
cd SignalP

signalp -org euk -fasta ../filtered_ORF_all.fasta -format short -gff3 -mature

#Building OSPS

seqkit seq ./filtered_ORF_all_mature.fasta -i -w 0 | seqkit fx2tab | awk -F '\t' '{print $1"\t"$2}' > ../filtered_ORF_signal.mature_seqence

awk -F '\t' '{print $1}' ../filtered_ORF_signal.mature_seqence > ../ORF_signal_mature.list

cd ..

seqkit grep -f ORF_signal_mature.list filtered_ORF_all.fasta > filtered_ORF_signal.fasta
rm -rf ORF_signal_mature.list

seqkit seq filtered_ORF_signal.fasta -i -w 0 | seqkit fx2tab | awk -F '\t' '{print $1"\t"$2}' > filtered_ORF_signal.table

#Building SPS

../app/Protein_database.py

#Sequence counts, output to OUT folder

for i in $(ls *.table); do
awk 'END{print NR}' $i > count_$i.txt
done

for i in $(ls count*); do
awk '{print FILENAME,"\t"$1}' $i >> sequence.summary
done

mv Search_file.table filtered_ORF_signal.table filtered_ORF_signal.mature_seqence filtered_ORF_all.table sequence.summary -t ./OUT/

rm -f ./*

cd ..

