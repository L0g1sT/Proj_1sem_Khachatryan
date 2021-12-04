

def Swap(X,Y):
    Y,X = X,Y
    return X,Y

A = input("")
B = input()
C = input()
D = input()
print(Swap(A,B))
A,B = Swap(A,B)
print(Swap(C,D))
C,D = Swap(C,D)
print(Swap(B,C))
B,C = Swap(B,C)
print(A,B,C,D)