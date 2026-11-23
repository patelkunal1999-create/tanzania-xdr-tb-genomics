from Bio import SeqIO

record = SeqIO.read("data/reference/Rv0678.fasta", "fasta")
dna = record.seq

for position in [47, 49]:
    start = (position - 1) * 3
    codon = dna[start:start + 3]
    amino_acid = codon.translate(table=11)

    print(f"\nProtein position: {position}")
    print(f"DNA positions: {start + 1}-{start + 3}")
    print(f"Codon: {codon}")
    print(f"Amino acid: {amino_acid}")
