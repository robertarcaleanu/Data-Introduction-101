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
        df = df[(df["area"] >= 3e6) | (df["population"] >= 25000000)]
        df = df[["name", "population", "area"]]

        return df

    def find_products(self) -> pd.DataFrame:
        df = self.datasets.recyclable_and_low_fat_products()

        return df[(df["low_fats"] == "Y") & (df["recyclable"] == "Y")][["product_id"]]
    
    def find_customers(self) -> pd.DataFrame:
        customers, orders = self.datasets.customers_who_never_order()
        
        df = customers[~customers["id"].isin(orders["customer_id"])]
        df = df.rename(columns={"name": "Customers"})
        df = df[["Customers"]]

        return df
    
    def article_views(self) -> pd.DataFrame:
        df = self.datasets.article_views_1()
        df = df[df["author_id"]  == df["viewer_id"]]
        df = df.drop_duplicates(subset=["author_id"])

        df = df[["author_id"]]
        df.columns = ["id"]

        return df
    def invalid_tweets(self) -> pd.DataFrame:
        df = self.datasets.invalid_tweets()
        df["tweet_len"] = df["content"].str.len()
        df = df[df["tweet_len"] > 15][["tweet_id"]]

        return df
    
    def calculate_special_bonus(self) -> pd.DataFrame:
        df = self.datasets.calculate_special_bonus()
        df["id_is_odd"] = df["employee_id"] % 2  # Create s column - Check if number is odd (0 is even, 1 is odd)
        df["name_starts_with_m"] = df["name"].str.startswith("M") #  Create s column - Check if name starts with M
        df.loc[(df["id_is_odd"] == True) & (df["name_starts_with_m"] == False), "bonus"] = df["salary"] # if number is odd and name does not starts with M, we create a column bonus which equal to the salary
        df["bonus"] = df["bonus"].fillna(0)  # fill NaN values with 0

        df = df[["employee_id", "bonus"]]

        return df
    
    def fix_names(self) -> pd.DataFrame:
        df = self.datasets.fix_names_in_table()
        df["name"] = df["name"].str.capitalize()
        
        return df
    
    def valid_email(self) -> pd.DataFrame:
        pass

    def find_patients(self) -> pd.DataFrame:
        df = self.datasets.patients_with_a_condition()
        solution = df.copy()
        df["conditions"] = df["conditions"].str.split(" ")
        df = df.explode("conditions")
        patients_with_type_1_diab = df[df["conditions"].str.startswith("DIAB1")]
        patients_with_type_1_diab["patient_id"]
        solution = solution[solution["patient_id"].isin(patients_with_type_1_diab["patient_id"])]

        return solution

    def nth_highest_salary(self, N: int = 1) -> pd.DataFrame:
        df = self.datasets.nth_highest_salary()
        df = df.sort_values("Salary").reset_index()

        col_name = f"getNthHighestSalary({N})"
        if N > df.shape[0]:
            solution = pd.DataFrame({col_name: [None]})
        else:
            salary = df.iloc[N-1]["Salary"]
            solution = pd.DataFrame({col_name: [salary]})

        return solution 

    def second_highest_salaty(self) -> pd.DataFrame:
        df = self.datasets.second_highest_salary()
        df = df.sort_values("salary")
        df = df.drop_duplicates("salary").reset_index()
        N = 2

        col_name = f"SecondHighestSalary "
        if N > df.shape[0]:
            solution = pd.DataFrame({col_name: [None]})
        else:
            salary = df.iloc[N-1]["salary"]
            solution = pd.DataFrame({col_name: [salary]})

        return solution
    
    def department_highest_salary(self) -> pd.DataFrame:
        employee, department = self.datasets.department_highest_salary()
        df = employee.copy()
        df["max_salary_dep"] = df.groupby("departmentId")["salary"].transform("max")
        df = df[df["salary"] == df["max_salary_dep"]]

        department = department.rename(columns={"id": "departmentId", "name": "Department"})
        df = pd.merge(
            df,
            department,
            how="inner",
            on="departmentId"
        )
        df = df.rename(columns={"name": "Employee", "salary": "Salary"})
        df = df[["Department", "Employee", "Salary"]]
        
        return df

        



