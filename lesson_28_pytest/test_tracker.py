import pytest


def test_tracker_creation(tracker):
    assert tracker.transactions == []


def test_add_income(tracker):
    tracker.add_transaction(1000, "income")
    assert len(tracker.transactions) == 1


def test_add_expense(tracker):
    tracker.add_transaction(500, "expense")
    assert len(tracker.transactions) == 1


def test_income_amount_saved(tracker):
    tracker.add_transaction(1000, "income")
    assert tracker.transactions[0]["amount"] == 1000


def test_negative_amount_raises_error(tracker):
    with pytest.raises(ValueError):
        tracker.add_transaction(-100, "income")


def test_zero_amount_raises_error(tracker):
    with pytest.raises(ValueError):
        tracker.add_transaction(0, "income")


def test_delete_transaction(tracker):
    tracker.add_transaction(500, "income")
    tracker.delete_transaction(0)
    assert len(tracker.transactions) == 0


def test_delete_invalid_transaction(tracker):
    with pytest.raises(IndexError):
        tracker.delete_transaction(0)


def test_calculate_balance_income_only(tracker):
    tracker.add_transaction(1000, "income")
    assert tracker.calculate_balance() == 1000


def test_calculate_balance_expense_only(tracker):
    tracker.add_transaction(300, "expense")
    assert tracker.calculate_balance() == -300


def test_calculate_balance_mixed(tracker):
    tracker.add_transaction(1000, "income")
    tracker.add_transaction(200, "expense")
    assert tracker.calculate_balance() == 800


def test_monthly_report(tracker):
    tracker.add_transaction(100, "income")
    tracker.add_transaction(50, "expense")
    assert tracker.monthly_report() == 2