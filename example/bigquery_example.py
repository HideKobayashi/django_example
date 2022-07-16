from google.cloud import bigquery


schema = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
]


def some_query(table_name='blahblahbloo'):

    client = bigquery.Client()
    table_id = f"project.dataset.{table_name}"
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)
