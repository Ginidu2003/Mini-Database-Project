import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="BusCompanyDB"
)

cursor = conn.cursor()

# User input
date_input = input("Enter the date (YYYY-MM-DD): ")

# Query: Sum revenue from booking table only
booking_query = """
    SELECT IFNULL(SUM(fare_amount), 0)
    FROM booking
    WHERE booking_date = %s
"""
cursor.execute(booking_query, (date_input,))
booking_revenue = cursor.fetchone()[0]

# Output
print(f"\nOnline Booking Revenue for {date_input}: Rs. {booking_revenue:.2f}")

cursor.close()
conn.close()
