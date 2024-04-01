#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia pagination information for a specific index
        """
        assert index is None or index >= 0, "Index must be non-negative"

        dataset = self.indexed_dataset()
        dataset_length = len(dataset)

        if index is None:
            index = 0

        if index >= dataset_length:
            return {
                'index': index,
                'data': [],
                'page_size': page_size,
                'next_index': None
            }

        # Adjust index to account for deleted items
        while index < dataset_length and index not in dataset:
            index += 1

        if index >= dataset_length:
            return {
                'index': index,
                'data': [],
                'page_size': page_size,
                'next_index': None
            }

        end_index = min(index + page_size, dataset_length)
        next_index = end_index if end_index < dataset_length else None

        return {
            'index': index,
            'data': [dataset[i] for i in range(index, end_index)],
            'page_size': page_size,
            'next_index': next_index
        }
