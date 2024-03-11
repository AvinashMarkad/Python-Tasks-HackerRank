# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
t1=map(int, input().split())
t=tuple(t1)
print(hash(t))
