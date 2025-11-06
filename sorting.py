salary = [1232 , 2343, 4543 , 3456, 4564, 1123]
def bubbleSort(salary):
    n = len(salary)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if salary[j] >salary[j+1]:
                # swap
                temp = salary[j]
                salary[j] = salary[j+1]
                salary[j+1] = temp
    print(salary)


def selectionSort(salary):
    start = 0
    end = len(salary) - 1
    for i in range(end):
        min_index = i
        for j in range(i + 1 , len(salary)):
            if salary[j] < salary[min_index]:
                min_index = j
        # swap i and min_inx
        temp = salary[i]
        salary[i] = salary[min_index]
        salary[min_index] = temp
    print(salary)    
    
while True:
    print("1. Bubble Sort \n 2. Selection Sort \n 3.Exit")
    opt = int(input("Enter Option : \n"))
    if opt == 1:
        bubbleSort(salary)
    elif opt == 2:
        selectionSort(salary)
    elif opt == 3:
        break
    else:
        print("invalid")
        continue

        
    
