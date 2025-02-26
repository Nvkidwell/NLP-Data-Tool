from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import datetime

class ActionQuerySales(Action):
    def name(self):
        return "action_query_sales"

    def run(self, dispatcher, tracker, domain):
        # Load your CSV data
        df = pd.read_csv("sales_data.csv")

        # Example logic: filter by month or date range
        today = datetime.date.today()
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        df['date'] = pd.to_datetime(df['date'])

        monthly_sales = df[df['date'].dt.month == last_month.month]['sales'].sum()

        dispatcher.utter_message(text=f"Total sales for last month: {monthly_sales}")
        return []

class ActionQueryProducts(Action):
    def name(self):
        return "action_query_products"

    def run(self, dispatcher, tracker, domain):
        df = pd.read_csv("sales_data.csv")
        top_products = df.groupby('product')['sales'].sum().nlargest(5)
        dispatcher.utter_message(text=f"Top 5 products by sales: {top_products}")
        return []

class ActionQueryAvgSales(Action):
    def name(self):
        return "action_query_avg_sales"

    def run(self, dispatcher, tracker, domain):
        df = pd.read_csv("sales_data.csv")
        avg_sales = df['sales'].mean()
        dispatcher.utter_message(text=f"Average sales: {avg_sales}")
        return []

class ActionQuerySalesTrends(Action):
    def name(self):
        return "action_query_sales_trends"

    def run(self, dispatcher, tracker, domain):
        df = pd.read_csv("sales_data.csv")
        monthly_sales_trends = df.groupby(df['date'].dt.to_period('M'))['sales'].sum()
        dispatcher.utter_message(text=f"Sales trends over time: {monthly_sales_trends}")
        return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import datetime

class ActionQuerySales(Action):
    def name(self):
        return "action_query_sales"

    def run(self, dispatcher, tracker, domain):
        # Load your CSV data
        df = pd.read_csv("sales_data.csv")

        # Example logic: filter by month or date range
        today = datetime.date.today()
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        df['date'] = pd.to_datetime(df['date'])

        monthly_sales = df[df['date'].dt.month == last_month.month]['sales'].sum()

        dispatcher.utter_message(text=f"Total sales for last month: {monthly_sales}")
        return []

class ActionQueryProducts(Action):
    def name(self):
        return "action_query_products"

    def run(self, dispatcher, tracker, domain):
        df = pd.read_csv("sales_data.csv")
        top_products = df.groupby('product')['sales'].sum().nlargest(5)
        dispatcher.utter_message(text=f"Top 5 products by sales: {top_products}")
        return []

class ActionQueryAvgSales(Action):
    def name(self):
        return "action_query_avg_sales"

    def run(self, dispatcher, tracker, domain):
        df = pd.read_csv("sales_data.csv")
        avg_sales = df['sales'].mean()
        dispatcher.utter_message(text=f"Average sales: {avg_sales}")
        return []

class ActionQuerySalesTrends(Action):
    def name(self):
        return "action_query_sales_trends"

    def run(self, dispatcher, tracker, domain):
        df = pd.read_csv("sales_data.csv")
        monthly_sales_trends = df.groupby(df['date'].dt.to_period('M'))['sales'].sum()
        dispatcher.utter_message(text=f"Sales trends over time: {monthly_sales_trends}")
        return []
