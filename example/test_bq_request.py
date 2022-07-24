import pytest
from bq_request import request_bq_query, request_bq_query_get_results, bigquery

@pytest.mark.bq_query_return_data(
    [
        {
            "query": "SELECT * FROM table",
            "table": {
                "columns": [
                    "id_row",
                    "name",
                ],
                "rows": [
                    [1, "Alice"],
                    [2, "Pete"],
                    [3, "Steven"],
                ],
            },
        },
    ]
)
def test_request_bq_query_get_results(bq_client_mock):
    bigquery.Client = bq_client_mock
    expected_row_dicts = [
        {"id_row": 1, "name": "Alice"},
        {"id_row": 2, "name": "Pete"},
        {"id_row": 3, "name": "Steven"},
    ]

    row_iter = request_bq_query_get_results()

    for row, expected_row in zip(row_iter, expected_row_dicts):
        assert dict(row) == expected_row


@pytest.mark.bq_query_return_data(
    [
        {
            "query": "SELECT * FROM table",
            "table": {
                "columns": [
                    "id_row",
                    "name",
                ],
                "rows": [
                    [1, "Alice"],
                    [2, "Pete"],
                    [3, "Steven"],
                ],
            },
        },
    ]
)
def test_request_bq_query_get_results(bq_client_mock):
    bigquery.Client = bq_client_mock
    bigquery.Client().query().job_id = 'jobId99'
    expected_row_dicts = [
        {"id_row": 1, "name": "Alice"},
        {"id_row": 2, "name": "Pete"},
        {"id_row": 3, "name": "Steven"},
    ]

    query_job = request_bq_query()

    print(f"query_job: {query_job}")
    print(f"query_job.job_id: {query_job.job_id}")
    assert query_job.job_id == 'jobId99'