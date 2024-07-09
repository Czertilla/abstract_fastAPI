from typing import TYPE_CHECKING, Annotated, Optional
from uuid import UUID
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_filter import FilterDepends, with_prefix
from pydantic import Field, validator

# from models.roles import RoleORM


class RoleFilter(Filter):
    id__in: Annotated[list[UUID], Field("id_list")] = None
    name__in: Annotated[list[str], Field(alias="names")] = None
    user_id: Annotated[Optional[UUID], Field(alias="owner")] = None
    level__gte: Annotated[int, Field(alias="level_gte", default=0, ge=0)]
    level__lte: Annotated[Optional[int], Field(alias="level_lte", ge=0)] = None

    @validator("level__lte")
    @classmethod
    def validate_level_enumerate(cls, field_value: int, values: dict):
        if (v := values.get("level__gte")) > field_value:
            raise HTTPException(
                status_code=422,
                detail={
                    "loc": [
                        "url",
                        "level_lte"
                    ],
                    "msg": f"level_lte= {field_value} must be greater then level_gte= {v}",
                    "input": field_value
                }
            )
        return field_value

    # class Constants(Filter.Constants):
    #     model = RoleORM

    class Config:
        populate_by_name = True
