def rshift(arr,rshift):
	rshift=int(input("enter the l_step value = "))
	for count in range(rshift):
		x=arr[-1]
		for i in range(len(arr)-2,-1,-1):
			arr[i+1]=arr[i]
		arr[0]=x
	print("after shifting = ",arr)

arr=[]
sizeofarr=int(input("enter the size of array = "))
for i in range(sizeofarr):
	val=int(input("enter the value of array = "))
	arr.append(val)
print("old arr = ",arr)

rshift(arr,rshift)


