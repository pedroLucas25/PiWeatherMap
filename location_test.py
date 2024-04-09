import cli
from unittest.mock import patch
import sys

def test_location():

    test_args = ["cli.py", "brasilia"]

    with patch.object(sys, 'argv', test_args):
        data = cli.return_data()

        lat = data.lat
        lon = data.lon
        
        assert lat == -15.7934036
        assert lon == -47.8823172