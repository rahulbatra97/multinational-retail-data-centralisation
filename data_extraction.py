class DataExtractor:                               
    #Develop a method inside your DataExtractor class to read the data from the RDS database.
    #Develop a method called read_rds_table in your DataExtractor class which will extract 
    #the database table to a pandas DataFrame.
    def read_rds_table():
        import pandas as pd

        #step 4
        #uncertain about this
        from database_utils.py import DatabaseConnector

        data = DatabaseConnector(list_db_tables)
        RDS_database = pd.DataFrame(data['data'], columns=data['feature_names'])
        RDS_database.head()

    #loading the dataset into a pandas dataframe



#This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
#The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket.