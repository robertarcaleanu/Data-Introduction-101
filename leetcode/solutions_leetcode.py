import pandas as pd
from datasets_leetcode import DatasetLeetcode


class SolutionsLeetcode:
    def __init__(self, DatasetLeetcode: DatasetLeetcode):
        """
        Constructor method.
        """
        self.datasets = DatasetLeetcode

    def dummy_data(self) -> pd.DataFrame:
        df = self.datasets.dummy_data()
        return df[df["a"] == 1]

    def big_countries(self) -> pd.DataFrame:
        df = self.datasets.big_countries()

        return df[(df["area"] >= 3e6) | (df["population"] >= 25000000)]
