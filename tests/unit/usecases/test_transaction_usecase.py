from unittest.mock import MagicMock
import pytest

from app.usecases.transaction_usecase import TransactionUsecase


@pytest.fixture
def mock_repository():
    return MagicMock()


@pytest.fixture
def transaction_usecase(mock_repository):
    usecase = TransactionUsecase(db=None)
    usecase.repository = mock_repository
    return usecase


def test_get_transactions(transaction_usecase, mock_repository):
    # Arrange
    mock_repository.find_all.return_value = ["Transaction 1", "Transaction 2"]

    # Act
    result = transaction_usecase.get_transactions()

    # Assert
    assert result == ["Transaction 1", "Transaction 2"]
    mock_repository.find_all.assert_called_once()
