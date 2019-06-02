import threading

class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.is_open = 0
        self.bank_lock = threading.Lock()

    def get_balance(self):
        if self.is_open == 1:
            return self.balance
        else:
            raise ValueError("Account closed")

    def open(self):
        if self.is_open == 0:
            self.balance = 0
            self.is_open = 1
        else:
            raise ValueError("Account currently is open")

    def deposit(self, amount):
        if self.is_open == 0:
            raise ValueError("Account closed")

        if amount < 0:
            raise ValueError("Invalid")

        self.bank_lock.acquire()
        self.balance += amount
        self.bank_lock.release()

    def withdraw(self, amount):
        if self.is_open == 0:
            raise ValueError("Account closed")

        if amount < 0:
            raise ValueError("Invalid")

        if amount > self.balance:
            raise ValueError("Invalid amount")

        self.bank_lock.acquire()
        self.balance -= amount
        self.bank_lock.release()
        
    def close(self):
        if self.is_open == 1:
            self.is_open = 0
        else:
            raise ValueError('Account currently is closed.')

