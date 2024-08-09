import csv
from itertools import islice

new_rows = []
with open(r"C:\Users\Artur.Semikov\Documents\20240413_TargetPOS.txt", mode = "r") as f:
  csv_reader = csv.reader(f,delimiter="|")
  # first 10 rows
  for row in islice(csv_reader,5):
      if not row[0].startswith("Date"): row[0]="2024-04-23"
      print(row)
      new_rows.append(row)

print(new_rows)

with open(r"C:\Users\Artur.Semikov\Documents\20240424_TargetPOS.txt", mode = "w") as f:
  csv_writer = csv.writer(f,delimiter="|")
  csv_writer.writerows(new_rows)