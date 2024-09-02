from typing import Tuple

import pandas as pd


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

    def article_views_1(self) -> pd.DataFrame:
        """
        Load the article_views_1 dataset into a Pandas DataFrame.

        Returns:
            pd.DataFrame: The article_views_1 dataset.
        """
        data = [
            [1, 3, 5, "2019-08-01"],
            [1, 3, 6, "2019-08-02"],
            [2, 7, 7, "2019-08-01"],
            [2, 7, 6, "2019-08-02"],
            [4, 7, 1, "2019-07-22"],
            [3, 4, 4, "2019-07-21"],
            [3, 4, 4, "2019-07-21"],
        ]
        article_views_df = pd.DataFrame(
            data, columns=["article_id", "author_id", "viewer_id", "view_date"]
        ).astype(
            {
                "article_id": "Int64",
                "author_id": "Int64",
                "viewer_id": "Int64",
                "view_date": "datetime64[ns]",
            }
        )

        return article_views_df

    def invalid_tweets(self) -> pd.DataFrame:
        """
        Load the invalid_tweets dataset into a Pandas DataFrame.

        Returns:
            pd.DataFrame: The invalid_tweets dataset.
        """
        data = [[1, "Vote for Biden"], [2, "Let us make America great again!"]]
        tweets = pd.DataFrame(data, columns=["tweet_id", "content"]).astype(
            {"tweet_id": "Int64", "content": "object"}
        )

        return tweets

    def calculate_special_bonus(self) -> pd.DataFrame:
        """
        Load the special_bonus dataset into a Pandas DataFrame.

        Returns:
            pd.DataFrame: The special_bonus dataset.
        """
        data = [
            [2, "Meir", 3000],
            [3, "Michael", 3800],
            [7, "Addilyn", 7400],
            [8, "Juan", 6100],
            [9, "Kannon", 7700],
        ]
        employees = pd.DataFrame(
            data, columns=["employee_id", "name", "salary"]
        ).astype({"employee_id": "int64", "name": "object", "salary": "int64"})

        return employees

    def fix_names_in_table(self) -> pd.DataFrame:
        """
        Load the users dataset into a Pandas DataFrame.

        Returns:
            pd.DataFrame: The users dataset.
        """
        data = [[1, "aLice"], [2, "bOB"]]
        users = pd.DataFrame(data, columns=["user_id", "name"]).astype(
            {"user_id": "Int64", "name": "object"}
        )

        return users

    def find_users_with_valid_emails(self):
        data = [
            [1, "Winston", "winston@leetcode.com"],
            [2, "Jonathan", "jonathanisgreat"],
            [3, "Annabelle", "bella-@leetcode.com"],
            [4, "Sally", "sally.come@leetcode.com"],
            [5, "Marwan", "quarz#2020@leetcode.com"],
            [6, "David", "david69@gmail.com"],
            [7, "Shapiro", ".shapo@leetcode.com"],
        ]

        users = pd.DataFrame(data, columns=["user_id", "name", "mail"]).astype(
            {"user_id": "int64", "name": "object", "mail": "object"}
        )

        return users

    def patients_with_a_condition(self):
        data = [
            [1, "Daniel", "YFEV COUGH"],
            [2, "Alice", ""],
            [3, "Bob", "DIAB100 MYOP"],
            [4, "George", "ACNE DIAB100"],
            [5, "Alain", "DIAB201"],
        ]

        patients = pd.DataFrame(
            data, columns=["patient_id", "patient_name", "conditions"]
        ).astype(
            {"patient_id": "int64", "patient_name": "object", "conditions": "object"}
        )

        return patients

    def nth_highest_salary(self):
        data = [[1, 100], [2, 200], [3, 300]]

        employee = pd.DataFrame(data, columns=["Id", "Salary"]).astype(
            {"Id": "Int64", "Salary": "Int64"}
        )

        return employee

    def second_highest_salary(self):
        data = [[1, 100], [2, 200], [3, 300]]

        employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
            {"id": "int64", "salary": "int64"}
        )

        return employee

    def department_highest_salary(self):
        data = [
            [1, "Joe", 70000, 1],
            [2, "Jim", 90000, 1],
            [3, "Henry", 80000, 2],
            [4, "Sam", 60000, 2],
            [5, "Max", 90000, 1],
        ]
        employee = pd.DataFrame(
            data, columns=["id", "name", "salary", "departmentId"]
        ).astype(
            {
                "id": "Int64",
                "name": "object",
                "salary": "Int64",
                "departmentId": "Int64",
            }
        )

        data = [[1, "IT"], [2, "Sales"]]
        department = pd.DataFrame(data, columns=["id", "name"]).astype(
            {"id": "Int64", "name": "object"}
        )

        return employee, department

    def rank_scores(self):
        data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
        scores = pd.DataFrame(data, columns=["id", "score"]).astype(
            {"id": "Int64", "score": "Float64"}
        )

        return scores

    def delete_duplicate_emails(self):
        data = [
            [1, "john@example.com"],
            [2, "bob@example.com"],
            [3, "john@example.com"],
        ]
        person = pd.DataFrame(data, columns=["id", "email"]).astype(
            {"id": "int64", "email": "object"}
        )

        return person

    def rearrange_products_table(self):
        data = [[0, 95, 100, 105], [1, 70, None, 80]]
        products = pd.DataFrame(
            data, columns=["product_id", "store1", "store2", "store3"]
        ).astype(
            {
                "product_id": "Int64",
                "store1": "Int64",
                "store2": "Int64",
                "store3": "Int64",
            }
        )

        return products

    def count_salary_categories(self):
        data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
        accounts = pd.DataFrame(data, columns=["account_id", "income"]).astype(
            {"account_id": "Int64", "income": "Int64"}
        )

        return accounts

    def find_total_time_spent_by_each_employee(self):
        data = [
            ["1", "2020-11-28", "4", "32"],
            ["1", "2020-11-28", "55", "200"],
            ["1", "2020-12-3", "1", "42"],
            ["2", "2020-11-28", "3", "33"],
            ["2", "2020-12-9", "47", "74"],
        ]
        employees = pd.DataFrame(
            data, columns=["emp_id", "event_day", "in_time", "out_time"]
        ).astype(
            {
                "emp_id": "Int64",
                "event_day": "datetime64[ns]",
                "in_time": "Int64",
                "out_time": "Int64",
            }
        )

        return employees

    def game_play_analysis_1(self):
        data = [
            [1, 2, "2016-03-01", 5],
            [1, 2, "2016-05-02", 6],
            [2, 3, "2017-06-25", 1],
            [3, 1, "2016-03-02", 0],
            [3, 4, "2018-07-03", 5],
        ]
        activity = pd.DataFrame(
            data, columns=["player_id", "device_id", "event_date", "games_played"]
        ).astype(
            {
                "player_id": "Int64",
                "device_id": "Int64",
                "event_date": "datetime64[ns]",
                "games_played": "Int64",
            }
        )

        return activity

    def number_of_unique_subjects_taught_by_each_teacher(self):
        data = [
            [1, 2, 3],
            [1, 2, 4],
            [1, 3, 3],
            [2, 1, 1],
            [2, 2, 1],
            [2, 3, 1],
            [2, 4, 1],
        ]
        teacher = pd.DataFrame(
            data, columns=["teacher_id", "subject_id", "dept_id"]
        ).astype({"teacher_id": "Int64", "subject_id": "Int64", "dept_id": "Int64"})

        return teacher

    def classes_more_than_5_students(self):
        data = [
            ["A", "Math"],
            ["B", "English"],
            ["C", "Math"],
            ["D", "Biology"],
            ["E", "Math"],
            ["F", "Computer"],
            ["G", "Math"],
            ["H", "Math"],
            ["I", "Math"],
        ]
        courses = pd.DataFrame(data, columns=["student", "class"]).astype(
            {"student": "object", "class": "object"}
        )

        return courses

    def customer_placing_the_largest_number_of_orders(self):
        data = [[1, 1], [2, 2], [3, 3], [4, 3]]
        orders = pd.DataFrame(data, columns=["order_number", "customer_number"]).astype(
            {"order_number": "Int64", "customer_number": "Int64"}
        )

        return orders

    def group_sold_prodcts_by_the_date(self):
        data = [
            ["2020-05-30", "Headphone"],
            ["2020-06-01", "Pencil"],
            ["2020-06-02", "Mask"],
            ["2020-05-30", "Basketball"],
            ["2020-06-01", "Bible"],
            ["2020-06-02", "Mask"],
            ["2020-05-30", "T-Shirt"],
        ]
        activities = pd.DataFrame(data, columns=["sell_date", "product"]).astype(
            {"sell_date": "datetime64[ns]", "product": "object"}
        )

        return activities

    def daily_leads_and_partners(self):
        data = [
            ["2020-12-8", "toyota", 0, 1],
            ["2020-12-8", "toyota", 1, 0],
            ["2020-12-8", "toyota", 1, 2],
            ["2020-12-7", "toyota", 0, 2],
            ["2020-12-7", "toyota", 0, 1],
            ["2020-12-8", "honda", 1, 2],
            ["2020-12-8", "honda", 2, 1],
            ["2020-12-7", "honda", 0, 1],
            ["2020-12-7", "honda", 1, 2],
            ["2020-12-7", "honda", 2, 1],
        ]
        daily_sales = pd.DataFrame(
            data, columns=["date_id", "make_name", "lead_id", "partner_id"]
        ).astype(
            {
                "date_id": "datetime64[ns]",
                "make_name": "object",
                "lead_id": "Int64",
                "partner_id": "Int64",
            }
        )

        return daily_sales

    def actors_and_directors_who_cooperated_at_least_three_times(self):
        data = [
            [1, 1, 0],
            [1, 1, 1],
            [1, 1, 2],
            [1, 2, 3],
            [1, 2, 4],
            [2, 1, 5],
            [2, 1, 6],
        ]
        actor_director = pd.DataFrame(
            data, columns=["actor_id", "director_id", "timestamp"]
        ).astype({"actor_id": "int64", "director_id": "int64", "timestamp": "int64"})

        return actor_director

    def replace_employee_id_with_the_unique_identifier(self):
        data = [
            [1, "Alice"],
            [7, "Bob"],
            [11, "Meir"],
            [90, "Winston"],
            [3, "Jonathan"],
        ]
        employees = pd.DataFrame(data, columns=["id", "name"]).astype(
            {"id": "int64", "name": "object"}
        )
        data = [[3, 1], [11, 2], [90, 3]]
        employee_uni = pd.DataFrame(data, columns=["id", "unique_id"]).astype(
            {"id": "int64", "unique_id": "int64"}
        )

        return employees, employee_uni

    def students_and_examinations(self):
        data = [[1, "Alice"], [2, "Bob"], [13, "John"], [6, "Alex"]]
        students = pd.DataFrame(data, columns=["student_id", "student_name"]).astype(
            {"student_id": "Int64", "student_name": "object"}
        )
        data = [["Math"], ["Physics"], ["Programming"]]
        subjects = pd.DataFrame(data, columns=["subject_name"]).astype(
            {"subject_name": "object"}
        )
        data = [
            [1, "Math"],
            [1, "Physics"],
            [1, "Programming"],
            [2, "Programming"],
            [1, "Physics"],
            [1, "Math"],
            [13, "Math"],
            [13, "Programming"],
            [13, "Physics"],
            [2, "Math"],
            [1, "Math"],
        ]
        examinations = pd.DataFrame(
            data, columns=["student_id", "subject_name"]
        ).astype({"student_id": "Int64", "subject_name": "object"})

        return students, subjects, examinations

    def managers_with_at_least_5_direct_reports(self):
        data = [
            [101, "John", "A", None],
            [102, "Dan", "A", 101],
            [103, "James", "A", 101],
            [104, "Amy", "A", 101],
            [105, "Anne", "A", 101],
            [106, "Ron", "B", 101],
        ]
        employee = pd.DataFrame(
            data, columns=["id", "name", "department", "managerId"]
        ).astype(
            {
                "id": "Int64",
                "name": "object",
                "department": "object",
                "managerId": "Int64",
            }
        )

        return employee

    def sales_person(self):
        data = [
            [1, "John", 100000, 6, "4/1/2006"],
            [2, "Amy", 12000, 5, "5/1/2010"],
            [3, "Mark", 65000, 12, "12/25/2008"],
            [4, "Pam", 25000, 25, "1/1/2005"],
            [5, "Alex", 5000, 10, "2/3/2007"],
        ]
        sales_person = pd.DataFrame(
            data, columns=["sales_id", "name", "salary", "commission_rate", "hire_date"]
        ).astype(
            {
                "sales_id": "Int64",
                "name": "object",
                "salary": "Int64",
                "commission_rate": "Int64",
                "hire_date": "datetime64[ns]",
            }
        )
        data = [
            [1, "RED", "Boston"],
            [2, "ORANGE", "New York"],
            [3, "YELLOW", "Boston"],
            [4, "GREEN", "Austin"],
        ]
        company = pd.DataFrame(data, columns=["com_id", "name", "city"]).astype(
            {"com_id": "Int64", "name": "object", "city": "object"}
        )
        data = [
            [1, "1/1/2014", 3, 4, 10000],
            [2, "2/1/2014", 4, 5, 5000],
            [3, "3/1/2014", 1, 1, 50000],
            [4, "4/1/2014", 1, 4, 25000],
        ]
        orders = pd.DataFrame(
            data, columns=["order_id", "order_date", "com_id", "sales_id", "amount"]
        ).astype(
            {
                "order_id": "Int64",
                "order_date": "datetime64[ns]",
                "com_id": "Int64",
                "sales_id": "Int64",
                "amount": "Int64",
            }
        )

        return sales_person, company, orders
