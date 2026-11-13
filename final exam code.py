# Read the FASTA file

f = open("dna2.fasta")
seqs = {}

for line in f:
    line = line.rstrip()
    if line[0] == ">":
        words = line.split()
        name = words[0][1:]
        seqs[name] = ""
    else:
        seqs[name] = seqs[name] + line
f.close()


# QUESTION 1
# Number of records

print("Number of records:", len(seqs))

# QUESTION 2
# Lengths of sequences

print("Sequence lengths:")

for name, seq in seqs.items():

    print(name, len(seq))

# Find longest and shortest length

longest = 0
shortest = 100000000

for name, seq in seqs.items():
    if len(seq) > longest:
        longest = len(seq)
    if len(seq) < shortest:
        shortest = len(seq)

print("Longest sequence length:", longest)
print("Shortest sequence length:", shortest)


# Find all sequences with the longest length

print("Longest sequence(s):")

for name, seq in seqs.items():
    if len(seq) == longest:
        print(name)

# Find all sequences with the shortest length

print("Shortest sequence(s):")

for name, seq in seqs.items():

    if len(seq) == shortest:
        print(name)


# QUESTION 3
# Find ORFs


def find_orfs(seq, frame):

    orfs = []

    # Convert frame 1, 2, 3 into indexes 0, 1, 2

    start = frame-1

    # Move through the sequence three bases at a time

    for i in range(start,len(seq)-2,3):

        # Looks for the start codon

        if seq[i:i+3] == "ATG":

            # Once ATG is found, looks for a stop codon

            for j in range(i+3, len(seq)-2,3):

                codon = seq[j:j+3]

                if codon == "TAA" or codon == "TAG" or codon == "TGA":

                    # +1 because the exam wants positions starting from 1 not 0

                    length = j+3-i
                    position = i+1
                    orfs.append((length, position))
                    break
    return orfs


# Ask which reading frame to use

frame = int(input("Enter reading frame (1, 2 or 3): "))

# Find all ORFs in every sequence

print("ORFs:")
all_orfs = {}

for name, seq in seqs.items():
    orfs = find_orfs(seq, frame)
    all_orfs[name] = orfs
    print(name, orfs)


# Find the longest ORF in the entire file

longest_orf = 0
for name, orfs in all_orfs.items():
    for length, position in orfs:
        if length > longest_orf:
            longest_orf = length
            longest_orf_name = name
            longest_orf_position = position

if longest_orf > 0:
    print("\nLongest ORF:", longest_orf)
    print("Sequence:", longest_orf_name)
    print("Starting position:", longest_orf_position)
else:
    print("\nNo ORFs found.")

# QUESTION 4
# Find repeats

def find_repeats(seq, n):
    repeats = {}
    for i in range(len(seq)-n+1):
        repeat = seq[i:i+n]
        if repeat in repeats:
            repeats[repeat] = repeats[repeat] + 1
        else:
            repeats[repeat] = 1
    return repeats

# Ask for repeat length

n = int(input("Enter repeat length: "))

# Find repeats in the entire file

all_repeats = {}
for name, seq in seqs.items():
    repeats = find_repeats(seq, n)
    for repeat, number in repeats.items():
        if repeat in all_repeats:
            all_repeats[repeat] = all_repeats[repeat] + number
        else:
            all_repeats[repeat] = number

# Print repeats that occur more than once

print("Repeats occurring more than once:")
for repeat, number in all_repeats.items():
    if number > 1:
        print(repeat, number)

# Find most frequent repeat

most_frequent = ""
highest = 0

for repeat, number in all_repeats.items():
    if number > highest:
        highest = number
        most_frequent = repeat

print("Most frequent repeat:", most_frequent)
print("Number of occurrences:", highest)