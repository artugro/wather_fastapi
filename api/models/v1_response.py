from typing import Any
from api.models.base import BaseModel


class V1Response(BaseModel):
    api_version: str = "v1"
    data: BaseModel = BaseModel()
    meta: Any = {}
