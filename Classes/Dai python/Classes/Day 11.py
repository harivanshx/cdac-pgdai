import mysql.connector

# Step 1 – Connect to the database
try:
    connection = mysql.connector.connect(
        host="localhost",       # or your host, e.g., "127.0.0.1"
        user="root",   # MySQL username

        password="Cdac123#", # MySQL password
        database="testdb"  # The database you want to connect to
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    # Step 2 – Create a cursor object
    cursor = connection.cursor()

    # Step 3 – Define and execute the query
    query = "SELECT * "  # Replace 'your_table' with your actual table name
    cursor.execute(query)

    # Step 4 – Fetch all rows from the result
    rows = cursor.fetchall()

    # Step 5 – Print the fetched records
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Step 6 – Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
