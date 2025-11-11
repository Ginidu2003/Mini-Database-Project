import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="BusCompanyDB"
)

cursor = conn.cursor()

# Get the date input from the user
date_input = input("Enter booking date (YYYY-MM-DD): ")

# Query to get booking details for that specific date
query = """
SELECT 
    b.booking_id,
    p.passenger_id,
    p.name,
    p.contact,
    b.no_of_seats
FROM 
    booking b
JOIN 
    passenger p ON b.passenger_id = p.passenger_id
WHERE 
    b.booking_date = %s
ORDER BY 
    b.booking_id
"""

cursor.execute(query, (date_input,))

# Fetch results
results = cursor.fetchall()

# Display results nicely
print("\nBooking ID | Passenger ID | Passenger Name | Contact Number | No. of Seats")
print("-" * 75)
for row in results:
    print(f"{row[0]:<10} | {row[1]:<12} | {row[2]:<15} | {row[3]:<15} | {row[4]}")

cursor.close()
conn.close()
