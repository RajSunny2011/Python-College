L1 = [0,0,1,1]
L2 = [0,1,0,1]
print("A  B  &  |  ^")
for i in range(0,4):
    print(f"{L1[i]}  {L2[i]}",L1[i]&L2[i],L1[i]|L2[i],L1[i]^L2[i],sep="  ")
