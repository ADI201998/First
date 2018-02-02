ef count(n):
    sum=0
    for i in range(1,n+1):
	    print(i)
	    sum=sum+i
    return sum
def main():
    n=int(input())
    s = count(n)
    print(s)
main()    

