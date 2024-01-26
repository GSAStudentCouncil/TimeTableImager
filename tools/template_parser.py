from tools.subject_name_finder import name_finder

class Template:
    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        f = open(self.path, 'r', encoding='utf-8')
        lines = f.readlines()
        self.temp_height = len(lines)
        self.temp_width = 0
        for i in range(self.temp_height):
            lines[i] = lines[i].replace('\n', '')
            self.temp_width = max(self.temp_width, len(lines[i].split(',')))
        self.temp = [[None for _ in range(self.temp_width)] for _ in range(self.temp_height)]
        for i in range(self.temp_height):
            line = lines[i].split(',')
            for j in range(len(line)):
                self.temp[i][j] = line[j].strip()
        f.close()

    def parser(self, cell_data : list):
        if len(cell_data) != self.temp_height:
            raise ValueError('cell_data height is not match with template height')
        elif len(cell_data[0]) != self.temp_width:
            raise ValueError('cell_data width is not match with template width')
        result = {}
        for i in range(self.temp_height):
            for j in range(self.temp_width):
                if self.temp[i][j] != None and self.temp[i][j] != '':
                    result[self.temp[i][j]] = name_finder(cell_data[i][j].value)
        return result