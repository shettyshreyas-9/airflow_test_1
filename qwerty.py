
import os


# Define the directory and file name
directory = r"C:/Users/sst7260/Documents/shreyas/system_keys/"
file_name = "gcp-test.json"

# Construct the full file path using os.path.join
file_path = os.path.join(directory, file_name)


# Set the path to your service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = file_path
# Print the environment variable
print("GOOGLE_APPLICATION_CREDENTIALS:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))



# Get the path from the environment variable
key_file_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

# Check if the file exists
if os.path.exists(key_file_path):
    print(f"File exists: {key_file_path}")

    # Check if the file is readable
    if os.access(key_file_path, os.R_OK):
        print("File is readable")
    else:
        print("File is not readable")
else:
    print("File does not exist")



from google.cloud import bigquery
# Initialize BigQuery client
client = bigquery.Client()

# Define a test query
sql_query = """
SELECT COUNT(*) as row_count
FROM `aceinternal-2ed449d3.sandbox_ss_eu.dev_result_3`
LIMIT 1
"""

# Execute the query
query_job = client.query(sql_query)
results = query_job.result()

# Print the result
for row in results:
    print(f"Row count: {row.row_count}")