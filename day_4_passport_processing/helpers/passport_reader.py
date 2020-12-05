class PassportReader:
    def __init__(self, dataset):
        self.dataset = dataset
        self.passports = []

    def processPassports(self):
        passport = {}
        for line in self.dataset:
            if len(line) == 0:
                self.passports.append(passport)
                passport = {}
                continue

            passport = self.__processPassportData(line, passport)
        self.passports.append(passport)

    def __processPassportData(self, line, passport):
        split_line = line.split(" ")
        for data_entry in split_line:
            split_key_value = data_entry.split(":")
            passport[split_key_value[0]] = split_key_value[1]
        return passport

