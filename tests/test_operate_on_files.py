import unittest
from unittest.mock import mock_open, patch
from src.operate_on_files import FileOperations


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.temp = FileOperations()

    def test_read_files(self):
        with patch('builtins.open', mock_open(read_data='some_data')) as mocked_file:
            self.assertEqual(self.temp.read_files('/fake/file/path.txt'), 'some_data')
            mocked_file.assert_called_with('/fake/file/path.txt', 'r')

    def test_write_files(self):
        with patch('builtins.open', mock_open(read_data='some_data')) as mocked_file:
            self.temp.write_files('/fake/file/path.txt', 'new_data')
            mocked_file.assert_called_with('/fake/file/path.txt', 'w')

    @patch('os.path.isfile')
    @patch('os.remove')
    def test_delete_file_exists(self, mock_isfile, mock_remove):
        mock_isfile.return_value = True
        self.temp.delete_files('/fake/file/path.txt')
        mock_remove.assert_called_with('/fake/file/path.txt')

    @patch('os.path.isfile')
    def test_delete_file_doesnt_exist(self, mock_isfile):
        mock_isfile.return_value = False
        with self.assertRaises(Exception):
            self.temp.delete_files('/fake/file/path.txt')

    def tearDown(self):
        self.temp = None
