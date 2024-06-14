from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from .models import Base

# Create an engine
engine = create_engine("sqlite:///bank.db", echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()


from app.models import Customer, Account, Transaction
from app.db import session

# Create a new customer
def create_customer(name, email, phone, address):
    new_customer = Customer(name=name, email=email, phone=phone, address=address)
    session.add(new_customer)
    session.commit()

# Create a new account
def create_account(account_number, account_type, balance, customer_id):
    new_account = Account(account_number=account_number, account_type=account_type, balance=balance, customer_id=customer_id)
    session.add(new_account)
    session.commit()

# Create a new transaction
def create_transaction(account_id, transaction_type, amount):
    account = session.query(Account).get(account_id)

    if not account:
        raise ValueError("Account not found")  # Raise an exception
    
    new_transaction = Transaction(account_id=account_id, transaction_type=transaction_type, amount=amount)
    
    if transaction_type == 'deposit':
        account.balance += amount
    elif transaction_type == 'withdraw' and account.balance >= amount:
        account.balance -= amount
    else:
        print("Insufficient funds for withdrawal.")
        return

    session.add(new_transaction)
    session.commit()


# Get all customers
def get_all_customers():
    return session.query(Customer).all()

# Get all accounts
def get_all_accounts():
    return session.query(Account).all()

# Get all transactions for an account
def get_transactions(account_id):
    return session.query(Transaction).filter_by(account_id=account_id).all()

# Delete a customer (and cascade delete their accounts and transactions)
def delete_customer(customer_id):
    customer = session.query(Customer).get(customer_id)
    session.delete(customer)
    session.commit()
