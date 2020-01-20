import csv

with open(r'log_files\csv_files\test14c.csv', "r") as infile, open(r'log_files\csv_files\test14b.csv', "w",newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    conversion = set('' "[']")
    for row in reader:
        newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)