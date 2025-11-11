import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="BusCompanyDB"
)

cursor = conn.cursor()

# Query to get trip counts for each route
query = """
SELECT 
    route_id,
    COUNT(*) AS trip_count
FROM 
    trip
GROUP BY 
    route_id
ORDER BY 
    trip_count DESC
"""

cursor.execute(query)

# Fetch results
results = cursor.fetchall()

print("Route Trip Counts:")
for route_id, trip_count in results:
    print(f"Route {route_id}: {trip_count} trips")

cursor.close()
conn.close()
