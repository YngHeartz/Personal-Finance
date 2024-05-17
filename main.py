# Imports
import pymongo

# Db connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["personal_finance"]
post_spending = db["spending"]

def options():
    # ask user for an option that are associated with their respective functions
    question = input('What would you like to do? option1: for Uplodoading your finances. option2: retrieving financial information: ')
    # Option1 returns the Finances function
    if question == 'option1':
        Finances()
    # Option2 returns the retrieve_Finances function
    elif question == 'option2':
        retrieve_Finances()
    else:
        # If there is not a valid option closes and alerts the user
        print('Invalid option. Closing program.')
        exit()


# Finance Function
def Finances():
    # Variables for getting user data
    date_of_budget = str(input('Enter in the format 00/00/0000: '))
    month_of_year = str(input('What is the month you are budgeting for?: '))
    monthly_budget = int(input('What is your monthly budget going to be?: '))
    monthly_earnings = int(input('What was your monthly earnings?: '))
    monthly_spending = int(input('What was your monthly spending?: '))
    
    # Checks to see if the user entered a negative number or an invalid number
    if monthly_budget < 0 or monthly_earnings < 0 or monthly_spending < 0:
        print('You entered a number less than zero or an invalid number. Your data will not be uploaded.')
        exit()
    
    # Calculations for monthly spendings
    total_left = (monthly_earnings - monthly_spending)
    print(f'You have ${total_left} left this month')
    gain_loss = int(monthly_earnings - monthly_budget)

    # Returns if you made or lost money and how much
    if gain_loss < monthly_spending:
        print(f'You made ${gain_loss} dollars this month.')
    else:
        print(f'You lost ${gain_loss} dollars this month.')
    
    # This is the data that will be sent to the database 
    financial_post = {
        "date_of_budget": date_of_budget,  # Consistent field name
        "month_of_budget": month_of_year,
        "monthly_budget": monthly_budget,
        "monthly_earnings": monthly_earnings,
        "monthly_spending": monthly_spending,
        "total_left": total_left,
        "gain_or_loss": gain_loss
    }
    
    # Sends data to the database
    post_spending.insert_one(financial_post)
    
    # Confirmation message
    print('Finances Uploaded')

    check_prev_finnces = print('Did you want to check previous finances? if so type Yes and if not press any key to continue')
    if check_prev_finnces == 'Yes':
        retrieve_Finances()

def retrieve_Finances():
    # Asks the user for the date of the financial data they want to retrieve
    get_finances = input('What is the date you want to retrieve your finances from?: ')
    
    # Query to retrieve the financial data for the specified date
    result = post_spending.find_one({"date_of_budget": get_finances})
    
    # Prints the financial data for the specified date
    if result:
        print(f"Finances for {get_finances}:")
        print(f"Date of Budget: {result['date_of_budget']}")
        print(f"Monthly Budget: {result['monthly_budget']}")
        print(f"Monthly Earnings: {result['monthly_earnings']}")
        print(f"Monthly Spending: {result['monthly_spending']}")
        print(f"Total Left: {result['total_left']}")
        print(f"Gain or Loss: {result['gain_or_loss']}")
    else:
        # Prints a message if no financial data is found for the specified date
        print(f"No financial data found for the date: {get_finances}")

options()
