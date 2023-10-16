from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#silka k baze dannix
SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'

##podklyucheniya
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#obshiy klass dlya nasledovaniya models
Base = declarative_base()

#generator cessiy
session = sessionmaker(bind=engine)

#import vsex klassov
from database import models

#generator podklyucheniya k baze

def get_db():
    db = session()
    try:
        yield db

    except:
        db.rollback()
        raise
    finally:
        db.close()