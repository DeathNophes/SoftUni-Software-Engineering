from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Relationship

CONNECTION_STRING = 'postgresql+psycopg2://postgres-user:password@localhost:5432/alchemy'

engine = create_engine(CONNECTION_STRING)
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    city_id = Column(Integer, ForeignKey('cities.id'), default=1)
    city = Relationship('City', back_populates='employees')


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    employees = Relationship('Employee')


Base.metadata.create_all(engine)
