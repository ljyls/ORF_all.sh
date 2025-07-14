ORF_all.sh is a script integrated with Python scripts. This script sequentially truncates the N-terminal sequence preceding each methionine in the FPS, generates a series of redundant proteins termed ORF_shift proteins, removes protein sequences shorter than 20 amino acids, merges duplicate sequences, predicts endogenous secretory proteins using SignalP v5.0b, extracts the resulting hit sequence to obtain the OSPS, and merges the OSPS with the FPS to obtain the SPS.

Usage: Place the ​​subset FPS file​​ "filtered_transcript_all.table" in the same directory as ORF_all.sh for demonstration purposes, and run the following command in the Linux terminal: "bash ORF_all.sh". The final output file is OSPS named "filtered_ORF_signal.table" and FPS  named "Search_file.table"  in the OUT folder.

Note: 1. For the input FPS and the generated OSPS and SPS in this study, see Supplemental Data S4.
         2. Ensure that SeqKit and SignalP v5.0b are installed in your environment.
         3. In the OSPS and FPS, identical sequence titles, excluding the suffix _ORF followed by a number, indicate the same series of ORF_shift proteins.
