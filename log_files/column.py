import csv
toAdd = ['date','time','web server','service point','unknown1','unknown2','data type','method','path','host','request id','IP','model','tc','ts','uptime','size']
with open(r'log_files\csv_files\test14.csv', "r") as infile:
    reader = list(csv.reader(infile))
    reader.insert(0, toAdd)

with open(r'log_files\csv_files\test14c.csv', "w",newline='') as outfile:
    writer = csv.writer(outfile)
    for line in reader:
        writer.writerow(line)