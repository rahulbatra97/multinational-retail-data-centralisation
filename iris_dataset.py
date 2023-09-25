from sqlalchemy import create_engine

# Database connection details
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = "database-1.coddpaqo7juo.eu-north-1.rds.amazonaws.com"
USER = 'postgres'
PASSWORD = "#Thepearhouse1"
PORT = 5432
DATABASE = 'postgres'
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

engine.connect()

#loading the dataset into a pandas dataframe
from sklearn.datasets import load_iris
import pandas as pd
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])
iris.head()

#the to_sql function moves the data from the dataframe to a table (iris_dataset) in the postgres Amazon RDS
iris.to_sql('iris_dataset', engine, if_exists='replace')