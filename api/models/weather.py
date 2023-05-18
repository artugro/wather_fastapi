from api.models.base import BaseModel
from api.models.v1_response import V1Response


class WeatherActivity(BaseModel):
    can_i_go_outside: bool
    should_i_wear_sunscreen: bool
    can_i_fly_my_kite: bool


class WeatherActivityResponseV1(V1Response):
    data: WeatherActivity
