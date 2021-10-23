# -*- coding: utf-8 -*-
""" SQLAlchemy 2.0
"""
from sqlalchemy import create_engine

engine = create_engine("sqlite:////media/alxfed/data/dbase/sqla2.sqlite", future=True)
