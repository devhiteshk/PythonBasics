# Weekly challenge week 4
# 1 print a pyramid
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 4
triangle(n)

# problem2
# names = [ "John", " ", "Amanda", 5]
#for name in names:
 #   if type(name) == str:
 #       if name.strip() != '':
  #          print(name)

# Convert Celsius

tem = [32, 12, 44, 29]
Ftem = []
l = len(tem)
print('\n')
for i in range(l):
    F = float(tem[i])*(9.0/5.0) + 32
    Ftem.append(F)

print(Ftem)

# challenge complete
