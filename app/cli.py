from .db import create_customer, create_account, create_transaction, get_all_customers, get_all_accounts, get_transactions, delete_customer

def menu():
    print("\nBank Management System")
    print("1. Create Customer")
    print("2. Create Account")
    print("3. Create Transaction")
    print("4. View Customers")
    print("5. View Accounts")
    print("6. View Transactions for an Account")
    print("7. Delete Customer")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            address = input("Enter customer address: ")
            create_customer(name, email, phone, address)
            print("Customer created!")

        elif choice == '2':
            account_number = input("Enter account number: ")
            account_type = input("Enter account type (savings/checking): ")
            balance = float(input("Enter initial balance: "))
            customer_id = int(input("Enter customer ID: "))
            create_account(account_number, account_type, balance, customer_id)
            print("Account created!")

        elif choice == '3':
            account_id = int(input("Enter account ID: "))
            transaction_type = input("Enter transaction type (deposit/withdraw): ")
            amount = float(input("Enter amount: "))
            create_transaction(account_id, transaction_type, amount)
            print("Transaction created!")

        elif choice == '4':
            customers = get_all_customers()
            print("\nCustomers:")
            for customer in customers:
                print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

        elif choice == '5':
            accounts = get_all_accounts()
            print("\nAccounts:")
            for account in accounts:
                print(f"ID: {account.id}, Account Number: {account.account_number}, Type: {account.account_type}, Balance: {account.balance}")

        elif choice == '6':
            account_id = int(input("Enter account ID: "))
            transactions = get_transactions(account_id)
            print("\nTransactions:")
            for transaction in transactions:
                print(f"ID: {transaction.id}, Type: {transaction.transaction_type}, Amount: {transaction.amount}, Date: {transaction.date}")

        elif choice == '7':
            customer_id = int(input("Enter customer ID: "))
            delete_customer(customer_id)
            print("Customer deleted!")

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()