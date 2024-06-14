from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    
    accounts = relationship('Account', back_populates='customer')

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    account_number = Column(String, unique=True, nullable=False)
    account_type = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    customer = relationship('Customer', back_populates='accounts')
    transactions = relationship('Transaction', back_populates='account')

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    transaction_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    
    account = relationship('Account', back_populates='transactions')
