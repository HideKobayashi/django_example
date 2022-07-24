from bigquery_example import schema, some_query, bigquery
from unittest import mock


# stackOverFlow から pytest-mock を使った例
def test_some_query(mocker):
    mock_table = mocker.patch('google.cloud.bigquery.Table', autospec=True)
    mock_client = mocker.patch('google.cloud.bigquery.Client', autospec=True)

    some_query()  # run with mocked objects

    mock_table.assert_called_with('project.dataset.blahblahbloo', schema=schema)
    # print(f"mock_table.return_value: {mock_table.return_value}")
    mock_client().create_table.assert_called_with(mock_table.return_value)


# unittest.mock を使った書き方１
def test_some_query1():
    with mock.patch('bigquery_example.bigquery.Client', autospec=True) as mock_client:
        with mock.patch('bigquery_example.bigquery.Table', autospec=True) as mock_table:
            some_query()  # run with mocked objects

    mock_table.assert_called_with('project.dataset.blahblahbloo', schema=schema)
    # print(f"mock_table.return_value: {mock_table.return_value}")
    mock_client().create_table.assert_called_with(mock_table.return_value)

# unittest.mock を使った書き方２
@mock.patch('bigquery_example.bigquery.Client')
@mock.patch('bigquery_example.bigquery.Table')
def test_some_query2(mock_table, mock_client):

    some_query()  # run with mocked objects

    mock_table.assert_called_with('project.dataset.blahblahbloo', schema=schema)
    print(f"mock_table.return_value: {mock_table.return_value}")
    mock_client().create_table.assert_called_with(mock_table.return_value)