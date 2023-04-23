import sqlite3
import datetime

# Connect to the database
conn = sqlite3.connect('car_plate.db')
c = conn.cursor()

# Get the current time
now = datetime.datetime.now()
exit_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Fetch the in_time values where the exit_time is equal to the current time
c.execute("SELECT in_time FROM car_plate WHERE exit_time=?", (exit_time,))
results = c.fetchall()

# Print the fetched in_time values
for row in results:
    print(row[0])

# Close the database connection
conn.close()
