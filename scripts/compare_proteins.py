from Bio import SeqIO

record = SeqIO.read("data/reference/Rv0678.fasta", "fasta")
dna = record.seq

original = dna.translate(table=11, cds=True)

mutated_dna = dna[:138] + "A" + dna[138:]

# Remove incomplete trailing bases
mutated_dna = mutated_dna[:len(mutated_dna) // 3 * 3]

mutated = mutated_dna.translate(table=11)

print("Original protein (first 60 aa):")
print(original[:60])

print("\nMutated protein (first 60 aa):")
print(mutated[:60])

print("\nFirst 46 amino acids unchanged:",
      original[:46] == mutated[:46])

print("Amino acid at position 47 - original:", original[46])
print("Amino acid at position 47 - mutated:", mutated[46])
