#!/usr/bin/env python3
"""SQLAlchemy model module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User():
