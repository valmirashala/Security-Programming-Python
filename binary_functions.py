import sqlite3
import struct

def read_dbfile(file):
    # Connect to the database
    conn = sqlite3.connect(file)

    # Get a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to get the list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Get the list of tables

    tables = cursor.fetchall()

    # Loop through the list of tables
    for table in tables:
        table_name = table[0]
        print(f'Data from table {table_name}:')
        
        # Execute a SELECT statement to get the data from the table
        cursor.execute(f"SELECT * FROM {table_name};")
        
        # Get the data from the table
        data = cursor.fetchall()
        
        # Print the data
        for row in data:
            print(row)

    # Close the connection
    conn.close()

def read_datfiles(file):

    binary_file = open(file, 'rb')

    # read the binary data
    data = binary_file.read()

    # close the binary file
    binary_file.close()

    # unpack the binary data
    values = struct.unpack('iif', data)

    # print the data
    print(values)
