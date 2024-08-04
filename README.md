# GitHub Followers Data

This project collects data from the followers of a specific GitHub user, processes the data, and saves it to a CSV file.

## Requirements

- Python 3.7+
- PySpark
- Requests

## Configuration

### Environment Variables

Set the following environment variables:

- `GITHUB_TOKEN`: Your personal GitHub access token.
- `USER`: GitHub username to collect followers from.
- `CSV_OUTPUT`: Path to the output CSV file.

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
