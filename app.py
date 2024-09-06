import database as db
import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash import dash_table
from datetime import date,datetime
from dash.dependencies import Input,Output

# ********************GETTING DATA FROM SQLITE AND DATA PROCESSING*********************


#task 1 - query users table to retrieve users who joined within a specific date range
#syntax :- get_users_by_date_range('YYYY-MM-DD','YYYY-MM-DD')
users = db.show_users()
users['join_date'] = pd.to_datetime(users['join_date']).dt.strftime('%Y-%m-%d')
task1 = db.get_users_by_date_range('2023-01-01','2024-03-10')

##task 2 - query transactions table to calculate the total amount spent by each user
task2 = db.get_total_amount()

#task 3 - join users table and transactions table to generate a report showing user details along with total amount spent
task3 = db.total_amount_spent_by_each_user()
task3['total_amount'] = task3['total_amount'].replace(np.nan,0)
task3['avg_spent'] = task3['avg_spent'].replace(np.nan,0)


#task 4 - find top three users with max amount spent
task4 = task3.nlargest(3,['total_amount'])

#task 5 - calculate average transaction amount across all users (including those with 0 transaction)
#it's not very clear to me whether you want avg transaction for all users or avg transaction for each user
#I have therefore included a field avg_spent for each user in task 3.
task5_1 = task3['total_amount'].mean()
task5_2 = task3['total_amount'].loc[task3['total_amount'] != 0].mean()

#task 6 - identify users with no transactions
task6 = task3[task3['total_amount'] == 0].iloc[:,0:4]


#GRAPHS ________________________

fig1 = px.bar(task4, x="name", y="total_amount")

transactions = db.show_transactions()

fig2_1 = px.line(transactions, x="transaction_date", y="amount")
fig2_2 = px.scatter(transactions, x="transaction_date", y="amount")



# ************************************APP LAYOUT******************************************

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Python Dash Assignment", style={'text-align': 'center'}),

    html.H2("TABLES SECTION"),

    html.H3("Task 1"),
    html.P("Query users table to retrieve users who joined within a specific date range."),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        # min_date_allowed=date(2000,1,1),
        # max_date_allowed=date(2017, 9, 19),
        start_date=date(2020,1,1),
        initial_visible_month=date(2024, 1, 1),
        end_date=date(2025, 1, 1)
    ),
    html.Div(id="table-dynamic-data"),
    html.Br(),

    html.H3("Task 2"),
    html.P("Query transactions table to calculate the total amount spent by each user"),
    dash_table.DataTable(task2.to_dict('records'),[{"name": i, "id": i} for i in task2.columns], id='tbl2'),
    html.Br(),

    html.H3("Task 3"),
    html.P("Join users table and transactions table to generate a report showing user details along with total amount spent"),
    dash_table.DataTable(task3.to_dict('records'),[{"name": i, "id": i} for i in task3.columns], id='tbl3',sort_action='native',selected_columns=["name","total_amount"]),
    html.Br(),

    html.H3("Task 4"),
    html.P("Find top three users with max amount spent"),
    dash_table.DataTable(task4.to_dict('records'),[{"name": i, "id": i} for i in task4.columns], id='tbl4'),
    html.Br(),

    html.H3("Task 5"),
    html.P("Avg spent across all users"),
    dash_table.DataTable(task3.to_dict('records'),[{"name": i, "id": i} for i in task3.columns], id='tbl5'),
    html.P(f"Avg amount including users with 0 transactions:{task5_1}"),
    html.P(f"Avg amount excluding users with 0 transactions:{task5_2}"),
    html.Br(),

    html.H3("Task 6"),
    html.P("Identify users with no transactions"),
    dash_table.DataTable(task6.to_dict('records'),[{"name": i, "id": i} for i in task6.columns], id='tbl6'),
    html.Br(),

    html.H2("GRAPHS SECTION"),

    html.H3("Graph 1"),
    html.P("Create graph showing total amount spent by top three users"),

    dcc.Graph(figure=fig1),
    html.Br(),

    html.H3("Graph 2"),
    html.P("Line and scatter plot of transaction amount vs date"),

    dcc.Graph(figure=fig2_1),
    html.Br(),

    dcc.Graph(figure=fig2_2)
    
], style={'font-family': 'Verdana'})


@app.callback(
    Output('table-dynamic-data','children'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    start_date = datetime.strptime(start_date,'%Y-%m-%d').strftime('%Y-%m-%d')
    end_date = datetime.strptime(end_date,'%Y-%m-%d').strftime('%Y-%m-%d')
    temp_df = users[(users['join_date'] >= start_date) & (users['join_date'] <= end_date)]
    #create a table having users within start_date and end_date
    return dash_table.DataTable(temp_df.to_dict('records'),[{"name": i, "id": i} for i in temp_df.columns], id='tbl1'),



if __name__ == "__main__":
    app.run_server(debug=True)
