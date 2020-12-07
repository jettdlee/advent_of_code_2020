class ImportData:
    def __init__(self, fileName, convert_to_int=False):
        with open(fileName, 'r') as f:
            self.dataset = []
            for line in f:
                result = self.__convertLine(line, convert_to_int)
                self.dataset.append(result)
    
    def __convertLine(self, line, convert_to_int):
        result = line
        result = result.strip('\n')
        if convert_to_int == True:
            result = int(result)
        return result

