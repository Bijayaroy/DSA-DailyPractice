def zeroesatend(arr, n): 
	count = 0 
	for i in range(n): 
		if arr[i] != 0: 
		
			arr[count] = arr[i] 
			count+=1
	
	while count < n: 
		arr[count] = 0
		count += 1

arr_str = input("Enter the array of integers (comma-separated): ")
arr = [int(num) for num in arr_str.split(',')]
n = len(arr) 
zeroesatend(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr) 


