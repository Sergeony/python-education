from freezegun import freeze_time
from python.unittesting.to_test import time_of_day


@freeze_time("12:00:01")
def test_time_of_day_for_afternoon():
    assert time_of_day() == "afternoon"


@freeze_time("09:00:01")
def test_time_of_day_for_morning():
    assert time_of_day() == "morning"


@freeze_time("21:00:01")
def test_time_of_day_fro_night():
    assert time_of_day() == "night"
