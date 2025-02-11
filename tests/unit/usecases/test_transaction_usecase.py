from decimal import Decimal
from unittest.mock import MagicMock
import uuid
import pytest

from app.domain.models.transaction import PostTransaction
from app.usecases.transaction_usecase import TransactionUsecase


@pytest.fixture
def mock_repository():
    return MagicMock()


@pytest.fixture
def transaction_usecase(mock_repository):
    usecase = TransactionUsecase(db=None)
    usecase.repository = mock_repository
    return usecase


def test_create_transaction_with_valid_income_data(
    transaction_usecase, mock_repository
):
    # Arrange
    user_id = uuid.uuid4()
    transaction_data = PostTransaction(
        user_id=user_id,
        category_id="101",
        amount=100.50,
        transaction_type="income",
        date="2021-01-01",
        note="New Transaction",
    )
    mock_repository.insert.return_value = "New Transaction"

    # Act
    result = transaction_usecase.create_transaction(transaction_data)

    # Assert
    assert result == "New Transaction"
    mock_repository.insert.assert_called_once()
    args, _ = mock_repository.insert.call_args
    assert args[0].user_id == user_id
    assert args[0].category_id == 101
    assert args[0].amount.value == Decimal("100.50")
    assert args[0].transaction_type.value == "income"
    assert args[0].date.strftime("%Y-%m-%d") == "2021-01-01"
    assert args[0].note == "New Transaction"


def test_create_transaction_with_valid_expense_data(
    transaction_usecase, mock_repository
):
    # Arrange
    user_id = uuid.uuid4()
    transaction_data = TransactionCreate(
        user_id=user_id,
        category_id="101",
        amount=100.50,
        transaction_type="expense",
        date="2021-01-01",
        note="New Transaction",
    )
    mock_repository.insert.return_value = "New Transaction"

    # Act
    result = transaction_usecase.create_transaction(transaction_data)

    # Assert
    assert result == "New Transaction"
    mock_repository.insert.assert_called_once()
    args, _ = mock_repository.insert.call_args
    assert args[0].user_id == user_id
    assert args[0].category_id == 101
    assert args[0].amount.value == Decimal("100.50")
    assert args[0].transaction_type.value == "expense"
    assert args[0].date.strftime("%Y-%m-%d") == "2021-01-01"
    assert args[0].note == "New Transaction"


def test_create_transaction_missing_user_id():
    # Arrange
    invalid_data = {
        "user_id": None,
        "category_id": 101,
        "amount": 100.50,
        "transaction_type": "income",
        "date": "2021-01-01",
        "note": "New Transaction",
    }

    # Act / Assert
    with pytest.raises(
        ValueError, match="UUID input should be a string, bytes or UUID object"
    ):
        TransactionCreate(**invalid_data)


def test_get_transactions(transaction_usecase, mock_repository):
    # Arrange
    mock_repository.find_all.return_value = ["Transaction 1", "Transaction 2"]

    # Act
    result = transaction_usecase.get_transactions()

    # Assert
    assert result == ["Transaction 1", "Transaction 2"]
    mock_repository.find_all.assert_called_once()
