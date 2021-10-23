# -*- coding: utf-8 -*-
""" SQLAlchemy 2.0
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:////media/alxfed/data/dbase/sqla2.sqlite", future=True)
Session = sessionmaker(engine, future=True)
