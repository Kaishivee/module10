from threading import Thread, Lock

class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdrew(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrew {amount}, new balance is {self.balance}')
            if self.balance < amount:
                print(f'You have not enough money on your bank account')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdrew(amount)


account = BankAccount(1000)

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdrew_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdrew_thread.start()

deposit_thread.join()
withdrew_thread.join()
