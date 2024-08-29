from typing import Tuple

import pandas as pd
import polars as pl


class DatasetLeetcode:
    def __init__(self):
        """
        Constructor method.
        """
        pass

    def dummy_data(self) -> pd.DataFrame:
        dummy_df = pd.DataFrame(
            {
                "a": [1, 2, 3],
                "b": [4, 5, 6],
                "c": [7, 8, 9],
            }
        )
        return dummy_df

    def big_countries(self) -> pd.DataFrame:
        """
        Load the big countries dataset into a Pandas DataFrame.

        Returns:
            pd.DataFrame: The big countries dataset.
        """
        data = [
            ["Afghanistan", "Asia", 652230, 25500100, 20343000000],
            ["Albania", "Europe", 28748, 2831741, 12960000000],
            ["Algeria", "Africa", 2381741, 37100000, 188681000000],
            ["Andorra", "Europe", 468, 78115, 3712000000],
            ["Angola", "Africa", 1246700, 20609294, 100990000000],
        ]
        df = pd.DataFrame(
            data, columns=["name", "continent", "area", "population", "gdp"]
        )
        df = df.astype(
            {
                "name": "object",
                "continent": "object",
                "area": "Int64",
                "population": "Int64",
                "gdp": "Int64",
            }
        )

        return df

    def recyclable_and_low_fat_products(self) -> pd.DataFrame:
        """Load a DataFrame with product_id, low_fats, and recyclable columns."""
        data = [
            ["0", "Y", "N"],
            ["1", "Y", "Y"],
            ["2", "N", "Y"],
            ["3", "Y", "Y"],
            ["4", "N", "N"],
        ]
        df = pd.DataFrame(
            data, columns=["product_id", "low_fats", "recyclable"]
        ).astype(
            {"product_id": "int64", "low_fats": "category", "recyclable": "category"}
        )

        return df

    def customers_who_never_order(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load the customers and orders datasets into a tuple of two Pandas DataFrames.

        Returns:
            tuple: A tuple of two DataFrames, customers and orders.
        """
        customers_data = [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]]
        customers_df = pd.DataFrame(customers_data, columns=["id", "name"]).astype(
            {"id": "Int64", "name": "object"}
        )

        orders_data = [[1, 3], [2, 1]]
        orders_df = pd.DataFrame(orders_data, columns=["id", "customer_id"]).astype(
            {"id": "Int64", "customer_id": "Int64"}
        )

        return customers_df, orders_df
