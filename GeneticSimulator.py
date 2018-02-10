import numpy as np
import matplotlib.pyplot as plt

rounds = 30
levels=4
memberCount = 10

members = [1]*memberCount
deaths=[0]*rounds
removed=0;

for i in range(0,rounds):
    removed=0
    for counter in range(0,len(members)):
        counter=counter-removed
        initial_population = members[counter]
        for j in range(0,initial_population):
            members[counter] = (members[counter] + np.random.randint(0,levels,size=1)-1)[0]
        if members[counter] == 0:
            del members[counter]
            removed = removed + 1
            deaths[i]=deaths[i]+1
    members.sort(reverse=True)
    if len(members)!=0:
        plt.plot((members/sum(members)))
plt.show()
    
plt.plot(deaths)
plt.show()

print("deaths {}".format(sum(deaths)))
print("original members {}".format(memberCount))
if len(members)!=0:
    print("member allele share {}".format(members/sum(members)))
else:
    print("all members dead")