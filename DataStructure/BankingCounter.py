"""
Using Queue Data Structure :
Create a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.
"""


class Queue:
    def __init__(self):
        self.balance = 0
        print("Welcome .....")
        print("This is a Banking portal")

    def enqueue_deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def dequeue_withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance ")

    def queue_display(self):
        print("\nNet Available Balance=", self.balance)

    def queue_exit(self):
        exit()


if __name__ == '__main__':
    q = Queue()
    while True:
        print("Please Enter the option that you want to make a transaction:")
        n = int(input(
            " Press \n 1. Deposite Amount to the account \n 2. Withdraw Amount from the account \n "
            "3. Display the amount \n 4. Cancel Transaction \n"))
        if n == 1:
            q.enqueue_deposit()
        elif n == 2:
            q.dequeue_withdraw()
        elif n == 3:
            q.queue_display()
        elif n == 4:
            q.queue_exit()
