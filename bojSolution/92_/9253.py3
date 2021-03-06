from sys import stdin
def input(): return stdin.readline().rstrip()

def getFail(P):
    Plen=len(P)
    ret=[0]*Plen
    j=0
    for i in range(1,Plen):
        while j>0 and P[i]!=P[j]:
            j=ret[j-1]
        if P[i]==P[j]:
            j+=1
            ret[i]=j
    return ret

def KMP(T, P):
    Tlen=len(T)
    Plen=len(P)
    j=0
    for i in range(Tlen):
        while j>0 and T[i]!=P[j]:
            j=fail[j-1]
        if T[i]==P[j]:
            if j==Plen-1:
                return True
                j=fail[j]
            else:
                j+=1
    return False

T1=str(input())
T2=str(input())
ref=str(input())
fail=getFail(ref) # List

print("YES" if KMP(T1,ref) and KMP(T2,ref) else "NO")