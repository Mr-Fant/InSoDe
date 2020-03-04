import os
import copy
import exceptions
import section

class HandlerFileINI:
    fileName = ''
    Sections = []

    def save_file(self, pathFile):
        f = open('test1.ini', 'w')
        for i in self.Sections
            f.write('[', name,']')
            for j in i.Data
                f.write(j.key, ' = ', j.value) 


    def add_value(self, id_section, key, value):
        self.Sections[id_section].AddData({key: value})
    
    def delete_value(self, id_section, key):
        del self.Sections[id_section].Data[key]

    def del_allKeys_inSection(self, id_section):
        self.Sections[id_section].Data = []

    def read_file(self, pathFile):
        """Constructor class
        
        Arguments:
            pathFile {string} -- path to file ini
        
        Raises:
            exceptions.InvalidTypeFile: invalid type file
            exceptions.ErrorReadFile: error read file
        """        
        self.fileName = pathFile
        name, ext = os.path.splitext(pathFile)
        if(ext != '.ini'):
            raise exceptions.InvalidTypeFile
        else:
            try:
                file = open(self.fileName, 'r')
                lines = file.readlines()
                for line in lines:
                    line = line.strip(' ').strip('\n')
                    flag = True
                    if(line[0] == '['):
                                                                       
                        line = line[1:-1]
                        self.Sections.append(section.Section(line))
                        flag = False
                    else:
                        if(flag and line != '' and line[0] != ';'):
                            data = line.replace(' ', ';').replace('=', ';').split(';')
                            data = list(filter(None, data))
                            if(len(self.Sections) > 0 and len(data) >= 2):
                                self.Sections[-1].AddData({data[0] : data[1]})
            except:
                raise exceptions.ErrorReadFile
    
    def GetValue(self, sectionName, key):
        """Function for get value from ini file
        
        Arguments:
            sectionName {string} -- section name
            key {string} -- key in section
        
        Raises:
            exceptions.SectionNotFound: not found section
        
        Returns:
            string -- value
        """        
        mySection = None
        for item in self.Sections:
            if(item.Name == sectionName):
                mySection = item 
        if(mySection):
            return mySection.Find(key)
        else:
            raise exceptions.SectionNotFound
    
    def PrintAll(self):
        """Print all file
        """        
        for item in self.Sections:
            item.PrintSection()
    
    def 