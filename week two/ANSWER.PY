#practice 2
# question 1
item=int(input("enter how many items you want to buy:"))
def apply_discount(item):
    if(item>3):
        print("discount applied")
    else:
        print("no discount")
apply_discount(item)

# question 2
prices=[120,45,300,85,150]
def get_expensive_products(prices):
    expensive_products=[]
    for price in prices:
        if(price>100):
            expensive_products.append(price)
        return expensive_products
print("the expensive products are:",get_expensive_products(prices))

# question 3
with open("log.txt","a") as file:
    file.write("user logged in\n")
with open("log.txt","r") as file:
    for i in file:
        print(i)

# question 4
student={"kidus":"90","abebe":"85","susan":"95","lily":"80","john":"70"}
def get_grade(student):
    try:
        name=input("enter the student name:")
        grade=student[name]
        print(f"{name}'s grade is {grade}")
    except KeyError:
        print("student not found in the system")

get_grade(student)

# question 5
with open("sales.txt","r") as file:
    try:
        for sales_number in file:
            sales=int(sales_number)
            print(f"sales number: {sales}")
    except ValueError:
        print("invalid sales number found in the file")

# question 6
with open("sales.txt","w") as file:
    file.write("150\n")
    file.write("200\n")
    file.write("abc\n")  # just adding example of invalid data
    file.write("300\n")
with open("sales.txt","r") as file:
    try:
        for sales_number in file:
            sales=int(sales_number)
            sales_list=[]
            sales_list.append(sales)
            total_sales+=sales
    except ValueError:
        print("invalid sales number found in the file")


print("total sales:",total_sales)

# question 7
num=int(input("enter a number:"))
answer=["1","2","3","4","5","6","7","8","9","10"]
if(num%3==0 and num%5==0):
    answer[num-1]="fizzbuzz"
elif(num%3==0):
    answer[num-1]="fizz"
elif(num%5==0):
    answer[num-1]="buzz"
else:
    answer[num-1]=str(num)
for i in range(0,num):
    print(answer[i])


# question 8
arr = [0,1,0,3,12]

def pushing(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] == 0 and arr[j+1] != 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]

pushing(arr)
print("sorted list:", arr)

# question 9
nums=[3,2,4]
target=6
n=len(nums)
output=[]
def add_up(arr,target,n,output):
        for i in range(n):
         for j in range(1,n):
            if(arr[i]+arr[j]==target):
                output.append(i)
                output.append(j)
                return output


print(add_up(nums,target,n,output))

# question 10
num=(input("enter the number:"))
def check(num):
    if(num==num[::-1]):
        print("true")
    else:
        print("false")
check(num)

# question 11
number=int(input("enter a number:"))
def mySqrt(x):
    if x < 2:   
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid          
        elif square < x:
            left = mid + 1      
        else:
            right = mid - 1    

    return right                 

print("the square root is:",mySqrt(number))




# question 12
with open("numbers.txt","w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("forty\n")  # adding invalid data for testing
    file.write("50\n")
with open("numbers.txt","r") as file:
    total=0
    for number in file:
        try:
            num=int(number)
            total+=num
        except ValueError:
            print("invalid data found in the file")
print("the total sum is:",total)


# question 13
m1=input("enter some text:")
m2=input("enter another text:")

with open("messages.txt","w") as file:
    file.write(m1+"\n")
    file.write(m2+"\n")
with open("messages.txt","r") as file:
    for message in file:
        upper_message=message.upper()
        print(upper_message)

# question 14
scores={"kidus":"90","abebe":"85","susan":"95","lily":"80","john":"70"}
def display(scores):
    try:
        name=input("enter the student name:")
        grade=scores[name]
        print(f"{name}'s grade is {grade}")
    except KeyError:
        print("student not found ")

get_grade(scores)


# question 15
sentence=input("enter a sentence:")
words=sentence.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print("word frequencies:",word_count)


# question 16
grades = {"John": "A", "Sara": "B", "Musa": "A"}
inverted = {}
for name, grade in grades.items():
    if grade not in inverted:
        inverted[grade] = []
    inverted[grade].append(name)

print(inverted)