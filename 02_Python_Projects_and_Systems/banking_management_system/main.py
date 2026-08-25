"""
Banking Management System - Interactive Console Interface
Author: Juzer Tezabwala
Description: Production-ready enterprise banking management simulator with multi-tier role access:
             1. Super Administrator
             2. Branch Administrator
             3. Bank Operations Employee
             4. Customer Account Holder
"""

import sys
from database import init_db
from models import BankingService

def print_header(title: str):
    print("\n" + "=" * 60)
    print(f"   {title.upper()}")
    print("=" * 60)

def format_currency(amount: float) -> str:
    return f"${amount:,.2f}"

def superadmin_menu(user: dict):
    while True:
        print_header(f"Super Admin Portal - Logged in as: {user['name']}")
        print("1. Create New Branch Admin")
        print("2. List All Branch Admins")
        print("3. Change Super Admin Password")
        print("4. Logout to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n--- Create New Admin ---")
            aid = input("Enter Admin ID (e.g. admin2): ").strip()
            name = input("Enter Admin Full Name: ").strip()
            pwd = input("Enter Admin Password: ").strip()
            if not aid or not name or not pwd:
                print("❌ All fields are required!")
                continue
            success, msg = BankingService.create_admin(aid, pwd, name, user["sid"])
            print("✅ " + msg if success else "❌ " + msg)
            
        elif choice == "2":
            print("\n--- Registered Branch Admins ---")
            admins = BankingService.list_admins()
            if not admins:
                print("No admins found.")
            else:
                for a in admins:
                    print(f" • ID: {a['aid']:<10} | Name: {a['name']:<25} | Created By: {a['sid']}")
                    
        elif choice == "3":
            new_pwd = input("Enter New Password: ").strip()
            if len(new_pwd) < 4:
                print("❌ Password must be at least 4 characters!")
                continue
            success, msg = BankingService.update_superadmin_pwd(user["sid"], new_pwd)
            print("✅ " + msg if success else "❌ " + msg)
            
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def admin_menu(user: dict):
    while True:
        print_header(f"Branch Admin Portal - Logged in as: {user['name']}")
        print("1. Create New Branch")
        print("2. Register New Employee")
        print("3. Transfer Employee to Another Branch")
        print("4. View All Branches")
        print("5. View All Employees")
        print("6. Logout to Main Menu")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Create New Branch ---")
            bid = input("Enter Branch ID (e.g. B002): ").strip()
            bname = input("Enter Branch Name: ").strip()
            city = input("Enter City: ").strip()
            contact = input("Enter Contact Number: ").strip()
            email = input("Enter Branch Email: ").strip()
            success, msg = BankingService.create_branch(bid, bname, city, contact, email, user["aid"])
            print("✅ " + msg if success else "❌ " + msg)
            
        elif choice == "2":
            print("\n--- Register New Employee ---")
            eid = input("Enter Employee ID (e.g. EMP002): ").strip()
            name = input("Enter Full Name: ").strip()
            pwd = input("Enter Temporary Password: ").strip()
            bid = input("Enter Branch ID: ").strip()
            role = input("Enter Role (e.g. Teller / Manager / Loan Officer): ").strip() or "Associate"
            try:
                salary = float(input("Enter Salary ($): ").strip() or 40000.0)
            except ValueError:
                salary = 40000.0
            success, msg = BankingService.create_employee(eid, pwd, name, bid, role, salary)
            print("✅ " + msg if success else "❌ " + msg)
            
        elif choice == "3":
            print("\n--- Transfer Employee ---")
            eid = input("Enter Employee ID: ").strip()
            new_bid = input("Enter New Branch ID: ").strip()
            success, msg = BankingService.transfer_employee(eid, new_bid)
            print("✅ " + msg if success else "❌ " + msg)
            
        elif choice == "4":
            print("\n--- Branch Network ---")
            branches = BankingService.list_branches()
            for b in branches:
                print(f" • [{b['bid']}] {b['bname']} | City: {b['city']} | Tel: {b['contact']} | Email: {b['email']}")
                
        elif choice == "5":
            print("\n--- Staff Directory ---")
            employees = BankingService.list_employees()
            for e in employees:
                print(f" • [{e['eid']}] {e['name']:<20} | Branch: {e['bid']:<6} | Role: {e['role']:<15} | Salary: {format_currency(e['salary'])}")
                
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def employee_menu(user: dict):
    while True:
        print_header(f"Employee Operations Portal - {user['name']} ({user['role']})")
        print("1. Open New Customer Bank Account")
        print("2. Deposit Cash for Customer")
        print("3. Withdraw Cash for Customer")
        print("4. Process / Review Loan Applications")
        print("5. Check Account Balance & Statement")
        print("6. Logout to Main Menu")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Open Customer Account ---")
            cid = input("Enter Customer ID (e.g. CUST002): ").strip()
            name = input("Enter Customer Full Name: ").strip()
            pwd = input("Enter Customer Login Password: ").strip()
            email = input("Enter Email Address: ").strip()
            phone = input("Enter Phone Number: ").strip()
            address = input("Enter Residential Address: ").strip()
            acc_no = input("Enter New Account Number (e.g. ACC1002): ").strip()
            acc_type = input("Account Type (Savings/Current) [Savings]: ").strip() or "Savings"
            try:
                deposit = float(input("Initial Deposit Amount ($): ").strip() or 0.0)
            except ValueError:
                deposit = 0.0
            
            success, msg = BankingService.create_customer_account(
                cid, pwd, name, email, phone, address, user["bid"], acc_no, deposit, acc_type
            )
            print("✅ " + msg if success else "❌ " + msg)
            
        elif choice == "2":
            acc_no = input("Enter Account Number: ").strip()
            try:
                amt = float(input("Enter Deposit Amount ($): ").strip())
                success, msg = BankingService.deposit(acc_no, amt, "Teller Cash Deposit")
                print("✅ " + msg if success else "❌ " + msg)
            except ValueError:
                print("❌ Invalid amount format.")
                
        elif choice == "3":
            acc_no = input("Enter Account Number: ").strip()
            try:
                amt = float(input("Enter Withdrawal Amount ($): ").strip())
                success, msg = BankingService.withdraw(acc_no, amt, "Teller Cash Withdrawal")
                print("✅ " + msg if success else "❌ " + msg)
            except ValueError:
                print("❌ Invalid amount format.")
                
        elif choice == "4":
            print("\n--- Loan Management ---")
            loans = BankingService.list_all_loans()
            if not loans:
                print("No active loan applications.")
            else:
                for l in loans:
                    print(f" • ID: #{l['loan_id']} | Applicant: {l['customer_name']} ({l['cid']}) | Amount: {format_currency(l['amount'])} | Status: {l['status']} | Purpose: {l['purpose']}")
                
                lid = input("\nEnter Loan ID to update status (or Press Enter to skip): ").strip()
                if lid.isdigit():
                    new_status = input("Enter New Status (Approved / Rejected / Pending): ").strip()
                    if new_status:
                        success, msg = BankingService.process_loan_status(int(lid), new_status)
                        print("✅ " + msg)
                        
        elif choice == "5":
            acc_no = input("Enter Account Number: ").strip()
            acc = BankingService.get_account(acc_no)
            if not acc:
                print("❌ Account not found.")
            else:
                print(f"\nAccount #{acc['acc_no']} ({acc['acc_type']}) | Current Balance: {format_currency(acc['balance'])}")
                print("\nRecent Transactions:")
                statement = BankingService.get_statement(acc_no, 5)
                for s in statement:
                    print(f" • [{s['timestamp']}] {s['tx_type']:<12} {format_currency(s['amount']):<12} | Bal: {format_currency(s['balance_after']):<12} | {s['details']}")
                    
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def customer_menu(user: dict):
    accounts = BankingService.get_customer_accounts(user["cid"])
    if not accounts:
        print("❌ No active accounts linked to this profile. Please contact customer support.")
        return

    primary_acc = accounts[0]["acc_no"]

    while True:
        # Refresh account data
        acc_data = BankingService.get_account(primary_acc)
        balance = acc_data["balance"] if acc_data else 0.0

        print_header(f"Customer Banking Portal - Welcome, {user['name']}")
        print(f"Account Number : {primary_acc} ({acc_data.get('acc_type', 'Savings')})")
        print(f"Current Balance: {format_currency(balance)}")
        print("-" * 60)
        print("1. Deposit Funds (Instant)")
        print("2. Withdraw Funds")
        print("3. Transfer Money to Another Account")
        print("4. View Detailed Account Statement (Passbook)")
        print("5. Apply for Personal / Business Loan")
        print("6. Switch / Select Account")
        print("7. Logout to Main Menu")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            try:
                amt = float(input("Enter Deposit Amount ($): ").strip())
                success, msg = BankingService.deposit(primary_acc, amt, "Online Mobile Deposit")
                print("✅ " + msg if success else "❌ " + msg)
            except ValueError:
                print("❌ Invalid amount format.")
                
        elif choice == "2":
            try:
                amt = float(input("Enter Withdrawal Amount ($): ").strip())
                success, msg = BankingService.withdraw(primary_acc, amt, "ATM/Online Withdrawal")
                print("✅ " + msg if success else "❌ " + msg)
            except ValueError:
                print("❌ Invalid amount format.")
                
        elif choice == "3":
            rec_acc = input("Enter Recipient Account Number: ").strip()
            try:
                amt = float(input("Enter Transfer Amount ($): ").strip())
                success, msg = BankingService.transfer(primary_acc, rec_acc, amt)
                print("✅ " + msg if success else "❌ " + msg)
            except ValueError:
                print("❌ Invalid amount format.")
                
        elif choice == "4":
            print(f"\n--- Account Statement for {primary_acc} ---")
            statement = BankingService.get_statement(primary_acc, 10)
            if not statement:
                print("No transactions recorded yet.")
            else:
                print(f"{'TX ID':<6} | {'Timestamp':<20} | {'Type':<12} | {'Amount':<10} | {'Balance':<10} | {'Details'}")
                print("-" * 80)
                for s in statement:
                    print(f"#{s['tx_id']:<5} | {s['timestamp']:<20} | {s['tx_type']:<12} | {format_currency(s['amount']):<10} | {format_currency(s['balance_after']):<10} | {s['details']}")
                    
        elif choice == "5":
            try:
                amt = float(input("Enter Desired Loan Amount ($): ").strip())
                purpose = input("Enter Purpose of Loan: ").strip()
                success, msg = BankingService.apply_loan(user["cid"], amt, purpose)
                print("✅ " + msg if success else "❌ " + msg)
            except ValueError:
                print("❌ Invalid amount format.")
                
        elif choice == "6":
            accounts = BankingService.get_customer_accounts(user["cid"])
            print("\nAvailable Accounts:")
            for idx, a in enumerate(accounts, 1):
                print(f" {idx}. #{a['acc_no']} ({a['acc_type']}) - Balance: {format_currency(a['balance'])}")
            sel = input("Select Account number: ").strip()
            if sel.isdigit() and 1 <= int(sel) <= len(accounts):
                primary_acc = accounts[int(sel) - 1]["acc_no"]
                print(f"Switched active account to #{primary_acc}")
                
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def main():
    # Initialize SQLite database with seed data
    init_db()

    while True:
        print_header("Enterprise Banking Management System")
        print("Please choose your login portal:")
        print("  1. Super Administrator (Management & Oversight)")
        print("  2. Branch Administrator (Staff & Branch Operations)")
        print("  3. Bank Employee / Operations Executive")
        print("  4. Customer Banking Portal")
        print("  5. View Demo Credentials & System Info")
        print("  6. Exit Application")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == "1":
            sid = input("Enter Super Admin ID (Default: super1): ").strip()
            pwd = input("Enter Password (Default: admin123): ").strip()
            user = BankingService.superadmin_login(sid, pwd)
            if user:
                superadmin_menu(user)
            else:
                print("❌ Invalid Super Admin ID or Password!")
                
        elif choice == "2":
            aid = input("Enter Admin ID (Default: admin1): ").strip()
            pwd = input("Enter Password (Default: admin123): ").strip()
            user = BankingService.admin_login(aid, pwd)
            if user:
                admin_menu(user)
            else:
                print("❌ Invalid Admin ID or Password!")
                
        elif choice == "3":
            eid = input("Enter Employee ID (Default: EMP001): ").strip()
            pwd = input("Enter Password (Default: emp123): ").strip()
            user = BankingService.employee_login(eid, pwd)
            if user:
                employee_menu(user)
            else:
                print("❌ Invalid Employee ID or Password!")
                
        elif choice == "4":
            cid = input("Enter Customer ID (Default: CUST001): ").strip()
            pwd = input("Enter Password (Default: cust123): ").strip()
            user = BankingService.customer_login(cid, pwd)
            if user:
                customer_menu(user)
            else:
                print("❌ Invalid Customer ID or Password!")
                
        elif choice == "5":
            print("\n" + "=" * 60)
            print("   DEMO CREDENTIALS (READY OUT OF THE BOX)")
            print("=" * 60)
            print(" • Super Admin : ID: 'super1'  | Password: 'admin123'")
            print(" • Branch Admin: ID: 'admin1'  | Password: 'admin123'")
            print(" • Employee    : ID: 'EMP001'  | Password: 'emp123'")
            print(" • Customer    : ID: 'CUST001' | Password: 'cust123' (Account: ACC1001)")
            print("=" * 60)
            
        elif choice == "6":
            print("\nThank you for using Enterprise Banking Management System. Goodbye!\n")
            sys.exit(0)
        else:
            print("❌ Invalid selection. Please enter 1-6.")

if __name__ == "__main__":
    main()
