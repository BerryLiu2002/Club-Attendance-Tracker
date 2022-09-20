import csv
import os
from consts import *
from collections import defaultdict

files = os.listdir(csv_dir)

EMAIL_NAME = {}

def data_csv_path_gen():
    for file_name in files:
        abs_path = f"{csv_dir}\{file_name}"
        yield abs_path

def process_data_csvs():
    attendance = defaultdict(int)
    for path in data_csv_path_gen():
        with open(path, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter= ',', quotechar="\"")
            rows = [row for idx, row in enumerate(reader) if idx > 5]
            for row in rows:
                first_name, last_name, email = row[0], row[1], row[2]
                EMAIL_NAME[email] = first_name,last_name
                attendance[email] += 1
    return attendance
    
def write_to_attendance_csv():
    attendance = process_data_csvs()
    with open(attendance_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        for email, count in attendance.items():
            first, last = EMAIL_NAME[email]
            writer.writerow([first, last, email, count])

def clear_attendance_csv():
    with open(attendance_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["First Name", "Last Name", "Email", "Count"])

if __name__ == "__main__":
    clear_attendance_csv()
    write_to_attendance_csv()