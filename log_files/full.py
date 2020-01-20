import csv
import os
def start_setup():
    loc_in=input(str("enter the location of the log file: "))
    loc_out=input(str("enter the location to save the csv file: "))
    out=input(str("enter the new filename: "))
    loc_out=loc_out+out
    with open(loc_in) as f,open(r'temp1.csv', 'w') as f_out:
        for line in f:
    #       line = line.strip().split()
            line=line.split()
            f_out.write(f'{line}\n')                #code converts the log files into csv files

    toAdd = ['date','time','web server','service point','unknown1','unknown2''data type','method','path','host','request id','IP','model','tc','ts','uptime','size']
    with open(r'temp1.csv', "r") as infile:
        reader = list(csv.reader(infile))
        reader.insert(0, toAdd)

    with open(r'temp2.csv', "w",newline='') as outfile:
        writer = csv.writer(outfile)
        for line in reader:
            writer.writerow(line)                   #code adds the attribute name for each column

    with open(r'temp2.csv', "r") as infile, open(loc_out, "w",newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        conversion = set('' "[']")
        for row in reader:
            newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]
            writer.writerow(newrow)                 #code removes unnecessary delimiters from the data

    os.remove(r'temp1.csv')
    os.remove(r'temp2.csv')
start_setup()