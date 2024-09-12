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

    def find_products(self) -> pd.DataFrame:
        df = self.datasets.recyclable_and_low_fat_products()

        return df[(df["low_fats"] == "Y") & (df["recyclable"] == "Y")][["product_id"]]
    
    def article_views(self) -> pd.DataFrame:
        customers, orders = self.datasets.customers_who_never_order()
        solution = customers[~customers["id"].isin(orders["customer_id"])][["name"]]
        solution = solution.rename(columns={"name": "Customers"})

        return solution
