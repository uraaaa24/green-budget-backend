from unittest.mock import MagicMock
import pytest
from app.usecases.category_usecase import CategoryUsecase


@pytest.fixture
def mock_repository():
    return MagicMock()


@pytest.fixture
def category_usecase(mock_repository):
    usecase = CategoryUsecase(db=None)
    usecase.repository = mock_repository
    return usecase


def test_get_categories(category_usecase, mock_repository):
    # Arrange
    user_id = "user_id"
    mock_repository.find_all.return_value = ["Category 1", "Category 2"]

    # Act
    result = category_usecase.get_categories(user_id)

    # Assert
    assert result == ["Category 1", "Category 2"]
    mock_repository.find_all.assert_called_once_with(user_id)
