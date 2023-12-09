from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, country, status and created_at fields are defined correctly
    """
    account = Account('John Doe', 'jujuju', 200, '$', 'papua neuva guinea', '37986437677657530547 77589212239432817621 1000 ,', False)
    assert account.name == 'John Doe'
    assert account.password == 'jujuju'
    assert account.account_number != None
    assert account.balance == 200
    assert account.currency == '$'
    assert account.status == 'Active'
    assert account.country == 'Argentina'
    assert account.transactions == '37986437677657530547 77589212239432817621 1000 ,'
    assert account.main_account == False

def test_account_deactivate():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the __deactivate__ method is defined correctly
    """
    account = Account('John Doe', 'jujuju', 200, '$', 'papua neuva guinea', '37986437677657530547 77589212239432817621 1000 ,', False)
    assert account.__deactivate__() == "Inactive"
    
def test_account_check():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the __repr__ method is defined correctly
    """
    account = Account('John Doe', 'jujuju', 200, '$', 'papua neuva guinea', '37986437677657530547 77589212239432817621 1000 ,', False)
    assert repr(account) == f"<Event '{(account.account_number)}'>"

def test_main_account_flag():
    """
    GIVEN a Account model
    WHEN a new Account is created with the main_account flag
    THEN check the main_account field is set correctly
    """
    account = Account('John Doe', 'jujuju', 200, '$', 'papua neuva guinea', '37986437677657530547 77589212239432817621 1000 ,', True)
    assert account.main_account == True

def test_account_balance_update():
    """
    GIVEN a Account model
    WHEN the balance of an Account is updated
    THEN check the balance is updated correctly
    """
    account = Account('John Doe', 'jujuju', 200, '$', 'papua neuva guinea', '37986437677657530547 77589212239432817621 1000 ,', False)
    account.balance = 1000
    assert account.balance == 1000

def test_transaction_string_format():
    """
    GIVEN a Account model
    WHEN a new Account is created with a transaction string
    THEN check the transaction string is formatted correctly
    """
    account = Account('John Doe', 'jujuju', 200, '$', 'papua neuva guinea', '37986437677657530547 77589212239432817621 1000 ,', False)
    assert account.transactions == '37986437677657530547 77589212239432817621 1000 ,'