"""
Banking Management System - Business Logic & OOP Domain Models
"""

import datetime
from database import get_connection

class BankingService:
    @staticmethod
    def log_transaction(acc_no: str, tx_type: str, amount: float, balance_after: float, details: str):
        conn = get_connection()
        cursor = conn.cursor()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO transactions (acc_no, tx_type, amount, balance_after, details, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
            (acc_no, tx_type, amount, balance_after, details, now)
        )
        conn.commit()
        conn.close()

    # --- Super Admin Operations ---
    @staticmethod
    def superadmin_login(sid: str, spwd: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM superadmin WHERE sid = ? AND spwd = ?", (sid, spwd))
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def create_admin(aid: str, apwd: str, name: str, sid: str):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO admin (aid, apwd, name, sid) VALUES (?, ?, ?, ?)", (aid, apwd, name, sid))
            conn.commit()
            return True, "Admin created successfully!"
        except Exception as e:
            return False, f"Failed to create admin: {e}"
        finally:
            conn.close()

    @staticmethod
    def list_admins():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT aid, name, sid FROM admin")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def update_superadmin_pwd(sid: str, new_pwd: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE superadmin SET spwd = ? WHERE sid = ?", (new_pwd, sid))
        conn.commit()
        conn.close()
        return True, "Password updated successfully!"

    # --- Admin Operations ---
    @staticmethod
    def admin_login(aid: str, apwd: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin WHERE aid = ? AND apwd = ?", (aid, apwd))
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def create_branch(bid: str, bname: str, city: str, contact: str, email: str, adminid: str):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO branches VALUES (?, ?, ?, ?, ?, ?)", (bid, bname, city, contact, email, adminid))
            conn.commit()
            return True, "Branch created successfully!"
        except Exception as e:
            return False, f"Failed to create branch: {e}"
        finally:
            conn.close()

    @staticmethod
    def create_employee(eid: str, epwd: str, name: str, bid: str, role: str, salary: float):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", (eid, epwd, name, bid, role, salary))
            conn.commit()
            return True, "Employee registered successfully!"
        except Exception as e:
            return False, f"Failed to register employee: {e}"
        finally:
            conn.close()

    @staticmethod
    def transfer_employee(eid: str, new_bid: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT bid FROM branches WHERE bid = ?", (new_bid,))
        if not cursor.fetchone():
            conn.close()
            return False, "Target branch ID does not exist!"
        cursor.execute("UPDATE employees SET bid = ? WHERE eid = ?", (new_bid, eid))
        conn.commit()
        conn.close()
        return True, f"Employee {eid} transferred to Branch {new_bid} successfully!"

    @staticmethod
    def list_branches():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM branches")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def list_employees():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT eid, name, bid, role, salary FROM employees")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    # --- Employee Operations ---
    @staticmethod
    def employee_login(eid: str, epwd: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE eid = ? AND epwd = ?", (eid, epwd))
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def create_customer_account(cid: str, cpwd: str, name: str, email: str, phone: str, address: str, bid: str, acc_no: str, initial_deposit: float, acc_type: str = "Savings"):
        conn = get_connection()
        cursor = conn.cursor()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            cursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)", (cid, cpwd, name, email, phone, address, bid))
            cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?)", (acc_no, cid, acc_type, initial_deposit, now))
            if initial_deposit > 0:
                cursor.execute(
                    "INSERT INTO transactions (acc_no, tx_type, amount, balance_after, details, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                    (acc_no, "DEPOSIT", initial_deposit, initial_deposit, "Account Opening Deposit", now)
                )
            conn.commit()
            return True, f"Customer {name} and Account {acc_no} created successfully!"
        except Exception as e:
            conn.rollback()
            return False, f"Failed to create customer account: {e}"
        finally:
            conn.close()

    @staticmethod
    def process_loan_status(loan_id: int, new_status: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE loans SET status = ? WHERE loan_id = ?", (new_status, loan_id))
        conn.commit()
        conn.close()
        return True, f"Loan #{loan_id} updated to '{new_status}'."

    @staticmethod
    def list_all_loans():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT l.*, c.name as customer_name FROM loans l JOIN customers c ON l.cid = c.cid")
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    # --- Customer / Account Operations ---
    @staticmethod
    def customer_login(cid: str, cpwd: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE cid = ? AND cpwd = ?", (cid, cpwd))
        user = cursor.fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def get_customer_accounts(cid: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE cid = ?", (cid,))
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def get_account(acc_no: str):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE acc_no = ?", (acc_no,))
        acc = cursor.fetchone()
        conn.close()
        return dict(acc) if acc else None

    @staticmethod
    def deposit(acc_no: str, amount: float, details: str = "Cash Deposit"):
        if amount <= 0:
            return False, "Deposit amount must be positive!"
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE acc_no = ?", (acc_no,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return False, "Account not found!"
        
        new_balance = row["balance"] + amount
        cursor.execute("UPDATE accounts SET balance = ? WHERE acc_no = ?", (new_balance, acc_no))
        conn.commit()
        conn.close()

        BankingService.log_transaction(acc_no, "DEPOSIT", amount, new_balance, details)
        return True, f"Successfully deposited ${amount:,.2f}. New Balance: ${new_balance:,.2f}"

    @staticmethod
    def withdraw(acc_no: str, amount: float, details: str = "Cash Withdrawal"):
        if amount <= 0:
            return False, "Withdrawal amount must be positive!"
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE acc_no = ?", (acc_no,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return False, "Account not found!"
        
        if row["balance"] < amount:
            conn.close()
            return False, f"Insufficient funds! Available balance: ${row['balance']:,.2f}"

        new_balance = row["balance"] - amount
        cursor.execute("UPDATE accounts SET balance = ? WHERE acc_no = ?", (new_balance, acc_no))
        conn.commit()
        conn.close()

        BankingService.log_transaction(acc_no, "WITHDRAWAL", amount, new_balance, details)
        return True, f"Successfully withdrew ${amount:,.2f}. New Balance: ${new_balance:,.2f}"

    @staticmethod
    def transfer(sender_acc_no: str, recipient_acc_no: str, amount: float):
        if amount <= 0:
            return False, "Transfer amount must be positive!"
        if sender_acc_no == recipient_acc_no:
            return False, "Cannot transfer funds to the same account!"

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE acc_no = ?", (sender_acc_no,))
        sender = cursor.fetchone()
        cursor.execute("SELECT balance FROM accounts WHERE acc_no = ?", (recipient_acc_no,))
        recipient = cursor.fetchone()

        if not sender:
            conn.close()
            return False, "Sender account not found!"
        if not recipient:
            conn.close()
            return False, "Recipient account not found!"
        if sender["balance"] < amount:
            conn.close()
            return False, f"Insufficient balance for transfer! Available: ${sender['balance']:,.2f}"

        new_sender_bal = sender["balance"] - amount
        new_rec_bal = recipient["balance"] + amount

        cursor.execute("UPDATE accounts SET balance = ? WHERE acc_no = ?", (new_sender_bal, sender_acc_no))
        cursor.execute("UPDATE accounts SET balance = ? WHERE acc_no = ?", (new_rec_bal, recipient_acc_no))
        conn.commit()
        conn.close()

        BankingService.log_transaction(sender_acc_no, "TRANSFER_OUT", amount, new_sender_bal, f"Transferred to {recipient_acc_no}")
        BankingService.log_transaction(recipient_acc_no, "TRANSFER_IN", amount, new_rec_bal, f"Received from {sender_acc_no}")

        return True, f"Transferred ${amount:,.2f} to {recipient_acc_no} successfully! New Balance: ${new_sender_bal:,.2f}"

    @staticmethod
    def get_statement(acc_no: str, limit: int = 10):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE acc_no = ? ORDER BY tx_id DESC LIMIT ?", (acc_no, limit))
        rows = [dict(r) for r in cursor.fetchall()]
        conn.close()
        return rows

    @staticmethod
    def apply_loan(cid: str, amount: float, purpose: str):
        if amount <= 0:
            return False, "Loan amount must be greater than zero!"
        conn = get_connection()
        cursor = conn.cursor()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO loans (cid, amount, status, purpose, applied_at) VALUES (?, ?, ?, ?, ?)",
                       (cid, amount, "Pending", purpose, now))
        conn.commit()
        conn.close()
        return True, "Loan application submitted successfully!"
