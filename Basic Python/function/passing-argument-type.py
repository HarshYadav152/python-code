def modify_immutable(x):
    x = 10 # rebind x to new object
    print(f"Inside function : x = {x}")

x = 5
print(f"Before function call : x = {x}")
modify_immutable(x)
print(f"After function call : x = {x}")


def modify_mutable(lst):
    lst.append(4) # this modify the list
    print(f"Inside function list : {lst}")

lst = [1,2,3]
print(f"Before function call list : {lst}")
modify_mutable(lst)
print(f"After function call list : {lst}")