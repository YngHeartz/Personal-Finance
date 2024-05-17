# Imports
import pymongo
# Db connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["personal_finance"]
users_collection = db["spending"]
post_spending = db["spending"]

# Finance Function
def Finances():
    # Variables for getting user data
    month_of_year = str(input('What is the month you are budgeting for?: '))
    monthly_budget = int(input('What is your monthly budget going to be?: '))
    monthly_earnings = int(input('What was your monthly earnings?:'))
    monthly_spending = int(input('What was your monthly spending?:'))
    
    # Checks to see if the user entered a negative number or an invalid number
    if monthly_budget < 0 or monthly_earnings < 0 or monthly_spending < 0:
        print('You entered a number less than zero or an invalid number. Your data will not be uploaded.')
        exit()
    
    # Calculations for monthly spendings
    total_left = (monthly_earnings - monthly_spending)
    print(f'You have ${total_left} left this month')
    gain_loss = int (monthly_earnings - monthly_budget)

    # Returns if you made or lost money and how much
    if gain_loss < monthly_spending:
        print(f'You made ${gain_loss} dollars this month.')
    else:
        print(f'You lost ${gain_loss} dollars this month.')
    
    # This is the data that will be sent to the database 
    financial_post = {"month of budget": month_of_year,"monthly budget": monthly_budget, "monthly earnings": monthly_earnings, "monthly spending": monthly_spending, "total left": total_left, "gain or loss": gain_loss}
    
    # Sends data to the database
    post_spending.insert_one(financial_post)
    # if the data is uploaded successfully
    if Finances:
        print('Finances Uploaded')
    # if the data is uploaded unsuccessfully
    else:
        print('Finances not Uploaded')

    
# Calls the function
Finances()
