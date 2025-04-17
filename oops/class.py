class account:
    def __init__(self,id,name,bal):
        print("special method is created")
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=bal
    def open_acc(self):
        print("open account method")
        
    def check_bal(self,amt):
        self.acc_bals=self.acc_bals*amt
        print("check  method")
    @classmethod
    def check_status(cls):
        print("open status method")
    @staticmethod
    def check_interest():
        print("open interest method")
a=account(10,'sai',5000)
a.open_acc()
a2.check_bal(50)
a.check_status()
a.check_interest()
print(a.__dict__)
