import os
import shutil
import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
from utils.file_manager import FileManager
from utils.formatters import DateTimeFormatter

@pytest.fixture
def mock_formatter():
    formatter = Mock(spec=DateTimeFormatter)
    formatter.day.return_value = "05-07-2025"
    formatter.time.return_value = "19-00"

    return formatter

@pytest.fixture
def file_manager(mock_formatter):
    return FileManager("./remindme", mock_formatter)

@patch('utils.file_manager.os.path.exists')
@patch('utils.file_manager.os.mkdir')
def test_mkdir(mock_mkdir, mock_exists, file_manager):
    mock_exists.return_value = False
    
    file_manager.mkdir()
    
    mock_mkdir.assert_called_once_with("./remindme")
    mock_exists.assert_called_once_with("./remindme")


@patch('utils.file_manager.os.path.exists')
@patch('builtins.open', create=True)
def test_file_creation(mock_open, mock_exists, file_manager):
    """Тест создания файла с мокингом"""
    mock_exists.return_value = False
    mock_file = MagicMock()
    mock_open.return_value.__enter__.return_value = mock_file
    
    file_manager.create_file()
    
    mock_open.assert_called_once_with("./remindme/05-07-2025.txt", "w")
    mock_file.write.assert_called_once_with("")

@patch('builtins.open', create=True)
def test_write(mock_open, file_manager):
    """Тест записи с мокингом"""
    mock_file = MagicMock()
    mock_open.return_value.__enter__.return_value = mock_file
    
    idea = "Implement convolution"
    file_manager.write(idea)
    
    mock_open.assert_called_once_with("./remindme/05-07-2025.txt", "a")
    mock_file.write.assert_called_once_with(f"19-00 | {idea}\n")
