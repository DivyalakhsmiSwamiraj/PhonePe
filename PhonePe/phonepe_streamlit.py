import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import mysql.connector
import plotly.express as px

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="" ,
  database="Phonepe" )
mycursor = mydb.cursor(buffered=True)

#-----------------------------------------------------------------

st.set_page_config(
    page_title="PhonePe Analysis |By Divyalakhsmi",
    page_icon='chart_with_upwards_trend',
    layout="wide",
    #initial_sidebar_state="expanded",
)
img=Image.open("phnPe img.jpeg")
st.image(img,width=500)
st.header("***Phonepe Pulse Data Visualization and Exploration***",divider='rainbow')

SELECT = option_menu(
    menu_title = None,
    options = ["About","Basic insights","Geo-visualization"],
    icons =["house","toggles"],
    #default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})

#-------------------------About-----------------------------#
if SELECT=="About":
     st.markdown("## :blue[Domain] : ***Fintech***")
     st.markdown("## :blue[Technologies used] : ***Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.***")
     st.markdown("## :blue[Overview] : ***Extracting PhonePe Pulse data by cloning phonepe github repository, transforming data and storing it into MySQL, visualizing the insights obtained from the data***")
        
#-----------------------Basic Insights------------------------#
if SELECT == "Basic insights":
        st.write("----")
        st.subheader("Let's know some basic insights about the data")
        options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 Districts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]
    
               
               
        select = st.selectbox("Select the option",options)
        if select=="Top 10 states based on year and amount of transaction":
            mycursor.execute("SELECT DISTINCT State, Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_transaction GROUP BY State, Year ORDER BY Total_Transaction_Amount DESC Limit 10");
        
            ddf6 = pd.DataFrame(mycursor.fetchall(), columns=['State','Year', 'Transaction_Amount'])
            col1,col2 = st.columns(2)
            with col1:
              st.write(ddf6)
            with col2:
               st.title("Top 10 states and amount of transaction")
               st.bar_chart(data=ddf6,y="State",x="Transaction_Amount")
        
        elif select=="List 10 states based on type and amount of transaction":
              mycursor.execute("SELECT DISTINCT State, SUM(Transaction_Count) as Total FROM top_transaction GROUP BY State ORDER BY Total ASC LIMIT 10");
              df = pd.DataFrame(mycursor.fetchall(),columns=['State','Total_Transaction'])
              col1,col2 = st.columns(2)
              with col1:
               st.write(df)
              with col2:
                st.title("List 10 states based on type and amount of transaction")
                st.bar_chart(data=df,x="Total_Transaction",y="State")
            
          
        elif select== "Top 10 Registered-users based on States and District":
          mycursor.execute("SELECT DISTINCT State, District, SUM(Registered_User) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10");
          df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','Registered_User'])
          col1,col2 = st.columns(2)
          with col1:
              st.write(df)
          with col2:
              st.title("Top 10 Registered-users based on States and District")
              st.bar_chart(data=df,y="State",x="Registered_User")
              
            
        elif select== "Top 10 Districts based on states and Count of transaction":
            mycursor.execute("SELECT DISTINCT State,District,SUM(Transaction_Count) AS Counts FROM map_transaction GROUP BY State,District ORDER BY Counts DESC LIMIT 10");
            df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','Transaction_Count'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 Districts based on states and Count of transaction")
                st.bar_chart(data=df,y="State",x="Transaction_Count")
            
            
        elif select== "List 10 Districts based on states and amount of transaction":
            mycursor.execute("SELECT DISTINCT State,Year,SUM(Transaction_Amount) AS Amount FROM aggregate_transaction GROUP BY State, Year ORDER BY Amount ASC LIMIT 10");
            df = pd.DataFrame(mycursor.fetchall(),columns=['State','Year','Transaction_Amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 Districts based on states and amount of transaction")
                st.bar_chart(data=df,y="State",x="Transaction_Amount")
            
            
        elif select== "List 10 Transaction_Count based on Districts and states":
            mycursor.execute("SELECT DISTINCT State, District, SUM(Transaction_Count) AS Counts FROM map_transaction GROUP BY State,District ORDER BY Counts ASC LIMIT 10");
            df = pd.DataFrame(mycursor.fetchall(),columns=['State','District','Transaction_Count'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("List 10 Transaction_Count based on Districts and states")
                st.bar_chart(data=df,y="State",x="Transaction_Count")
            
             
        elif select== "Top 10 RegisteredUsers based on states and District":
            mycursor.execute("SELECT DISTINCT State,District, SUM(Registered_User) AS Users FROM map_user GROUP BY State,District ORDER BY Users DESC LIMIT 10");
            df = pd.DataFrame(mycursor.fetchall(),columns = ['State','District','Registered_User'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 RegisteredUsers based on state and District")
                st.bar_chart(data=df,y="State",x="Registered_User")

#----------------------Geo-visualization--------------------------------#

mycursor = mydb.cursor()

# execute a SELECT statement
mycursor.execute("SELECT * FROM aggregate_transaction")

# fetch all rows
rows = mycursor.fetchall()

if SELECT == "Geo-visualization":
    st.subheader(':blue[Registered Users Hotspots - States]')

    Data_Aggregated_Transaction_df= pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Data_Aggregated_Transaction_Table.csv')
    Data_Aggregated_User_Summary_df= pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Data_Aggregated_User_Summary_Table.csv')
    Data_Aggregated_User_df= pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Data_Aggregated_User_Table.csv')
    Scatter_Geo_Dataset =  pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Data_Map_Districts_Longitude_Latitude.csv')
    Coropleth_Dataset =  pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Data_Map_IndiaStates_TU.csv')
    Data_Map_Transaction_df = pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Data_Map_Transaction_Table.csv')
    Data_Map_User_Table= pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Data_Map_User_Table.csv')
    Indian_States= pd.read_csv(r'C:\Users\divya\OneDrive\Desktop\vs python guvi\PROJECT\PhonePe\Longitude_Latitude_State_Table.csv')

    c1,c2=st.columns(2)
    with c1:
        Year = st.selectbox(
                'Please select the Year',
                ('2018', '2019', '2020','2021','2022'))
    with c2:
        Quarter = st.selectbox(
                'Please select the Quarter',
                ('1', '2', '3','4'))
    year=int(Year)
    quarter=int(Quarter)

    Transaction_scatter_districts=Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['Year'] == year ) & (Data_Map_Transaction_df['Quarter']==quarter) ].copy()
    Transaction_Coropleth_States=Transaction_scatter_districts[Transaction_scatter_districts["State"] == "india"]
    Transaction_scatter_districts.drop(Transaction_scatter_districts.index[(Transaction_scatter_districts["State"] == "india")],axis=0,inplace=True)
    # Dynamic Scattergeo Data Generation
    
    Transaction_scatter_districts = Transaction_scatter_districts.sort_values(by=['Place_Name'], ascending=False)
    Scatter_Geo_Dataset = Scatter_Geo_Dataset.sort_values(by=['District'], ascending=False) 
    Total_Amount=[]
    for i in Transaction_scatter_districts['Total_Amount']:
        Total_Amount.append(i)
    Scatter_Geo_Dataset['Total_Amount']=Total_Amount
    Total_Transaction=[]
    for i in Transaction_scatter_districts['Total_Transactions_count']:
        Total_Transaction.append(i)
    Scatter_Geo_Dataset['Total_Transactions']=Total_Transaction
    Scatter_Geo_Dataset['Year_Quarter']=str(year)+'-Q'+str(quarter)
    # Dynamic Coropleth
    
    Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['state'], ascending=False)
    Transaction_Coropleth_States = Transaction_Coropleth_States.sort_values(by=['Place_Name'], ascending=False)
    Total_Amount=[]
    for i in Transaction_Coropleth_States['Total_Amount']:
        Total_Amount.append(i)
    Coropleth_Dataset['Total_Amount']=Total_Amount
    Total_Transaction=[]
    for i in Transaction_Coropleth_States['Total_Transactions_count']:
        Total_Transaction.append(i)
    Coropleth_Dataset['Total_Transactions']=Total_Transaction 

    #scatter plotting the states codes 
    Indian_States = Indian_States.sort_values(by=['state'], ascending=False)
    Indian_States['Registered_Users']=Coropleth_Dataset['Registered_Users']
    Indian_States['Total_Amount']=Coropleth_Dataset['Total_Amount']
    Indian_States['Total_Transactions']=Coropleth_Dataset['Total_Transactions']
    Indian_States['Year_Quarter']=str(year)+'-Q'+str(quarter)
    fig=px.scatter_geo(Indian_States,
                        lon=Indian_States['Longitude'],
                        lat=Indian_States['Latitude'],                                
                        text = Indian_States['code'], #It will display district names on map
                        hover_name="state", 
                        hover_data=['Total_Amount',"Total_Transactions","Year_Quarter"],
                        )
    fig.update_traces(marker=dict(color="white" ,size=0.3))
    fig.update_geos(fitbounds="locations", visible=False,)
    # scatter plotting districts
    Scatter_Geo_Dataset['col']=Scatter_Geo_Dataset['Total_Transactions']
    fig1=px.scatter_geo(Scatter_Geo_Dataset,
                        lon=Scatter_Geo_Dataset['Longitude'],
                        lat=Scatter_Geo_Dataset['Latitude'],
                        color=Scatter_Geo_Dataset['col'],
                        size=Scatter_Geo_Dataset['Total_Transactions'],     
                    #text = Scatter_Geo_Dataset['District'], #It will display district names on map
                        hover_name="District", 
                        hover_data=["State", "Total_Amount","Total_Transactions","Year_Quarter"],
                        title='District',
                        size_max=22)
    
    fig1.update_traces(marker=dict(color="rebeccapurple" ,line_width=1))    #rebeccapurple
#coropleth mapping india
    fig_ch = px.choropleth(
                        Coropleth_Dataset,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',                
                        locations='state',
                        color="Total_Transactions",                                       
                        )
    fig_ch.update_geos(fitbounds="locations", visible=False,)
#combining districts states and coropleth
    fig_ch.add_trace( fig.data[0])
    fig_ch.add_trace(fig1.data[0])
    st.write("### **:blue[PhonePe India Map]**")
    colT1,colT2 = st.columns([6,4])
    with colT1:
        st.plotly_chart(fig_ch, use_container_width=True)
    with colT2:
        st.info(
        """
        Details of Map:
        - The darkness of the state color represents the total transactions
        - The Size of the Circles represents the total transactions dictrict wise
        - The bigger the Circle the higher the transactions
        - Hover data will show the details like Total transactions, Total amount
        """
        )
        st.info(
        """
        Important Observations:
        - User can observe Transactions of PhonePe in both statewide and Districtwide.
        - We can clearly see the states with highest transactions in the given year and quarter
        - We get basic idea about transactions district wide
        """
        )
# -----------------------------------------------FIGURE2 HIDDEN BARGRAPH------------------------------------------------------------------------
    # Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['Total_Transactions'])
    # fig = px.bar(Coropleth_Dataset, x='state', y='Total_Transactions',title=str(year)+" Quarter-"+str(quarter))
    # with st.expander("See Bar graph for the same data"):
    #     st.plotly_chart(fig, use_container_width=True)
    #     st.info('**:blue[The above bar graph showing the increasing order of PhonePe Transactions according to the states of India, Here we can observe the top states with highest Transaction by looking at graph]**')

    
    
