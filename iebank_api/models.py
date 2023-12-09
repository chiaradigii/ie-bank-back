from iebank_api import db
from datetime import datetime
import string, random

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    account_number = db.Column(db.String(20), nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False, default = 0.0)
    currency = db.Column(db.String(1), nullable=False, default="€")
    status = db.Column(db.String(10), nullable=False, default="Active")
    country = db.Column(db.String(32), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transactions = db.Column(db.String(1024), nullable=False, default = "")
    main_account = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Event %r>' % self.account_number

    def __deactivate__(self):
        self.status = "Inactive"
        return self.status

    def __init__(self, name, password, currency, balance, country, transactions, main_account):
        self.name = name
        self.password = password
        self.account_number = ''.join(random.choices(string.digits, k=20))
        self.currency = currency
        self.balance = balance
        self.status = "Active"
        self.country = country
        self.transactions = transactions
        self.main_account = main_account