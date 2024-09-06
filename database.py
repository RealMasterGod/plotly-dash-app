import sqlite3
import pandas as pd


def show_users():
    #create a database connection
    conn = sqlite3.connect('example.db')

    #query to get all users from users table
    sql_query = pd.read_sql_query("SELECT * FROM users",conn)

    #create a DataFrame
    df = pd.DataFrame(sql_query, columns=["user_id","name", "email", "join_date"])

    #commit out command
    conn.commit()

    #close the connection
    conn.close()

    #return DataFrame
    return df

def show_transactions():
    #create a database connection
    conn = sqlite3.connect('example.db')

    #query to get all transactions from transactions table
    sql_query = pd.read_sql_query("SELECT * FROM transactions",conn)

    #create a DataFrame
    df = pd.DataFrame(sql_query, columns=["transaction_id","user_id", "amount", "transaction_date"])

    #commit out command
    conn.commit()

    #close the connection
    conn.close()

    #return DataFrame
    return df

def get_users_by_date_range(start,end):
     #create a database connection
    conn = sqlite3.connect('example.db')

    #query to get all users by join date range
    sql_query = pd.read_sql_query(f"SELECT * FROM users WHERE join_date BETWEEN '{start}' AND '{end}'",conn)

    #create a DataFrame
    df = pd.DataFrame(sql_query, columns=["user_id","name", "email", "join_date"])

    #commit out command
    conn.commit()

    #close the connection
    conn.close()

    #return DataFrame
    return df

def get_total_amount():
     #create a database connection
    conn = sqlite3.connect('example.db')

    #query to get total amount spent
    sql_query = pd.read_sql_query(f"SELECT user_id,SUM(amount) as total_spent from transactions GROUP BY user_id",conn)

    #create a DataFrame
    df = pd.DataFrame(sql_query, columns=["user_id","total_spent"])

    #commit out command
    conn.commit()

    #close the connection
    conn.close()

    #return DataFrame
    return df

def total_amount_spent_by_each_user():
     #create a database connection
    conn = sqlite3.connect('example.db')

    #query to get total amount spent by each user
    sql_query = pd.read_sql_query(f"SELECT u.user_id,u.name,u.email,u.join_date,SUM(t.amount) as total_amount,ROUND(AVG(t.amount),2) as avg_spent from users u LEFT JOIN transactions t ON u.user_id = t.user_id GROUP BY u.user_id ",conn)

    #create a DataFrame
    df = pd.DataFrame(sql_query, columns=["user_id","name", "email", "join_date","total_amount","avg_spent"])

    #commit out command
    conn.commit()

    #close the connection
    conn.close()

    #return DataFrame
    return df


# c.execute("SELECT * from users")

# print(c.fetchall())

# c.execute("SELECT * from transactions")

# print(c.fetchall())

# c.execute("DELETE FROM users")
# c.execute("DELETE FROM transactions")
# c.execute("SELECT * from transactions")
# c.execute("DROP TABLE users")
# c.execute("DROP TABLE transactions")

# print(c.fetchall())
