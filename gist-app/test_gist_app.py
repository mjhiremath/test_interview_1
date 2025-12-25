import pytest
import json
from gist_app import gist_app


# Create a test fixture for the Flask app
@pytest.fixture
def client():
    # test client to send requests to the Flask app.
    with gist_app.test_client() as client:
        yield client

# Verify the homepage response
def test_home_page(client):
    response = client.get('/')
    # Decode response.data (which is a byte string) to a regular string
    response_data = json.loads(response.data)['message']
    assert response.status_code == 200
    assert response_data == "This app interacts with the public gists github api and responds to requests on /user with a list of the user's publicly available gists"

# Verify the content type of user endpoint
def test_user_endpoint_content_type(client):
    response = client.get("/octocat")
    content_type = response.headers.get('Content-Type')
    assert content_type == 'application/json'

# Verify existing github user with gists
def test_exist_user_gists(client):
    # Send a GET request to the Flask API with octocat user
    response = client.get('/octocat')

    # Assert the response status code is 200
    assert response.status_code == 200

    # Assert the response contains the correct data
    response_data = json.loads(response.data)

    # Assert the number of gists
    assert len(response_data) == 8

    # Assert whether returned gists are public
    for gists in response_data:
        assert gists['public'] == True

# Verify existing github user with no gists
def test_exist_user_no_gists(client):
    # Send a GET request to the Flask API
    response = client.get('/mjshiremath')  # Example user: 'octocat'

    # Assert the response status code is 404 (no gists found)
    assert response.status_code == 404

    # Assert the response returned the correct message
    response_data = json.loads(response.data)
    assert response_data['message'] == 'No public gists found for this user.'


# Verify non existing github user
def test_nonexist_user_gists(client):
    # Send a GET request to the Flask API
    response = client.get('/nonexistmjhiremath')

    # Assert the response status code is 404
    assert response.status_code == 404

    # Assert the error message in the response
    response_data = json.loads(response.data)
    assert response_data['error'] == 'User is not exist in github'
    assert response_data['message']['message'] == 'Not Found'

# Verify Rate limit error handling
def test_error_handles_rate_limiting(client, mocker):

    # Mock the requests.get method using pytest-mock
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=429))

    # Send a GET request to the Flask API
    response = client.get('/octocat')

    # Assert the response status code is 429 (rate limiting)
    assert response.status_code == 429

    # Assert the error message in the response
    assert response.json == {"error": "Rate limit exceeded. Please try again later."}

# Verify server error handling
def test_server_error_handling(client, mocker):
    # Simulate an exception when calling the GitHub API
    mocker.patch('requests.get', side_effect=Exception("Internal Server error"))

    # Send a GET request to the Flask API
    response = client.get('/octocat')  # Example user: 'octocat'

    # Assert the response status code is 500 (internal server error)
    assert response.status_code == 500

    # Assert the error message in the response
    response_data = json.loads(response.data)
    assert response_data['error'] == 'Oops, something went wrong on our end. Please try refreshing the page or come back later'
    assert response_data['message'] == 'Internal Server error'