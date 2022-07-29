# -*- coding: UTF-8 -*-
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import date


class extensiontoqueuelink(SQLModel, table=True):
    estension_id: Optional[int] = Field(
        default=None, foreign_key="extensions.id", primary_key=True
    )
    queue_id: Optional[int] = Field(
        default=None, foreign_key="queues.id", primary_key=True
    )


class extensions(SQLModel, table=True):
    """
    Table listant les extensions(n° 3cx)
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    extension: str
    name: str
    mail: str
    date_added: date = Field(default=date.today())
    date_out: date
    sorti: bool
    queuelist: List["queues"] = Relationship(back_populates="extensions",
                                             link_model=extensiontoqueuelink)


class queues(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    queue: str
    queuename: str
    extensionslist: List["extensions"] = Relationship(back_populates="extensions",
                                                      link_model=extensiontoqueuelink)