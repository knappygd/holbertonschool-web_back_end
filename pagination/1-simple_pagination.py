from typing import Tuple
import csv
import math
from typing import List


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
        assert type(page) is int and type(page_size) is int
        assert page > 0
        assert page_size > 0
        p = index_range(page, page_size)
        self.dataset()
        return self.__dataset[p[0]:p[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple."""
    start = page * page_size - page_size
    end = start + page_size
    return (start, end)
