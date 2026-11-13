# Genomic Sequence Analyser

A Python-based tool for analysing DNA sequences stored in multi-record FASTA files.

## Overview

This project was developed as part of the Python for Genomic Data Science course offered by Johns Hopkins University.

The program processes DNA sequence data and performs basic genomic analyses, including sequence length calculations, open reading frame (ORF) identification and nucleotide repeat analysis.

The project demonstrates the application of Python programming to biological sequence analysis.

## Features

- FASTA parsing: Reads and processes multiple DNA sequences from a FASTA file.
- Sequence analysis: Calculates sequence lengths and identifies the longest and shortest sequences.
- ORF identification: Detects open reading frames using start and stop codons.
- Repeat analysis: Identifies recurring nucleotide subsequences of a specified length.
- Sequence comparison: Allows analysis of individual sequences within a multi-record FASTA file.

## Methodology

FASTA Parsing:

DNA sequences are extracted from FASTA files and stored in a Python dictionary, using sequence identifiers as keys.

ORF Identification:

The program searches for start codons (`ATG`) and in-frame stop codons (`TAA`, `TAG`, `TGA`) within a selected reading frame.

Repeat Analysis:

Nucleotide subsequences of a specified length are counted to identify frequently occurring patterns.

## Limitations

- ORF detection is limited to the reading frames implemented in the program.
- ORF identification uses simplified sequence-based criteria and does not confirm actual gene expression.
- The program is intended for educational genomic sequence analysis rather than clinical or diagnostic applications.
## How to Run

### Requirements
- Python 3
- No external libraries required

### Instructions

1. Download or clone this repository.
2. Ensure `dna2.fasta` is located in the same folder as `Genomic sequence analyser.py`.
3. Open a terminal in that folder.
4. Run the following command:

   ```bash
   python "Genomic sequence analyser.py"
   ```

5. When prompted, enter:
   - **Reading frame:** `1`, `2` or `3` to select the reading frame for ORF identification.
   - **Repeat length:** A positive integer (e.g. `3`) to specify the length of nucleotide sequences to analyse.

### Output

The program displays:

- Total number of FASTA records.
- Length of each DNA sequence.
- Longest and shortest sequences.
- Identified open reading frames (ORFs) and the longest ORF.
- Nucleotide repeats occurring more than once.
- Most frequently occurring nucleotide repeat and its frequency.

The results are printed directly to the terminal.
