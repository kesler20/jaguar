
import os
from path import Path
import unittest
from file import OperatingSystemInterface, File

print("Testing:" + OperatingSystemInterface.__doc__)
        
class Test_OperatingSystemInterface(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self) -> None:
        pass

    def test___enter__(self) -> None:
        '''signature description'''
        pass
    
    def test___exit__(self) -> os:
        '''signature description'''
        pass
    
    def test_move_folder_files(self) -> None:
        '''signature description'''
        pass
    
    def test_read_word_in_directory(self) -> Path:
        '''signature description'''
        pass
    
    def test_get_files_from_directory(self) -> File:
        '''signature description'''
        pass
    def tearDown(self):
        pass
        

class Test_File(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self) -> None:
        pass

    def test_read(self) -> str:
        '''signature description'''
        pass
    
    def test_write(self) -> None:
        '''signature description'''
        pass
    
    def test_readlines(self) -> 'list[str]':
        '''signature description'''
        pass
    
    def test_writeline(self) -> None:
        '''signature description'''
        pass
    
    def test_delete_line_by_condition(self) -> None:
        '''signature description'''
        pass
    
    def test_delete_line_by_condition(self) -> None:
        '''signature description'''
        pass
    
    def test_delete(self) -> None:
        '''signature description'''
        pass
    
    def test_read_line_by_condition(self) -> 'list[str]':
        '''signature description'''
        pass
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        