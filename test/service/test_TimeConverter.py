from datetime import datetime
from unittest import TestCase

from service.time_converter import TimeConverter

class TestTimeConverter(TestCase):
    def test_calculate_elapsed_time_in_hours_from_two_unix_timestamps(self):
        earlier = self.unix_time_of(datetime.fromisoformat('2018-05-24T11:30:00'))
        later = self.unix_time_of(datetime.fromisoformat('2018-05-24T12:00:00'))

        self.assertEqual(TimeConverter.time_elapsed_in_hours(earlier, later), 0.5)

    def unix_time_of(self, dt):
        return (dt - datetime(1970,1,1)).total_seconds()