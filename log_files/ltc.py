import csv
with open(r'log_files\python-log-parse-example-master\parsed_lines.log') as f,open(r'log_files\csv_files\test1.csv', 'w') as f_out:
    for line in f:
 #       line = line.strip().split()
        line=line.split()
        f_out.write(f'{line}\n')