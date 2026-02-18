n=int(input("Enter number of zones:"))
requests=[0]*n
for i in range(n):
    requests[i]=int(input("Enter resources requested by zone :"))
print("resources requested by different zones: ",requests)

low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_requests=[]

valid_count=0

for req in requests:
    if req < 0:
        invalid_requests.append(req)
    else:
        valid_count = valid_count + 1
        if req == 0:
          continue
        elif req >= 1 and req <= 20:
          low_demand.append(req)
        elif req >= 21 and req <= 50:
          moderate_demand.append(req)
        else:
          high_demand.append(req)
print("\nlist based on classification rules: ")
print("low demand",low_demand)
print("moderate demand",moderate_demand)
print("high demand",high_demand)
print("invalid requests",invalid_requests)

fullname=input("enter your full name: ")
count=0
for ch in fullname:
    if ch != " ":
     count=count+1
L=count
PLI=L%3
print("length of name: ",L)
print("PLI value ",PLI)

removed_count=0
if PLI == 0:
    removed_count=len(low_demand)
    low_demand=[]
elif PLI == 1:
    removed_count=len(high_demand)
    high_demand=[]
else:
    removed_count=len(low_demand)+len(high_demand)
    low_demand=[]
    high_demand=[]


print("Total valid requests: ",valid_count)
print("After personalization: ")
print("removed requests due to PLI:",removed_count)
print("low demand",low_demand)
print("moderate demand",moderate_demand)
print("high demand",high_demand)
print("invalid requests",invalid_requests)


