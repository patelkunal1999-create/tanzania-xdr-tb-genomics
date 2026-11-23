from Bio import SeqIO

record = SeqIO.read("data/reference/Rv0678.fasta", "fasta")
dna = record.seq

# Original protein sequence
original_protein = dna.translate(table=11, cds=True)

# Insert one nucleotide after DNA position 138
mutated_dna = dna[:138] + "A" + dna[138:]

# Translate the mutated sequence
mutated_protein = mutated_dna.translate(table=11)

print("Original protein:", original_protein)
print("Mutated protein:", mutated_protein)
print("Original length:", len(original_protein))
print("Mutated length:", len(mutated_protein))
