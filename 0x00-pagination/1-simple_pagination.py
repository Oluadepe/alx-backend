#!/usr/bin/env python3
# Function take two interger arguements with default value 1 and 10

import csv
import math
from typing import List

def index_range(page, page_size):
    """ return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters. """
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Initialize instance. '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Return page of dataset. '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []
