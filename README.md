# Rosalind Bioinformatics Stronghold

My Python solutions to problems from the [Rosalind](https://rosalind.info/problems/list-view/) "Bioinformatics Stronghold" track — a set of programming exercises that build up core computational biology skills: string processing on DNA/RNA/protein sequences, combinatorics, probability, and basic algorithms applied to biological data.

## What's in this repo

Each solved problem has two files:

- `problemNsolution.py` — the Python script that solves it
- `problemNdata.txt` — the sample input data used to test/run that script

Problems currently solved: 1–18 (see the file names for the full list).

## Topics covered so far

- Counting nucleotides in a DNA string
- Transcribing DNA to RNA, computing the reverse complement
- Computing GC content and finding the sequence with the highest GC%
- Building consensus sequences and profile matrices from multiple aligned strings
- Basic combinatorics/probability problems (e.g. counting mRNA strings from a protein, codon counting)
- FASTA-format parsing (reading multi-sequence files with `>` headers)

## How to run a solution

Each script is standalone. From this folder:

```bash
python problem1solution.py
```

**Note:** some scripts currently read their input file using a hardcoded absolute path (from when I was working locally) rather than a relative path. If you clone this repo and a script doesn't find its data file, open the script and update the file path in the `open(...)` call to point to the matching `problemNdata.txt` in this folder — that's on my to-do list to fix by switching to relative paths.

## About

I'm a biotech student learning bioinformatics and computational biology by working through Rosalind's problem sets. This repo is a running log of that practice — expect the code style to get cleaner and more efficient as I go (early solutions are more brute-force, later ones use more Pythonic/vectorized approaches).

## Setup

A `.venv` virtual environment is used locally for dependencies (see `.gitignore` — it isn't tracked in this repo). To set up your own environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# then install any dependencies your local scripts need, e.g.:
pip install requests
```
