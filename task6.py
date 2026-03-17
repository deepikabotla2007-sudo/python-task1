n = int(input("Enter number of transactions: "))
transactionamounts = [0] * n

for i in range(n):
    transactionamounts[i] = int(input("Enter amount: "))

print("\nThe list of transactions is:")
for i in range(n):
    print(transactionamounts[i])

categorized = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}

for t in transactionamounts:
    if t <= 0:
        categorized["invalid"].append(t)
    elif t <= 500:
        categorized["normal"].append(t)
    elif t <= 2000:
        categorized["large"].append(t)
    else:
        categorized["high_risk"].append(t)


valid_transactions = [t for t in transactionamounts if t > 0]


total_value = sum(valid_transactions)
num_transactions = len(transactionamounts)


frequent = num_transactions > 5
large_spending = total_value > 5000
suspicious = len(categorized["high_risk"]) >= 3


if suspicious or (frequent and large_spending):
    risk = "High Risk"
elif frequent or large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"


summary = (total_value, num_transactions)


print("\nCategorized Transactions:")
for key in categorized:
    print(key, ":", categorized[key])

print("\nSummary (Total Value, Number of Transactions):", summary)
print("Final Risk Classification:", risk)