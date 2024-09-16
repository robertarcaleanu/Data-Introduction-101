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
        df = self.datasets.article_views_1()
        df = df[df["author_id"]  == df["viewer_id"]]
        df = df.drop_duplicates(subset=["author_id"])

        return df
    def invalid_tweets(self) -> pd.DataFrame:
        df = self.datasets.invalid_tweets()
        df["tweet_len"] = df[df["content"].str.len()]
        df = df[df["tweet_len"] > 15][["tweet_id"]]

        return df
    
    def calculate_special_bonus(self) -> pd.DataFrame:
        df = self.datasets.calculate_special_bonus()
        df["id_is_odd"] = df["employee_id"] % 2  # Create s column - Check if number is odd (0 is even, 1 is odd)
        df["name_starts_with_m"] = df["name"].str.startswith("M") #  Create s column - Check if name starts with M
        df.loc[(df["id_is_odd"] == True) & (df["name_starts_with_m"] == False), "bonus"] = df["salary"] # if number is odd and name does not starts with M, we create a column bonus which equal to the salary
        df["bonus"] = df["bonus"].fillna(0)  # fill NaN values with 0

        return df
    
    def fix_names(self) -> pd.DataFrame:
        df = self.datasets.fix_names_in_table()
        df["name"] = df["name"].str.capitalize()
        
        return df
    
    def valid_email(self) -> pd.DataFrame:
        pass

    def find_patients(self) -> pd.DataFrame:
        pass


