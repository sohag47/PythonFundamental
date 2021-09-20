class CreditCard:
    # A consumer credit card

    def __init__(self, customer, bank, actn, limit):
        ''' 
        Create a new credit card instance/object
        The initial balance is zero
        '''
        self.customer = customer
        self.bank = bank
        self.actn = actn
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        # Return name of the customer
        return self.customer

    def get_bank(self):
        # Return name of the Bank's
        return self.bank

    def get_acoount(self):
        return self.actn

    def get_limit(self):
        return self.limit
    
    def get_balance(self):
        return self.balance

    def charge(self, price):
        if(price + self.balance > self.limit):
            return False
        else:
            self.balance += price
            return True
    def make_payment(self, amount):
        self.balance -= amount


obj1 = CreditCard('Sohag', '1st bank','123 456 789', '1000')
