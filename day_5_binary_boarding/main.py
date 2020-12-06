from helpers.import_data import ImportData
import numpy as np
import re
import pdb

class TicketChecker:
    def __init__(self, dataset):
        self.dataset = dataset

    def getSeatingDetails(self, seating_range, column_range):
        seatings = []
        for line in self.dataset:
            seating = {}
            partitioning = re.findall("(\w{7}|\w{3}$)", line)
            seating['ticket'] = line
            seating['row'] = self.__get_seating_row(seating_range, partitioning[0])
            seating['column'] = self.__get_column(column_range, partitioning[1])
            seating['seat_id'] = self.__get_seat_id(seating)
            seatings.append(seating)
        return seatings

    def __get_seating_row(self, seating_array, row_string):
        seat_row = seating_array
        for seating_char in row_string:
            seating_range = int((len(seat_row) / 2))
            if len(seat_row) == 2:
                if seating_char == "B":
                    seat_row = seat_row[1]
                else:
                    seat_row = seat_row[0]
                break
            elif seating_char == "B":
                seat_row = seat_row[seating_range:]
            else: 
                seat_row = seat_row[:seating_range]
        return seat_row

    def __get_column(self, column_array, column_string):
        column = column_array
        for column_char in column_string:
            column_slice = int((len(column) / 2))
            if len(column) == 2:
                if column_char == "R":
                    column = column[1]
                else:
                    column = column[0]
                break
            elif column_char == "R":
                column = column[column_slice:]
            else:
                column = column[:column_slice]
        return column
    
    def __get_seat_id(self, seating):
        return seating['row'] * 8 + seating['column']

if __name__ == '__main__':
    seating_range = np.array(range(128))
    column_range = np.array(range(8))
    data_file = ImportData('dataset.data')
    checker = TicketChecker(data_file.dataset)
    results = checker.getSeatingDetails(seating_range, column_range)
    seat_id_array = []
    print(len(data_file.dataset))
    print(len(results))
    for result in results:
        if result['seat_id'] == 826:
            print(result)
        seat_id_array.append(result['seat_id'])
    print(np.amax(np.array(seat_id_array)))
