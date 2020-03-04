import exceptions

class Section:
    Name = ''
    Data = {}

    def __init__(self, name, data = {}):
        """Constructor section class
        
        Arguments:
            name {string} -- name section
        
        Keyword Arguments:
            data {dict} -- data in section (default: {{}})
        """        
        self.Name = name
        self.Data = data 
    
    def AddData(self, data):
        """Add data to section
        
        Arguments:
            data {dict} -- new data
        """        
        self.Data.update(data)
    
    def Find(self, key):
        """Find value in section by key 
        
        Arguments:
            key {string} -- key name
        
        Raises:
            exceptions.KeyNotFound: not found key
        
        Returns:
            string -- data
        """        
        try:
            return self.Data[key]
        except:
            raise exceptions.KeyNotFound
    
    def PrintSection(self):
        """Print section
        """        
        print()
        print('--------------')
        print('Print section', self.Name)
        print('Data:')
        for item in self.Data:
            print(item, ':', self.Data[item])
        print('--------------')
        print()
    
    
