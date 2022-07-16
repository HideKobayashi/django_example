import pytest
from unittest.mock import Mock, patch

from bigquery_requests import list_blobs, extract_table

@pytest.fixture
def extract_result():
    'Mock extract_job result with properties needed'
    er = Mock()
    er.return_value = 1
    return er

@pytest.fixture
def extract_job(extract_result):
    'Mock extract_job with properties needed'
    ej = Mock()
    ej.job_id = 1
    ej.result.return_value = 2
    return ej

@patch("bigquery_requests.storageClient")
def test_list_blobs(storageClient):

    storageClient().list_blobs.return_value = [1,2]

    blob_list = list_blobs()

    storageClient().list_blobs.assert_called_with('bucket', prefix='prefix')
    assert blob_list == [1,2]

@patch("bigquery_requests.bigqueryClient")
def test_extract_table(bigqueryClient, extract_job):

    bigqueryClient().extract_table.return_value = extract_job

    job = extract_table()

    bigqueryClient().extract_table.assert_called_with('project.dataset.table_id', destination_uris='uri')
    assert job.job_id == 1
    assert job.result() == 2