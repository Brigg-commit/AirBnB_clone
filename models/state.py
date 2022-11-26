#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent Class state that inherits from basemodel
    Attributes:
        name (str): The name of the state.
    """

    name = ""
