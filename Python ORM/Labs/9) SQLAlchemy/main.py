from sqlalchemy.orm import sessionmaker
from models import Employee, engine, City


Session = sessionmaker(bind=engine)
with Session() as session:
    pass
