def depth(arg1):
        if isinstance(arg1,(list,tuple)):
            return 1+max(depth(item) for item in arg1)
        else:
            return 0

print(depth(('expt',('x',2))))