import sqlite3
import csv

# Function to insert data from a CSV file into a table
def insert_data_from_csv(connection, table_name, input_file):
    cursor = connection.cursor()
    
    with open(input_file, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the header
        next(csv_reader)
        
        # Insert each row into the database
        for row in csv_reader:
            cursor.execute(f'INSERT INTO {table_name} VALUES ({",".join("?" for _ in row)})', row)
    
    # Commit the changes
    connection.commit()

# Main function
def main():
    # Connect to the SQLite database
    connection = sqlite3.connect('db.sqlite3')
    
    # Insert data from CSV back into the table
    insert_data_from_csv(connection, 'sentences', 'backup_data/sentences.csv')
    insert_data_from_csv(connection, 'lists', 'backup_data/lists.csv')
    
    # Close the database connection
    connection.close()
    
    print("Data imported successfully!")

# Run the main function
if __name__ == "__main__":
    main()