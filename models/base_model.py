#!/usr/bin/python3
"""Defines base class for all models"""

from uuid import uuid4
import models
from datetime import datetime
import sqlalchemy
from sqlalchemmy import Column, String, datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
  workerID =