import pyodbc

# Define the connection string
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DELLMM\MIKE_MSSQL;'
    r'DATABASE=weather_db;'
    r'UID=MIKE_MSSQL;'
    r'PWD=mikE2024M;'
    r'Trusted_Connection=yes;'
)

# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()
statemenet = """
INSERT INTO city (city_name, latitude, longitude) VALUES ('Sample', 51, 0);
"""
# Example query
cursor.execute(statemenet)


# cursor.execute("SELECT * FROM city;")
#
# # Fetch and print the result
# row = cursor.fetchone()
# print(row)

conn.commit()
# Close the connection
conn.close()