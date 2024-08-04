import os

class CSVExporter:
    def __init__(self, output_path):
        """
        Initialize CSVExporter with a path to save the CSV file.

        Args:
            output_path (str): Path to save the CSV file.
        """
        self.output_path = output_path
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

    def save_to_csv(self, df):
        """
        Save the DataFrame to a CSV file.

        Args:
            df (DataFrame): PySpark DataFrame to save.
        """
        if df is not None:
            df.coalesce(1).write.option("header", "true").csv(self.output_path, mode='overwrite')
        else:
            print("DataFrame is None. Cannot save to CSV.")
