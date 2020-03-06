####################################
class bank:
    def __init__(self, name, address, account):
        self.name = name
        self.address = address
        self.account = []


####################################
class account_holder:
    def __init__(self, fname, lname, mname, account_type, balance, status):
        self.fname = fname
        self.lname = lname
        self.mname = mname
        self.account_type = account_type
        self.balance = balance
        self.status = status
        super(bank, self).__init__(fname, lname, mname, account_type, balance, status, account)

    ####################################
    def open_account(self, fname, lname, mname, account_type, balance, status):
        if balance >= 100:

            temp = account_new(fname, lname, mname, account_type, balance, status)
            self.account.append(temp)
        return (f"account created for{fname} {lname} with a blanance of {balance}")
        # else balance < 100 :
        #     print("Insufficent funds deposited, account must have atleast 100 dollars starting amount")


####################################
    def transfer(self, transfer_amount):
    ####################################
        def withdraw(self, withdraw_amount):

    ####################################
            def overdraft(self, fee):

    ####################################

                # def show_accounts(self):
                #
                #     for account_holder:
                #         print(f"")


####################################
                def main():
                    wellsfargo = bank("wells fargo", "23 cherry lane", "checking")

                    while True:
                        print("1. make account")
                        print("2. print accounts")
                        print("3. withdraw")
                        print("4. exit account")
                        print("Enter choice(1-4)?")

                        response = input("enter in a response")

                    if (response == 1):

                        fname = input("enter in first name ")
                        mname = input("enter in middle name")
                        lname = input("enter in sur name")
                        account_type = input("account type, checkiing/saving")
                        deposit = int(input("enter in deposit amount"))


                    elif (response ==2):
                        wellsfargo.show_accounts()

                    elif (response == 4):
                        return ("good bye")
                        exit()

                    wellsfargo.open_account("nicholas", "nwanochie", "chigozie", "savings", 200, "open")
