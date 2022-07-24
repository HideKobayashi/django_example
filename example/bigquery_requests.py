from google.cloud.bigquery import Client as bigqueryClient
from google.cloud.storage import Client as storageClient

def list_blobs():

    storage_client = storageClient(project='test')

    blobs = storage_client.list_blobs('bucket', prefix='prefix')

    return blobs

def extract_table():

    bigquery_client = bigqueryClient(project='test')

    job = bigquery_client.extract_table('project.dataset.table_id', destination_uris='uri')

    return job

def request_bq_query_get_results():
    bq_client = bigqueryClient(project='test')
    query_str = "SELECT * FROM `test.dataset.table_id`"
    query_job = bq_client.query(query_str)
    results = query_job.results()
    return results

def request_bq_query():
    bq_client = bigqueryClient(project='test')
    query_str = "SELECT * FROM `test.dataset.table_id`"
    query_job = bq_client.query(query_str)
    return query_job