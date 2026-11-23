import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

mutations = [
    "mmpR5 Glu49fs\n(Isolate 8)",
    "gyrA Ala90Val\n(Isolate 1)",
    "ald frameshift\n(Isolates 56)"
]

frequencies = [71, 10, 17]

plt.figure(figsize=(9, 5))
bars = plt.bar(mutations, frequencies)

plt.title("Reported Mutation Frequencies in the Tanzania TB Case")
plt.xlabel("Mutation")
plt.ylabel("Allele frequency (%)")
plt.ylim(0, 100)

for bar, value in zip(bars, frequencies):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 2,
        f"{value}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig("results/mutation_frequencies.png", dpi=300)

print("Graph saved successfully!")
