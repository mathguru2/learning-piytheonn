def factorial(arg1):
    tot=1
    if int(arg1)==arg1 and arg1>0:
        for i in range(1,arg1+1):
            tot=tot*i
        print(tot)
    else:
        print("You need to enter an integer")

    return tot;
factorial(2)


def tree_ref(tree, index):
    for i in index:

        tree=tree[i]
    return tree

print(tree_ref((((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10)) ,(3,1)))