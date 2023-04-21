#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert isinstance(index, int) and index >= 0 and index < 1000
        get_indexed_data = self.indexed_dataset()
        ind = index
        data = []
        p = page_size
        while p > 0:
            if ind not in get_indexed_data:
                while True:
                    ind += 1
                    if ind in get_indexed_data:
                        break
            data.append(get_indexed_data[ind])
            ind += 1
            p -= 1
        next_index = ind

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
