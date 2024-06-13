from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# username:password@host:port/database
engine = create_engine("mssql+pymssql://dbadmin:Qwerty123@smx2024.database.windows.net:1433/dataAnalytics")
Session = sessionmaker(bind=engine)
sesija = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users_nenad"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)


class Employee(Base):
    __tablename__ = "employees_nenad"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    age = Column(Integer)
    position = Column(String)
    salary = Column(Integer)
    years_in_company = Column(Integer)

class Product(Base):
    __tablename__ = "products_nenad"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)

class Sale(Base):
    __tablename__ = "sales_nenad"

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey("employees_nenad.id"))
    product_id = Column(ForeignKey("products_nenad.id"))


    employee = relationship("Employee")
    product = relationship("Product")


Base.metadata.create_all(engine)



