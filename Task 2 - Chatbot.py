import pandas as pd
import random
import datetime

# Load the data from CSV files
final_data = pd.read_csv('final_data.csv')
final_summary = pd.read_csv('final_summary.csv')

# Convert column names to lowercase for easier comparison
final_data.columns = final_data.columns.str.lower()
final_summary.columns = final_summary.columns.str.lower()

# Horizontal line for formatting and separation
line_length = 100  # Adjust the length as needed
line_character = "-"  # Choose the character for the line
line = line_character * line_length

# Define chatbot logic
def chatbot(inner_user_input):

    # Normalize user input to lowercase
    inner_user_input = inner_user_input.lower()

    # Define keywords and corresponding column names
    keywords_to_columns = {
        "revenue": "total revenue",
        "income" or "profit": "net income",
        "asset" or "assets": "total assets",
        "liability" or "liabilities": "total liabilities",
        "cash flow": "cash flow from operating activities"
    }

    # Extract the keyword from the user input
    for keyword, column in keywords_to_columns.items():
        if keyword in inner_user_input:
            parts = inner_user_input.split()
            company = None
            year = None

            # Extract company name from query
            for part in parts:
                if part in final_data['company'].str.lower().unique():
                    company = part
                    break

            # Extract year from query if present
            for part in parts:
                if part.isdigit() and int(part) in final_data['year'].unique():
                    year = int(part)
                    break

            # If both company and year are provided
            if company and year:
                data = final_data[(final_data['company'].str.lower() == company) & (final_data['year'] == year)]
                return f"{company.capitalize()}'s {column} in {year}: ${data[column].values[0]}"

            # If only company is provided
            elif company:
                data = final_data[final_data['company'].str.lower() == company]
                return f"{company.capitalize()}'s {column} over the years:\n" + \
                           "\n".join([f"     {row['year']}: ${row[column]}" for index, row in data.iterrows()])

            # If only year is provided
            elif year:
                data = final_data[final_data['year'] == year]
                result = f"Metrics for all companies in {year}:\n"
                for index, row in data.iterrows():
                    company = row['company']
                    metric = row[column]
                    result += f"     {company.capitalize()}: ${metric}\n"
                return result

            # If neither is provided
            else:
                return "Please specify a company name from the dataset."

    # Handle other queries or provide a generic response
    else:
        return "Sorry, I couldn't understand your request."

# Startup greeting based on the time of the day
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    greeting = random.choice(["Good morning! ☀️", "Rise and shine! 🌅", "Morning! ☕"])
elif current_hour < 18:
    greeting = random.choice(["Good afternoon! ⛅", "How's your day going? 😊"])
else:
    greeting = random.choice(["Good evening! 🌙", "How was your day? 😴"])

# Startup introduction
print("\nBot:", greeting)
print(f"""
     I'm your financial data assistant. Ask me anything about the data I have.\n\n\
     To get started:\n\
         * Type a question about the data.\n\
         * Type "help" to see available options.\n\
         * Type "exit" or "quit" to end the conversation.\n\n\
     Let's dive into the numbers!\n{line}""")

# Main loop for user interaction
while True:
    user_input = input("\n\033[32mYou:\033[0m ")
    if user_input.lower() in ['exit', 'quit']:
        print(f"\033[34mBot:\033[0m {random.choice(["Goodbye! 👋", "Buh-bye! 👋", "See you around! 😊", "Later! ✌️", "Godspeed! 🚀"])} \n{line}")
        break

    elif user_input.lower() in ['hi', 'hey', 'hello']:
        print(f"\033[34mBot:\033[0m  {random.choice(["Hi there! 👋", "Hello! 😊", "Hey there! 😄", "Greetings! 😃", "Howdy!🤠", "Yo! 😎", "What's up? 🤔", "Sup? 😎", "Salutations!🎩"])} \n{line}")

    else:
        response = chatbot(user_input)
        print(f"\033[34mBot:\033[0m {response} \n{line}")