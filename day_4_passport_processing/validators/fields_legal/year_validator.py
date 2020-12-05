class YearValidator
    def __init__(self, lower_year, upper_year):
        self.__lower_year = lower_year
        self.__upper_year = upper_year

    def validate(self, value):
       return int(value) >= self.__lower_year and int(value) <= self.__upper_year 
