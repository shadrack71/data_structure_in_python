# Linear Time Complexity: Big O(n) Complexity
# O(n)

def get_square_number(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)

    return squared_numbers


numbers = [2,3,4,5,6]

print(get_square_number(numbers))



