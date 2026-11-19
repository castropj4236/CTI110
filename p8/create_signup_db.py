# CTI 110
# DHW1 My Version
# Castro-Perez, J
# 11/19/26

import sqlite3

# Connect to SQLite database file (creates file if it doesn't exist)
conn = sqlite3.connect("signup_hw.db")
cursor = conn.cursor()

# Drop table so script can be re-run cleanly in class
cursor.execute("DROP TABLE IF EXISTS users")

# STUDENT CODE GOES IN THIS SECTION ONLY!!!
#--------------------------------------------------------------------------------------
# STEP 1: Create users table
# TO DO: Create a table called users with fields
# user_id, first_name, last_name, email, username, password_hash, signup_date, country, age
# I have started the table for you with the primary key 'user_id'
# NOTE: SQLite assigns user_id for you. You do not insert a value for it.
# NOTE: Do not put a comma after the LAST column in the table. A trailing comma is a syntax error.
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    username TEXT,
    password_hash TEXT,
    signup_date DATE,
    country TEXT,
    age INTEGER
)""")

# STEP 2: Insert sample fake users
# TO DO: Create a list called users that will store all 10 of your fake users information.
# I have started it for you
# Each user has 8 values, in this order (user_id is NOT included):
# first_name, last_name, email, username, password_hash, signup_date, country, age

users = [
    ('Oprah', 'Winfrey', 'oprah.winfrey@example.com', 'oprah', 'SuperSoul1', '2026-06-01', 'UNITED STATES', 72),
    ('Anderson', 'Cooper', 'anderson.cooper@example.com', 'anderson_cooper', 'AC360Live', '2026-06-02', 'UNITED STATES', 59),
    ('Stephen', 'Colbert', 'stephen.colbert@example.com', 'stephen_colbert', 'LateShow4', '2026-06-03', 'UNITED STATES', 62),
    ('Trevor', 'Noah', 'trevor.noah@example.com', 'trevor_noah', 'DailyShow5', '2026-06-04', 'SOUTH AFRICA', 42),
    ('Gayle', 'King', 'gayle.king@example.com', 'gayle_king', 'CBSMornings7', '2026-06-05', 'UNITED STATES', 71),
    ('Jimmy', 'Fallon', 'jimmy.fallon@example.com', 'jimmy_fallon', 'TonightShow8', '2026-06-06', 'UNITED STATES', 52),
    ('Robin', 'Roberts', 'robin.roberts@example.com', 'robin_roberts', 'GoodMorning9', '2026-06-07', 'UNITED STATES', 65),
    ('Conan', 'OBrien', 'conan.obrien@example.com', 'conan_obrien', 'LateNight10', '2026-06-08', 'UNITED STATES', 63),
    ('David', 'Letterman', 'david.letterman@example.com', 'david_letterman', 'TopTen11', '2026-06-09', 'UNITED STATES', 79),
    ('Ellen', 'DeGeneres', 'ellen.degeneres@example.com', 'ellen_degeneres', 'Kindness12', '2026-06-10', 'UNITED STATES', 68),
]


#------------------------------------------------------------------------------------
# DO NOT CODE PASS HERE!!!
# STEP 3: Run the python script! Once your done creating your table and adding in the user information
# You should run the program and it will create your database called signup_hw.db.
# You can then view it in your terminal and you can upload the .db file to a database viewer thats provided on Canvas.

cursor.executemany("""
INSERT INTO users (
    first_name, last_name, email, username, password_hash,
    signup_date, country, age
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", users)

conn.commit()
conn.close()

print("✅ signup_hw.db created with users table and sample data.")

print()

conn = sqlite3.connect("signup_hw.db")
cur = conn.cursor()
for row in cur.execute("SELECT * FROM users LIMIT 10"):
    print(row)
conn.close()