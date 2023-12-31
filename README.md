## INTRODUCTION
This project aims to extract and process the data from PhonePe pulse github repositorywhich contains large amount 
of data related to various metrics and statistics, and to obtain insights and information that can be visualized 
in a user-friendly manner.

## INSTALLATION
To run this project, you need to install the following packages:
`````
pip install GitPython
pip install pandas
pip install mysql-connector-python
pip install streamlit
``````

##APPROACH
1. Data extraction: Clone the Github to fetch the data from the Phonepe pulse Github
repository and store it in CSV format.
2. Data transformation:transforming the data into a format suitable for analysis and visualization.
3. Database insertion: connect with MySQL database and insert the transformed data using SQL
commands.
4. Dashboard creation: Using Streamlit and Plotly libraries in Python to create
an interactive and visually appealing dashboard. Plotly's built-in geo map
functions is used to display the data on a map and Streamlit is used
to create a user-friendly interface with multiple dropdown options for users to
select different facts and figures to display.
