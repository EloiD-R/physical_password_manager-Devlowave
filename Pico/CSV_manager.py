
import os
import glob
import time


class Manager:

    def __init__(self):
        # init the variable cause else program don't work
        self.there_is_a_CSV = False
        # check is there is a csv_file in the pico
        while not self.there_is_a_CSV:
            self.check_for_CSV()
            if self.there_is_a_CSV:
                break
            else:
                time.sleep(1)
        # then check if the file is a firefox exported CSV
        self.CSV_name = self.get_CSV_name()
        if self.CSV_name == "logins" or self.CSV_name == "identifiants":
            print("a")
        else:
            print("b")

    def check_for_CSV(self):
        self.there_is_a_CSV = bool(glob.glob("*.csv"))

    def get_CSV_name(self):
        # get every file with csv extension in a list
        CSV_files = glob.glob('*.csv')
        # make the list into a single string
        CSV_files = CSV_files[0]
        # get only the name (without extension)
        file_name, file_extension = os.path.splitext(CSV_files)
        # return the formatted file_name
        return file_name
