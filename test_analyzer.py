import unittest
from analyzer import FinancialAnalyzer
import pandas as pd
from typing import cast


class TestFinancialAnalyzer(unittest.TestCase):

    def setUp(self):
        # Arrange: create analyzer object that runs before each test
        self.analyzer = FinancialAnalyzer("data.csv")

    ''' Test count_by_type method '''
    def test_count_by_type(self):
        # Act: Execute the method from analyzer
        result = self.analyzer.count_by_type()

        # Assert: Check if it is working as expected (Real Test Case)
        self.assertGreater(len(result), 0)

    ''' Test search_by_reference with VALID input '''
    def test_search_valid_reference(self):
        # Act
        result = self.analyzer.search_by_reference("INS001")

        # Assert: I am using typecast here to tell pycharm that we are using a dataframe so it doesn't get
        # confused if it is 'Any' and .empty throws a warning. (Cleaner code purpose)
        result = cast(pd.DataFrame, result)
        self.assertFalse(result.empty)

    ''' Test search_by_reference with INVALID input '''
    def test_search_invalid_reference(self):
        # Act
        result = self.analyzer.search_by_reference("INVALID")

        # Assert
        self.assertEqual(result, "No record found")

    ''' Test group_by_type method '''
    def test_group_by_type(self):
        result = self.analyzer.group_by_type()

        # Check type
        result = cast(pd.DataFrame, result)
        #self.assertIsInstance(result, pd.DataFrame) #checks if structure is dataframe

        # Check columns exist
        self.assertIn('count', result.columns)
        self.assertIn('sum', result.columns)
        self.assertIn('mean', result.columns)

    '''Test group_by_type if EMPTY method '''
    def test_group_by_type_empty(self):
        result = self.analyzer.group_by_type()

        # Check type
        result = cast(pd.DataFrame, result)
        # self.assertIsInstance(result, pd.DataFrame) #checks if structure is dataframe

        # Check not empty
        self.assertFalse(result.empty)

    ''' Check if highest transaction is correct '''

    def test_highest_transaction(self):
        result = self.analyzer.highest_transaction()

        # Check it contains amount column (exists or not)
        self.assertIn('amount', result)

        # Ensure value is max
        max_amount = self.analyzer.df['amount'].max()
        self.assertEqual(result['amount'], max_amount)

    def test_lowest_transaction(self):
        result = self.analyzer.lowest_transaction()

        # Check it contains amount column
        self.assertIn('amount', result)

        # Ensure value is min
        min_amount = self.analyzer.df['amount'].min()
        self.assertEqual(result['amount'], min_amount)


if __name__ == "__main__":
    unittest.main()