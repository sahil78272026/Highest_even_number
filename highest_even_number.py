# Highest Even Number

def high_even(li):
    new_li=[val for val in li if val%2==0]
    new_li.sort()
    return new_li[-1]    



print(f"Highest Even Number is : {high_even([3,4,5,6,1,0,10,11,50,40,300,51])}")