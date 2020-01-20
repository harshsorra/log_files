import os
import re

line_regex = re.compile(r".*fwd=\"12.34.56.78\".*$")      # Regex used to match relevant loglines (in this case, a specific IP address)

output_filename = os.path.normpath(r"log_files\python-log-parse-example-master\parsed_lines.log")   # Output file, where the matched loglines will be copied to
with open(output_filename, "w") as out_file:       # Overwrites the file, ensure we're starting out with a blank file
    out_file.write("")

with open(output_filename, "a") as out_file:                # Open output file in 'append' mode
    with open(r"log_files\python-log-parse-example-master\test_log.log", "r") as in_file:       # Open input file in 'read' mode
        for line in in_file:                                   # Loop over each log line
            if (line_regex.search(line)):               # If log line matches our regex, print to console, and output file
                print(line)
                out_file.write(line)