train_number = [1,2,3,4,5,6,7,8,9,10]
train_status = {'onTime':1,'delayed':2,'cancelled':5,'ontime':8}

outcome = []
print(train_status.values())
for i in train_status.values():
    for j in train_number:
        if(i==j):
            outcome.append(i)
            
print(outcome)