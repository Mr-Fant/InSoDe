import handlerFileINI
import exceptions
import unittest

class testCreate(unittest.TestCase):
    def test_file_name_exception(self):
        self.assertRaises(exceptions.InvalidTypeFile, handlerFileINI.HandlerFileINI, 'test.io')
    
    def test_read_file_exception(self):
        self.assertRaises(exceptions.ErrorReadFile, handlerFileINI.HandlerFileINI, 'testhjavdsu.ini')

if __name__ == '__main__':
    unittest.main()