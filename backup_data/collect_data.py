import sqlite3
import csv

# Function to export a table to a CSV file
def export_table_to_csv(connection, table_name, output_file):
    cursor = connection.cursor()
    
    # Fetch all rows from the table
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    
    # Get the column names
    column_names = [description[0] for description in cursor.description]
    
    # Write to CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)  # Write the header
        writer.writerows(rows)          # Write the data

# Main function
def main():
    # Connect to the SQLite database
    connection = sqlite3.connect('db.sqlite3')
    
    # Export data from 'sentences' table
    export_table_to_csv(connection, 'sentences', 'sentences.csv')
    
    # Export data from 'lists' table
    export_table_to_csv(connection, 'lists', 'lists.csv')
    
    # Close the database connection
    connection.close()
    
    print("Data exported successfully!")

# Run the main function
if __name__ == "__main__":
    main()