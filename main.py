import os
from github_client import GitHubClient
from dataframe_builder import DataFrameBuilder
from csv_exporter import CSVExporter

def main():
    """
    Main function to execute the GitHub followers data collection and processing.
    """
    github_token = os.getenv('GITHUB_TOKEN')
    user = os.getenv('USER')
    csv_output = f"output/github_{user}_followers"

    if not github_token or not user:
        raise ValueError("Environment variables GITHUB_TOKEN and USER must be set.")

    github_client = GitHubClient(github_token, user)
    dataframe_builder = DataFrameBuilder()
    csv_exporter = CSVExporter(csv_output)

    followers_data = github_client.collect_followers_data()
    if followers_data:
        dataframe = dataframe_builder.process_followers_data(followers_data)
        csv_exporter.save_to_csv(dataframe)
    else:
        print("No follower data found.")

if __name__ == "__main__":
    main()
