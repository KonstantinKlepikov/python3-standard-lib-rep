from typing import Protocol, List, Dict, Union
from datetime import datetime, timedelta
from collections import OrderedDict

class TemperatureMeasurement(datetime):
    pass

class HumidityMeasurement(datetime):
    pass


def calculate_windowed_avg(
        measurements: List[Union[TemperatureMeasurement, HumidityMeasurement]],
        window_size: timedelta,
        field_name: str
    ) -> Dict[datetime, float]:
    window_upper_bound = measurements[0].timestamp + window_size
    current_window = []
    window_averages = OrderedDict()
    for m in measurements:
        # various calculations happen here
        # based on the timestamp of each measurement
        pass
    return window_averages


class MeasurementLike(Protocol):
    timestamp: datetime

def calculate_windowed_avg(
        measurements: List[MeasurementLike],
        window_size: timedelta,
        field_name: str
    ) -> Dict[datetime, float]:
    window_upper_bound = measurements[0].timestamp + window_size
    return window_upper_bound
