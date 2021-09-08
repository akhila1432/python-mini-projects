def binary_search(arr,num):
    l_b=0
    u_b=len(arr)-1
    mid=0
    while l_b<=u_b:
        mid=(l_b+u_b)//2
        mid_value=arr[mid]

        if mid_value==num:
             print("Element {} found at position {}".format(num,mid+1))
             mid = 1
             return True

        elif mid_value < num:
            l_b=mid+1
        else:
            u_b=mid-1
    if mid!=1:
        print("Searching element {} not found in the array list".format(num))    
    return -1

if __name__=='__main__':
 arr = []    
size = int(input("Enter the size of the array: "))    
       
for i in range(size):    
     x= int(input("Enter the element at {} position in the array: ".format(i+1)))    
     arr.append(x)    
      
arr.sort()    
num = int(input("\nEnter the array element to be searched: "))  
binary_search(arr, num)    
