from Bio import SeqIO

# Read the Rv0678 reference DNA sequence
record = SeqIO.read("data/reference/Rv0678.fasta", "fasta")
dna = record.seq

# Translate the complete bacterial coding sequence
protein = dna.translate(table=11, cds=True)

# Display the results
print("Gene:", record.id)
print("DNA length:", len(dna), "bp")
print("Protein length:", len(protein), "amino acids")
print("First amino acid:", protein[0])
print("Last amino acid:", protein[-1])
print("Protein sequence:", protein)
