#!/usr/bin/python3
"""Contains the City class definition."""

from sqlalchemy import Column, Integer, String, ForeignKey

from relationship_state import Base


class City(Base):
    """City class linked to the cities table."""

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
