import pandas as pd 
import numpy as np
import sqlalchemy as db
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
import os

SQL_USR, SQL_PSW= os.environ['SQL_USR'], os.environ['SQL_PSW']
mysql_str = 'mysql+mysqlconnector://'+SQL_USR+':'+SQL_PSW+'@localhost:3306/'

# Create Wine database
print('Create database Wine.')
print('-'*30)
engine = db.create_engine(mysql_str)
con=engine.connect()
con.execute('commit')
con.execute('CREATE DATABASE if NOT EXISTS Wine;')
con.close()
print('Done.\n')

print('Create tables')
print('-'*30)

# Load csv data
wine_red = pd.read_csv('../data/winequality_red.csv',\
                    header=0)
wine_white = pd.read_csv('../data/winequality_white.csv',\
                    header=0)

# Select Small_movie database and create tables
engine = db.create_engine(mysql_str+'Wine')
con=engine.connect()

Base=declarative_base()
wine_red.columns=wine_red.columns.str.replace(' ', '_')
wine_white.columns=wine_white.columns.str.replace(' ', '_')
wine_red.info()
# TODO: complete the classes
class WineRed(Base):
    """
    # Class for creating the links table.
    """
    __tablename__ = 'wine_red'
    
    index=Column(Integer, primary_key=True) 
    fixed_acidity=Column(Float)
    volatile_acidity=Column(Float)
    citric_acid=Column(Float)
    residual_sugar=Column(Float)
    chlorides=Column(Float)
    free_sulfur_dioxide=Column(Float)
    total_sulfur_dioxide=Column(Float)
    density=Column(Float)
    pH=Column(Float)
    sulphates=Column(Float)
    alcohol=Column(Float)
    quality=Column(Integer)

    def __init__(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality):
        self.fixed_acidity=fixed_acidity
        self.volatile_acidity=volatile_acidity
        self.citric_acid=citric_acid
        self.residual_sugar=residual_sugar
        self.chlorides=chlorides
        self.free_sulfur_dioxide=free_sulfur_dioxide
        self.total_sulfur_dioxide=total_sulfur_dioxide
        self.density=density
        self.pH=pH
        self.sulphates=sulphates
        self.alcohol=alcohol
        self.quality=quality

class WineWhite(Base):
    """
    # Class for creating the links table.
    """
    __tablename__ = 'wine_white'
    
    index=Column(Integer, primary_key=True) 
    fixed_acidity=Column(Float)
    volatile_acidity=Column(Float)
    citric_acid=Column(Float)
    residual_sugar=Column(Float)
    chlorides=Column(Float)
    free_sulfur_dioxide=Column(Float)
    total_sulfur_dioxide=Column(Float)
    density=Column(Float)
    pH=Column(Float)
    sulphates=Column(Float)
    alcohol=Column(Float)
    quality=Column(Integer)

    def __init__(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality):
        self.fixed_acidity=fixed_acidity
        self.volatile_acidity=volatile_acidity
        self.citric_acid=citric_acid
        self.residual_sugar=residual_sugar
        self.chlorides=chlorides
        self.free_sulfur_dioxide=free_sulfur_dioxide
        self.total_sulfur_dioxide=total_sulfur_dioxide
        self.density=density
        self.pH=pH
        self.sulphates=sulphates
        self.alcohol=alcohol
        self.quality=quality

Base.metadata.create_all(engine)
con.close()

print('Done.\n')

print('Insert data from csv to database.\n')
print('-'*30)
# Insert data to database
engine = db.create_engine(mysql_str+'Wine')
con=engine.connect()

wine_red.to_sql(name='wine_red',\
             con=engine,\
             if_exists='replace')

wine_white.to_sql(name='wine_white',\
             con=engine,\
             if_exists='replace')

con.close()
print('Done.')
