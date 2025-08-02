
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\Admin\Downloads\cricket_data.csv")
engine = create_engine("mysql+pymysql://root:password@localhost/IPL_Analysis")
df.to_sql(name='cricket_data', con=engine, if_exists='replace', index=False)

print("success")
