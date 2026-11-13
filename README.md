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
