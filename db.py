import sqlite3

# Connect to the database
conn = sqlite3.connect('car_plate.db')
c = conn.cursor()

# Select all entries in the database
c.execute("SELECT * FROM car_plate")
entries = c.fetchall()

# Print the entries
for entry in entries:
    print(entry)

# Close the connection
conn.close()

# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('car_plate.db')
# c = conn.cursor()

# # Execute the SQL statement to delete the table
# c.execute("DROP TABLE IF EXISTS car_plate")

# # Commit the changes and close the connection
# conn.commit()
# conn.close()