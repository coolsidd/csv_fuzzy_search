import sys
import os
import csv
import string_distance


class CsvSearcher:

    calculate_dl_distance = True

    def __init__(self, csv_file, line_no=False, load_all=True, is_sorted=False,
                 exclude_rows=()):
        pass

    def search(self, key, out_buffer=sys.stdout, return_line_no=True):
        pass

    @staticmethod
    def matchness(key, other_string):
        return 1-string_distance.osa_distance(key.lower(), other_string.lower())/max(len(key), len(other_string))


if __name__ == "__main__":
    pass
