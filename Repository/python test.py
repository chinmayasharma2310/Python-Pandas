from array import * 

# Three largest distinct element
arr = array('i',[ 10,2,35,23,89,78,99,65])
arr= sorted(arr)
print(arr[-3:])
print(arr[len(arr)-2])

arr1= array('i',[0,2,35,56,85,0,26,0])
arr1=sorted(arr1)
arr1.reverse()
print(arr1)

# Re-arranging the array element as per index array.

arr = array('i',[11,34,56,23,45,89])
index = array('i',[1,3,0,5,2,4])

temp = []
n = len(index)
for i in range(0, n):
    for j in range(0, n):
        if(index[j] == i ):
            temp.append(arr[j])
        
print("Reorderd array:", end = " ")
for ele in range(len(temp)):
    print(temp[ele])



