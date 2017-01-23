def __main__():
    global ele
    ele = list()
    while True:
        inp = raw_input("Please Enter a number: ")
        if inp == 'end':
            break
        
        i = int(inp)
        ele.append(i)
    print("Before Sorting: ",ele)
    #Call the sorting function
    #In Ascending order
    mysort(ele)
    print ("After Sorting: ",ele)
    search = raw_input("Enter the element to be found: ")
    search = int(search)
    #Call Binary Search Function
    loc = binsearch(ele,search)
    if loc == -1:
        print("The element was not found")
    else:
        print("The element is found at: ",(loc+1))
    
    mymean(ele)

def mysort(ele):
    n = len(ele)
    if n==0:
        print("List is Empty")
        return
    if n==1:
        print("Already sorted!!")
        return
    
    for i in range(n):
        for j in range(i,n):
            if ele[i]>ele[j]:
                temp = ele[i]
                ele[i] = ele[j]
                ele[j] = temp

def binsearch(ele,s):
    if len(ele) == 0:
        print("The List is Empty")
        return -1
    else:
        start = 0
        end = len(ele)-1
        found = False
        while start<=end and not found:
            mid = (start+end)/2
            if ele[mid]==s:
                loc = mid
                found = True
            elif s > ele[mid]:
                start = mid + 1
            elif s < ele[mid]:
                end = mid + 1
        if found:
            return loc
        else:
            return -1
def mymean(ele):
    s = 0
    if len(ele) == 0:
        print("Cannot evaluate the Mean, Empty List")
        return
    
    for i in ele:
        s = s + i
    avg = s/len(ele)
    print("The Mean is: ",avg)

__main__()
        
