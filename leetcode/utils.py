import sqlite3

import pandas as pd


class SQLQuery:
    def __init__(self, query: str, dfs: dict) -> None:
        self.query = query
        self.dfs = dfs

    def load_data(self):
        conn = sqlite3.connect("test.db")
        for df_name in self.dfs.keys():
            df = self.dfs[df_name]
            df.to_sql(df_name, conn, if_exists="replace", index=False)

    def execute_query(self):
        self.load_data()
