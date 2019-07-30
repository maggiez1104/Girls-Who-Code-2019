#is_even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#calc_total
list1 = [2, 5, 8, 4]
print("the list is")
print(list1)

def calc_total(list1):
    #add all numbers in list
    sum = 0
    #return list1
    for num in list1:
        sum += num
    return sum

def main():
    #while True:
        #num = input("Pick a number: ")
        #number = int(num)
        #is_even(number)
        #print(is_even(number))
        calc_total(list1)
        print("the sum of the list is: " + str(calc_total(list1)))

if __name__ == "__main__":
    main()
