import logging
import requests

from api.models.weather import WeatherActivity
from api.exceptions import APIException

logger = logging.getLogger()


class WeatherService:
    """
    Weather service
    """

    def __init__(self):
        self.BASE_WEATHER_API_URL = "http://api.weatherstack.com"
        self.ACCESS_KEY = ""

    def get_outside_activity(self, zip_code: int) -> WeatherActivity:
        """
        Get list of activities based on weather conditions

        :param zip_code: Zip code to validate
        :return WeatherActivity:
        """
        url = f"{self.BASE_WEATHER_API_URL}/current?access_key={self.ACCESS_KEY}&query={zip_code}"
        response = requests.get(url).json()

        if not response:
            logger.error(
                "Error while processing API Weather request",
                extra={"zip_code": zip_code},
            )
            raise APIException()

        is_raining = (
            True
            if "Rain" in response.get("current").get("weather_descriptions")
            else False
        )
        uv_index = response.get("current").get("uv_index")
        wind_speed = response.get("current").get("wind_speed")
        return WeatherActivity(
            can_i_go_outside=False if is_raining else True,
            should_i_wear_sunscreen=True if uv_index > 3 else False,
            can_i_fly_my_kite=True if is_raining and wind_speed > 15 else False,
        )
