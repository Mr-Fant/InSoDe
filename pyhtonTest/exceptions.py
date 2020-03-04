class SectionNotFound(Exception):    
    text = ''

    def __init__(self):
        self.text = 'Section is not found'

class ErrorReadFile(Exception):
    text = ''

    def __init__(self):
        self.text = 'Error read file'

class InvalidTypeFile(Exception):
    text = ''

    def __init__(self):
        self.text = 'Invalid type file'

class AnotherType(Exception):
    text = ''

    def __init__(self):
        self.text = 'Another type'

class KeyNotFound(Exception):
    text = ''

    def __init__(self):
        self.text = 'Key not found'