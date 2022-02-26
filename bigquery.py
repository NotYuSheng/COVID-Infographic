
import os
import pandas as pd
from google.cloud import bigquery
import pickle as pkl

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="phrasal-period-342504-9781882daff3.json"
client = bigquery.Client()         # Start the BigQuery Client
# Input your Query Syntax here; You may try it first at https://console.cloud.google.com/bigquery

QUERY = (
    'SELECT * FROM `bigquery-public-data.covid19_jhu_csse.summary` WHERE '
    'STARTS_WITH(country_region, \'Singapore\')')

query_job = client.query(QUERY)    # Start Query API Request
query_result = query_job.result()  # Get Query Result
df = query_result.to_dataframe()   # Save the Query Resultto Dataframe
df.to_pickle("dataset.pkl") 

output = pd.read_pickle("dataset.pkl")
# print(output)
with open("dataset.pkl", "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(object)

# Sort data
# sorting date with sort_value() function
#df = df[df['date'].dt.dayofweek == 1]


Final_result = df.sort_values('date')
print(Final_result) # For debugging

Final_result.to_excel('dataset.xlsx')

# ---------------------------------------------
# ---- Continue Data Analysis with your DF ----
# ---------------------------------------------
