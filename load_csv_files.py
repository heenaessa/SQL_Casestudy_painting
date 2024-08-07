
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:admin@localhost/painting'
db = create_engine(conn_string)
conn = db.connect()

files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for file in files:
    df = pd.read_csv(f'/Users/heena/OneDrive/Documents/SQL/Scripts_SQL_Casestudy_Paintings/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)
