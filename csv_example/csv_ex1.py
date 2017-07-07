#!/usr/bin/env python
"""Read a CSV file. Use the first line as a header line. Return a dictionary."""
import csv

def main():
    """Read a CSV file. Use the first line as a header line. Return a dictionary."""
    file_name = 'test_net_devices.csv'
    with open(file_name) as f:
        read_csv = csv.DictReader(f)
        for entry in read_csv:
            print entry

if __name__ == "__main__":
    main()
