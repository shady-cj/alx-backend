#!/usr/bin/env python3
"""
Implementing an hypermedia pagination
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """
        getting the page based on start and end index returned from
        index_range()
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a dictionary containing information about
        the requested page.
        """
        data = self.get_page(page, page_size)
        total_data = self.dataset()
        total_pages = len(total_data) // page_size
        prev_page = None if page == 1 else page - 1
        next_page = None if page >= total_pages else page + 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start
    index and an end index corresponding
    to the range of indexes to return in a
    list for those particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
