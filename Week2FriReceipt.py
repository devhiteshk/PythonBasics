# Friday Project : Receipt Printing Program

# step 1 : Define Variables
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# step 2 : Create company name and information
company_name = "Coding Temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# step 3 :  Declare ending message
message = "Thanks for shopping with us today!"

# step 4 : Creating top border
print("*" *50)

# Step 5 : displaying company information
print("*\t\t\t\t{}\t\t\t\t *".format(company_name.title()))
print("*\t\t\t\t{}\t\t\t\t *".format(company_address.title()))
print("*\t\t\t\t{}\t\t\t\t\t\t *".format(company_city.title()))

# Step 6 : print a line between sections
print("=" *50)

# step 7 : Displaying the product Information
print("*\t\tProduct Name\t\tProduct price\t\t *")
print("*\t\t{}\t\t\t\t${}\t\t\t\t *".format(p1_name.title(),p1_price))
print("*\t\t{}\t\t\t${}\t\t\t\t *".format(p2_name.title(),p2_price))
print("*\t\t{}\t\t\t\t${}\t\t\t\t *".format(p3_name.title(),p3_price))

# step 8 : line between section
print("*" *50)

# step 9 : Total
total = p1_price+p2_price+p3_price
print("*\t\t\t\t\t\t\tTotal\t\t\t\t *")
print("*\t\t\t\t\t\t\t${}\t\t\t\t *".format(total))

# step 10 : Print a line between section
print("=" *50)

# step 11 : end message
print("*\t\t{}\t\t *".format(message))

# step 11 : Line between section
print("*" *50)

# program completed
