# Import pathlib
from pathlib import Path

# Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size


def test_save_csv():
    # @TODO: Your code here!
    csvpath = Path('qualifying_loans.csv')

    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    qualifying_loans = test_save_csv()
    
    # @TODO: Test the new save_csv code!
    assert credit_score(current_credit_score, bank_data) == [
        ['Bank of Big - Premier Option','300000','0.85','0.47','740','3.6'], 
        ['Bank of Fintech - Premier Option','300000','0.9','0.47','740','3.15'],
        ['Prosper MBS - Premier Option','400000','0.85','0.42','750','3.45'],
        ['Bank of Big - Starter Plus','300000','0.85','0.39','700','4.35'],
        ['West Central Credit Union - Starter Plus','300000','0.8','0.44','650','3.9'],
        ['FHA Fredie Mac - Starter Plus','300000','0.85','0.45','550','4.35'],
        ['FHA Fannie Mae - Starter Plus','200000','0.9','0.37','630','4.2'],
        ['General MBS Partners - Starter Plus','300000','0.85','0.36','670','4.05'],
        ['Bank of Fintech - Starter Plus','100000','0.85','0.47','610','4.5'],
        ['iBank - Starter Plus','300000','0.9','0.4','620','3.9'],
        ['Goldman MBS - Starter Plus','100000','0.8','0.43','600','4.35'],
        ['Citi MBS - Starter Plus','300000','0.8','0.39','740','4.05'],
        ['Prosper MBS - Starter Plus','100000','0.9','0.38','640','3.75'],
        ['Developers Credit Union - Starter Plus','200000','0.85','0.46','640','4.2'],
        ['Bank of Stodge & Stiff - Starter Plus','100000','0.8','0.35','680','4.35']
        ]
    assert debt_to_income(monthly_debt_ratio, bank_data) == [
        ['Bank of Big - Premier Option','300000','0.85','0.47','740','3.6'], 
        ['Bank of Fintech - Premier Option','300000','0.9','0.47','740','3.15'],
        ['Prosper MBS - Premier Option','400000','0.85','0.42','750','3.45'],
        ['Bank of Big - Starter Plus','300000','0.85','0.39','700','4.35'],
        ['West Central Credit Union - Starter Plus','300000','0.8','0.44','650','3.9'],
        ['FHA Fredie Mac - Starter Plus','300000','0.85','0.45','550','4.35'],
        ['iBank - Starter Plus','300000','0.9','0.4','620','3.9'],
        ['Goldman MBS - Starter Plus','100000','0.8','0.43','600','4.35'],
        ['Citi MBS - Starter Plus','300000','0.8','0.39','740','4.05'],
        ['Prosper MBS - Starter Plus','100000','0.9','0.38','640','3.75'],
        ['Developers Credit Union - Starter Plus','200000','0.85','0.46','640','4.2']
        ]
    assert loan_to_value(loan_to_value_ratio, bank_data) == [
        ['Bank of Big - Premier Option','300000','0.85','0.47','740','3.6'], 
        ['Bank of Fintech - Premier Option','300000','0.9','0.47','740','3.15'],
        ['Prosper MBS - Premier Option','400000','0.85','0.42','750','3.45'],
        ['Bank of Big - Starter Plus','300000','0.85','0.39','700','4.35'],
        ['FHA Fredie Mac - Starter Plus','300000','0.85','0.45','550','4.35'],
        ['iBank - Starter Plus','300000','0.9','0.4','620','3.9'],
        ['Prosper MBS - Starter Plus','100000','0.9','0.38','640','3.75'],
        ['Developers Credit Union - Starter Plus','200000','0.85','0.46','640','4.2']
        ]
    assert max_loan_size(loan, bank_data) == [
        ['Prosper MBS - Starter Plus','100000','0.9','0.38','640','3.75'],
        ['Developers Credit Union - Starter Plus','200000','0.85','0.46','640','4.2']
        ]
