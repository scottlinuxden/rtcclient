import pytest
from rtcclient.client import RTCClient
import requests


@pytest.fixture(scope="function")
def rtcclient(mocker):
    mock_resp = mocker.MagicMock(spec=requests.Response)
    mock_resp.status_code = 200
    mock_resp.headers = {"set-cookie": "cookie-id"}

    mocked_headers = mocker.patch("rtcclient.client.RTCClient._get_headers")
    mocked_headers.return_value = mock_resp

    return RTCClient(url="http://test.url:9443/jazz",
                     username="user",
                     password="password")