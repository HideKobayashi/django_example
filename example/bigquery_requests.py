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