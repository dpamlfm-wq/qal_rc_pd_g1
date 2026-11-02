import pytest
from models import ExpenseTracker


@pytest.fixture
def tracker():
    return ExpenseTracker()