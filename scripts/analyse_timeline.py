import csv

file = "data/variants/tb_mutation_timeline.csv"

with open(file, "r") as f:
    reader = csv.DictReader(f)
    mutations = list(reader)

print("TOTAL MUTATION RECORDS:", len(mutations))

print("\nMUTATIONS BY GENE:")

for gene in sorted(set(row["Gene"] for row in mutations)):
    count = sum(row["Gene"] == gene for row in mutations)
    print(gene, ":", count)

print("\nMUTATION DETAILS:")

for row in mutations:
    print(
        row["Gene"],
        row["Mutation"],
        "First reported isolate:", row["First_reported_isolate"],
        "Frequency:", row["Reported_frequency"]
    )
