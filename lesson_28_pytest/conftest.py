import pytest
import logging
from source import BankAccount
from models import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

@pytest.fixture()
def one_000_account():
    acc = BankAccount(1000)
    yield acc
    del acc


from models import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()