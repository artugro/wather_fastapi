from fastapi import APIRouter, Depends, Query
from fastapi import status
from api.services.weather import WeatherService
from api.models.weather import WeatherActivity, WeatherActivityResponseV1


def init_weather_router():
    weather_router = APIRouter()

    @weather_router.get(
        "/weather", responses={status.HTTP_200_OK: {"model": WeatherActivityResponseV1}}
    )
    def weather(
            weather_service: WeatherService = Depends(),
            zip_code: int = Query(...)
    ) -> WeatherActivity:
        """
        Service to help user decide outside activities
        :param weather_service: A dependency that provides get_outside_activity to retrieve weather data
        :param zip_code: Zip code to validate
        :return:
        """

        return weather_service.get_outside_activity(zip_code)

    return weather_router
