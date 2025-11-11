import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="BusCompanyDB"
)

cursor = conn.cursor()

# Get date range from user
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Query: count bookings per day within the date range
query = """
SELECT 
    booking_date, 
    COUNT(*) AS total_bookings
FROM 
    booking
WHERE 
    booking_date BETWEEN %s AND %s
GROUP BY 
    booking_date
ORDER BY 
    booking_date
"""

cursor.execute(query, (start_date, end_date))

# Fetch results
results = cursor.fetchall()

print(f"\nTotal Online Bookings from {start_date} to {end_date}:")
for row in results:
    print(f"Date: {row[0]} - Number of Bookings: {row[1]}")

cursor.close()
conn.close()
