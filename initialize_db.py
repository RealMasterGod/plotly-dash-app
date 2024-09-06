import sqlite3

#create a database connection
conn = sqlite3.connect('example.db')

#create a cursor
c = conn.cursor()

#create users table
c.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id integer PRIMARY KEY NOT NULL,
    name text NOT NULL,
    email text NOT NULL UNIQUE,
    join_date text
)
""")

print("users table created...")

#create transactions table
c.execute("""CREATE TABLE IF NOT EXISTS transactions (
    transaction_id integer PRIMARY KEY NOT NULL,
    user_id int NOT NULL,
    amount real NOT NULL,
    transaction_date text,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
""")

print("transactions table created...")


#user data
users = [
    ('John', 'john@testmail.com', '2024-01-01'),
    ('Mary', 'mary@testmail.com', '2024-01-15'),
    ('James', 'james@testmail.com', '2024-02-07'),
    ('Smith', 'smith@testmail.com', '2024-02-27'),
    ('Bob', 'bob@testmail.com', '2023-03-13'),
    ('Anita', 'anita@testmail.com', '2024-03-15'),
    ('Lily', 'lily@testmail.com', '2024-03-15'),
    ('Stuart', 'stuart@testmail.com', '2024-03-31'),
    ('Brian','brian@testmail.com','2023-05-17'),
    ('Martha', 'martha@testmail.com', '2024-05-23'),
]

#transaction data
transactions = [
    (1, 500.00, '2024-02-10'),
    (2, 200.00, '2024-03-17'),
    (2, 100.00, '2024-04-01'),
    (3, 400.00, '2024-02-27'),
    (1, 100.00, '2024-03-01'),
    (5, 350.00, '2024-05-06'),
    (4, 425.00, '2024-04-21'),
    (7, 175.00, '2024-05-06'),
    (7, 200.00, '2024-05-17'),
    (7, 100.00, '2024-06-15'),
]

#insert user data into users table
c.executemany("INSERT INTO users (name,email,join_date) VALUES (?,?,?)", users)

print('users table initialized...')

#insert transaction data into transactions table
c.executemany("INSERT INTO transactions (user_id,amount,transaction_date) VALUES (?,?,?)", transactions)

print('transactions table initialized...')

#commit out command
conn.commit()

#close the connection
conn.close()