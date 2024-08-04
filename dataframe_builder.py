from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType, IntegerType, StructType, StructField
from datetime import datetime

class DataFrameBuilder:
    def __init__(self):
        """
        Initialize the Spark session for building DataFrames.
        """
        self.spark = SparkSession.builder.appName("GitHub Followers Data").getOrCreate()
        self.spark.sparkContext.setLogLevel("ERROR")

    def create_dataframe(self, data):
        """
        Create a PySpark DataFrame from the collected data.

        Args:
            data (list): List of dictionaries with follower data.

        Returns:
            DataFrame: PySpark DataFrame.
        """
        schema = StructType([
            StructField("name", StringType(), True),
            StructField("company", StringType(), True),
            StructField("blog", StringType(), True),
            StructField("email", StringType(), True),
            StructField("bio", StringType(), True),
            StructField("public_repos", IntegerType(), True),
            StructField("followers", IntegerType(), True),
            StructField("following", IntegerType(), True),
            StructField("created_at", StringType(), True)
        ])
        df = self.spark.createDataFrame(data, schema=schema)
        return df

    def treat_created_at(self, df):
        """
        Convert the 'created_at' field to 'day/month/year' format.

        Args:
            df (DataFrame): PySpark DataFrame.

        Returns:
            DataFrame: Updated DataFrame.
        """
        treat_date_udf = udf(lambda date_str: datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y") if date_str else date_str, StringType())
        return df.withColumn("created_at", treat_date_udf(col("created_at")))

    def treat_company(self, df):
        """
        Remove '@' from the beginning of the 'company' field.

        Args:
            df (DataFrame): PySpark DataFrame.

        Returns:
            DataFrame: Updated DataFrame.
        """
        clean_company_udf = udf(lambda company: company[1:] if company and company.startswith('@') else company, StringType())
        return df.withColumn("company", clean_company_udf(col("company")))

    def process_followers_data(self, followers_data):
        """
        Process and transform the GitHub followers data.

        Args:
            followers_data (list): List of followers' data.

        Returns:
            DataFrame: Processed PySpark DataFrame.
        """
        df = self.create_dataframe(followers_data)
        df = self.treat_created_at(df)
        df = self.treat_company(df)
        df.show(truncate=False)
        return df
