import os

class CSVExporter:
    def __init__(self, output_path):
        self.output_path = output_path
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

    def save_to_csv(self, df):
        if df is not None:
            df.coalesce(1).write.option("header", "true").csv(self.output_path, mode='overwrite')
        else:
            print("DataFrame is None. Cannot save to CSV.")
