import pandas as pd

class FinancialAnalyzer:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.clean_data()

    def clean_data(self):
        # Convert date column from string datatype to datetime datatype
        self.df['date'] = pd.to_datetime(self.df['date'])

        # Fill missing values if any
        self.df.fillna(0, inplace=True)

    def preview_data(self):
        return self.df.head()

    def total_instructions(self):
        return len(self.df)

    def total_amount(self):
        return self.df['amount'].sum()

    def average_amount(self):
        return self.df['amount'].mean()

    def count_by_type(self):
        return self.df['instruction_type'].value_counts()

    def group_by_type(self):
        return self.df.groupby('instruction_type')['amount'].agg(['count', 'sum', 'mean'])

    def filter_by_status(self, status):
        return self.df[self.df['status'] == status]

    def search_by_reference(self, ref):
        result = self.df[self.df['instruction_ref'] == ref]
        if result.empty:
            return "No record found"
        return result

    def highest_transaction(self):
        return self.df.loc[self.df['amount'].idxmax()]

    def lowest_transaction(self):
        return self.df.loc[self.df['amount'].idxmin()]