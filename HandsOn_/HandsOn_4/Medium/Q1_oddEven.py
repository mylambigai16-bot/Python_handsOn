def sumOfOdd():
    sum_odd = 0
    for i in range(1, 1001):
        if(i % 2 == 0):
            sum_odd += i
    return sum_odd

def sumOfEven():
    sum_even = 0
    for i in range(1, 1001):
        if(i % 2 != 0):
            sum_even += i
    return sum_even

OddSum = sumOfOdd()
evenSum = sumOfEven()
print("The sum of odd numbers from 1 to 1000 is: ",OddSum)
print("The sum of even numbers from 1 to 1000 is: ",evenSum)
print("The absolute difference between the two sums is: ",abs(OddSum-evenSum))