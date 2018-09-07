import csv
codon = {}
count = {}
with open('codon.tsv') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
      codon[row[0]] = row[1]
inputSequence = input("input codon sequence: ")
sequence = [inputSequence[i:i+3] for i in range(0, len(inputSequence), 3)]

for codonKey in sequence:
    key = codon[codonKey]
    if key in count:
        count[key] += 1
    else:
        count[key] = 1
print(count)