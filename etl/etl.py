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

# Format columns and create dictionary dtype
wine_red.columns=wine_red.columns.str.replace(' ', '_')
wine_white.columns=wine_white.columns.str.replace(' ', '_')
maptype_dict={np.dtype(float): 'Float', np.dtype(int): 'Integer'}

wine_red_dtype_dic = wine_red.dtypes.map(maptype_dict).to_dict()
wine_white_dtype_dic = wine_white.dtypes.map(maptype_dict).to_dict()

# Select Small_movie database and create tables
engine = db.create_engine(mysql_str+'Wine')
con=engine.connect()

Base=declarative_base()

# TODO: complete the classes
class WineRed(Base):
    """
    # Class for creating the links table.
    """
    __tablename__ = 'wine_red'
    
    index=Column(Integer, primary_key=True) 



Base.metadata.create_all(engine)
con.close()
"""
print('Done.\n')

print('Insert data from csv to database.\n')
print('-'*30)
# Insert data to database
engine = db.create_engine(mysql_str+'Wine')
con=engine.connect()

links.to_sql(name='wine',\
             con=engine,\
             if_exists='replace')

con.close()
print('Done.')
"""