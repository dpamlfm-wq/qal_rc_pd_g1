class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, transaction_type):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.transactions.append(
            {
                "amount": amount,
                "type": transaction_type
            }
        )

    def delete_transaction(self, index):
        if index < 0 or index >= len(self.transactions):
            raise IndexError("Transaction not found")

        self.transactions.pop(index)

    def calculate_balance(self):
        balance = 0

        for transaction in self.transactions:
            if transaction["type"] == "income":
                balance += transaction["amount"]
            else:
                balance -= transaction["amount"]

        return balance

    def monthly_report(self):
        return len(self.transactions)