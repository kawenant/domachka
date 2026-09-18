sells=[("Q",1), ("W",1), ("E",1), ("Q",5), ("W",9), ("E",11),("Q",13), ("W",1), ("E",15)]

summs=dict()

for name, s in sells:
    if name in summs:
     summs[name]+=s
else:
    summs[name]=s

    print(summs)

    max_sum=max(summs.values())

    for i in summs:
        if summs[i]==max_sum:
            print(i)