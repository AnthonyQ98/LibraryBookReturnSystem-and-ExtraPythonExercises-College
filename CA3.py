"""
Anthony Quinn X00138635
14/12/2020
CA3
"""

number = 0
fee_per_day = 1.50
lateFee = 0
total = 0
totalDaily = 0
totalDays = 0

print("***********************************************************\n"
      "\tWelcome to the Library Book Return System\n"
      "***********************************************************")

staffNumber = input("Enter your staff ID number: ")

while len(staffNumber) != 5 and staffNumber[0-2] != "DUB":
    staffNumber = input("Error in Staff ID Number - re-enter: ")
else:
    print("**************************************************\n"
          "\t\tReturns Section\n"
          "**************************************************")
    bookReturn = input("Welcome member - do you have books to return, y/n: ")
    while bookReturn == "y" or bookReturn == "yes":
        number_of_books = int(input("How many books are you returning? "))
        totalDays = 0
        for lateBook in range(number_of_books):
            lateBook = int(input("Thank you for returning book {}, how many days late is this book? ".format(lateBook + 1)))
            if lateBook > 0:
                lateFee = lateBook * fee_per_day
                print("The late fee for this book is €" + str(lateFee))
                total += lateFee
                totalDays += lateBook
                totalBooks = fee_per_day * totalDays
        print("\nThe late fee for all these books is €" + str(totalBooks))
        bookReturn = input("\nWelcome member - do you have books to return, y/n: ")

print("\nThe total late fees today are €" + str(total))
print("Processed by staff member: ", staffNumber)

