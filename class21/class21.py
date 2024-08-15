import csv

# Writing data to a CSV file
def write_to_csv(file_path, data):
    # Open the file in write mode
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the header
        writer.writerow(['Name', 'Age', 'City'])
        # Writing the data rows
        writer.writerows(data)

# Reading data from a CSV file
def read_from_csv(file_path):
    # Open the file in read mode
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        # Skipping the header
        next(reader)
        # Reading and printing the data rows
        for row in reader:
            print(f'Name: {row[0]}, Age: {row[1]}, City: {row[2]}')

# Sample data
data = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# File path
file_path = 'class21\sample.csv'

# # Writing to the CSV file
# write_to_csv(file_path, data)

# Reading from the CSV file
read_from_csv(file_path)
