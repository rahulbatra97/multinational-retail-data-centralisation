class DatabaseConnector:


    def read_db_creds(db_creds):
        import yaml
        with open(f'db_creds.yml','r') as f:                       #'r' is for read and 'w' is for write
            credentials = yaml.safe_load(f)
        print(credentials)
    read_db_creds('credentials')


#step 3
#create a class that takes in the dictionary of the db_creds and initialises an SQLALchemy database engine 

    def init_db_engine(credentials):
        from sqlalchemy import create_engine
        credentials = read_db_creds(db_creds)
        # Assuming you have 'db_url' key in the credentials dictionary.
        db_url = credentials['RDS_HOST']
        engine = create_engine(db_url)
        return(engine)
    
    
#step 4
#Using the engine from init_db_engine create a method list_db_tables to list all the tables in the database so you know which tables you can extract data from.
#Develop a method inside your DataExtractor class to read the data from the RDS database.

    def list_db_tables(engine):
        #create an inspector instance
        from sqlalchemy import inspect                                 
        inspector = inspect(engine)
    
    # Get the table names from the database
        table_names = inspector.get_table_names()
        return table_names
    

#step 7 
#upload to database, takes in the pandas dataframe and uploads it as an argument
    def upload_to_db():
