import streamlit as st
import plotly.express as px
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='PhonePe'
  
)

print(mydb)
mycursor = mydb.cursor(buffered=True)

#Reading csv files
df1=pd.read_csv(r"C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Aggregate_Transaction.csv")
df2=pd.read_csv(r"C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Aggregate_User.csv")
df3=pd.read_csv(r"C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Map_Transaction.csv")
df4=pd.read_csv(r"C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Map_User.csv")
df5=pd.read_csv(r"C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Top_Transaction.csv")
df6=pd.read_csv(r"C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Top_User.csv")

#converting csv into dataframe
ddf1=pd.DataFrame(df1)
ddf2=pd.DataFrame(df1)
ddf3=pd.DataFrame(df1)
ddf4=pd.DataFrame(df1)
ddf5=pd.DataFrame(df1)
ddf6=pd.DataFrame(df1)

#creating sql table 
def create_sql_table():
       
       #creating table for Aggregate_Transaction
       mycursor.execute("""CREATE TABLE IF NOT EXISTS aggregate_transaction
                         (State varchar(255), Year int, Quarter int, 
                        Transaction_Count bigint, Transaction_Amount bigint)""")
       
       #creating table for Aggregate_User
       mycursor.execute("""CREATE TABLE IF NOT EXISTS aggregate_user
                         (State varchar(255), Year int, Quarter int, 
                        Brand varchar(255), Brand_count bigint, Brand_Percentage float)""")
       
       #creating table for Map_Transaction
       mycursor.execute("""CREATE TABLE IF NOT EXISTS map_transaction
                         (State varchar(255), Year int, Quarter int,District varchar(255), 
                        Transaction_Count bigint, Transaction_Amount bigint)""")
       
       #creating table for Map_User
       mycursor.execute("""CREATE TABLE IF NOT EXISTS map_user
                         (State varchar(255), Year int, Quarter int, District varchar(255), 
                         Registered_User bigint, App_Opening bigint)""")
       
       #creating table for Top_Transaction
       mycursor.execute("""CREATE TABLE IF NOT EXISTS top_transaction
                         (State varchar(255), Year int, Quarter int, District varchar(255),
                        Transaction_Count bigint, Transaction_Amount bigint)""")
       
       ##creating table for Top_User
       mycursor.execute("""CREATE TABLE IF NOT EXISTS top_user
                         (State varchar(255), Year int, Quarter int, 
                          District varchar(255), Registered_User bigint)""")
       
create_sql_table()

#inserting value into the respective tables
class insert_values_into_sqlTable():
       
      def insert_aggregated_transaction():
          data=ddf1.values.tolist()  
          query="""INSERT INTO aggregate_transaction VALUES(%s, %s, %s, %s, %s)"""
          for row in data:                  
             mycursor.execute(query,tuple(row))
          mydb.commit()
      
      def insert_aggregate_user():
         data=ddf2.values.tolist()
         query="""INSERT INTO aggregate_user VALUES(%s, %s, %s, %s, %s,%s)"""
         for row in data:
            mycursor.execute(query,tuple(row))
         mydb.commit()

      def insert_map_transaction():
         data=ddf3.values.tolist()
         query="""INSERT INTO map_transaction VALUES(%s,%s,%s,%s,%s,%s)"""
         for row in data:
           mycursor.execute(query,row)
           mydb.commit()

      def insert_map_user():
         data=ddf4.values.tolist()
         query="""INSERT INTO map_user VALUES(%s,%s,%s,%s,%s,%s)"""
         for row in data:
           mycursor.execute(query,row)
           mydb.commit()

      def insert_top_transaction():
         data=ddf5.values.tolist()
         query="""INSERT INTO top_transaction VALUES(%s,%s,%s,%s,%s,%s)"""
         for row in data:
           mycursor.execute(query,row)
           mydb.commit()

      def insert_top_user():
         data=ddf6.values.tolist()
         query="""INSERT INTO top_user VALUES(%s,%s,%s,%s,%s)"""
         for row in data:
           mycursor.execute(query,row)
           mydb.commit()


insert_values_into_sqlTable.insert_aggregated_transaction()
insert_values_into_sqlTable.insert_aggregate_user()
insert_values_into_sqlTable.insert_map_transaction()
insert_values_into_sqlTable.insert_map_user()
insert_values_into_sqlTable.insert_top_transaction()
insert_values_into_sqlTable.insert_top_user()
