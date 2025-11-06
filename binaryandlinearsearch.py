customer_id = [1000 , 1001 , 1002 , 1003 , 1004 , 1005 , 1006 ]
def linearSearch(key):
    for i in range(len(customer_id)):
        if customer_id[i] == key:
            print("customer id found at " , i)
            return
    print(key , "not found")
    return

def binarySearch(key):
    start = 0
    end = len(customer_id) - 1
    while start <= end:
        mid = (start + end) // 2

        if(customer_id[mid] == key):
            print(f"Customer Id {key} found at index {mid}")
            return
        elif key < customer_id[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print("not found")
    return
            
    
while True :
    key = int(input("Enter id \n"))
    print("1. Linear Search \n 2. Binary Search \n 3. Exit")
    opt = int(input("enter search no. \n "))
    if opt== 1:
        linearSearch(key)
    elif opt == 2:
        binarySearch(key)
    elif opt == 3:
        break
    else:
        print("invalid input \n")
        continue


    
