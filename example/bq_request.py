from google.cloud import bigquery

def request_bq_query_get_results():
    bq_client = bigquery.Client(project='test')
    query_str = "SELECT * FROM `test.dataset.table_id`"
    query_job = bq_client.query(query_str)
    results = query_job.results()
    return results

def request_bq_query():
    bq_client = bigquery.Client(project='test')
    query_str = "SELECT * FROM `test.dataset.table_id`"
    query_job = bq_client.query(query_str)
    return query_job