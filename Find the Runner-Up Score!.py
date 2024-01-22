if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sortedArray=sorted(arr)
    
    a=max(sortedArray)
    
    c=sortedArray.count(a)
    
    for i in range (c):
        sortedArray.remove(a)
        
    print(max(sortedArray))
