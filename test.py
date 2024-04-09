import cli
from unittest.mock import patch
import sys

def test_location_request():

    test_args = ["cli.py", "brasilia"]

    with patch.object(sys, 'argv', test_args):
        data = cli.return_data()

        lat = data.lat
        lon = data.lon
        
        assert lat == -15.7934
        assert lon == -47.8823

def test_wheather_request():

    test_args = ["cli.py", "brasilia"]

    with patch.object(sys, 'argv', test_args):
        data = cli.return_data()

        timezone_offset = data.timezone_offset
        
        assert timezone_offset == -10800
