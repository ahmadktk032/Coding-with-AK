def create_account(name, balance):
    return {"owner":name, "balance":balance}
def deposit( account,amount):
    account["balance"] += amount
# just checking this functin
def withdraw(account,amount):
    if amount > account["balance"]:
        return "Insufficient Balance"
    account['balance'] -= amount
