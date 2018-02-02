#WAF make_list() which will build an initial empty list and return the list to
#the main. Ensure that only positive numbers are added to the list
#Rewrite the function to recieve the size of the list

def make_list(n):
    a=[]
    for i in range(n):
        x = int(input())
        if x>=0:
            a = a +[x]
        else:
            i=i-1
    return a
def main():
    n = int(input())
    print(make_list(n))
main()
