import json

def slash_balance(model_name, amount):
    # Load balances
    with open("balances.json", "r") as file:
        balances = json.load(file)
    if model_name in balances:
        balances[model_name]['balance'] = max(0, balances[model_name]['balance'] - amount)
    # Save changes
    with open("balances.json", "w") as file:
        json.dump(balances, file)

def reward_balance(model_name, amount):
    # Load balances
    with open("balances.json", "r") as file:
        balances = json.load(file)
    if model_name in balances:
        balances[model_name]['balance'] += amount
    # Save changes
    with open("balances.json", "w") as file:
        json.dump(balances, file)