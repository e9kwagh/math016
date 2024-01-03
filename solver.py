"""math problem no 16"""


def solver(n):
    """solver"""
    start = str(2**4)
    final = ""

    for _ in range(5, n + 1):
        start = str(start)    
        result,carry = "",0
        for num in start[::-1]:
            value = int(num) * 2 + carry
            reminder = value % 10
            carry = value // 10
            result += str(reminder)
            final = result
        if carry != 0:
            final = final + str(carry)
        start = final[::-1]

    li = [int(i) for i in final[::-1]]
    return sum(li)


if __name__ == "__main__":
    print(solver(10))
