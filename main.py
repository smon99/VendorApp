from src.Structure.Market import MarketController

market_controller_instance = MarketController()

user_input = input("Do you want to Start? Y/n? ").strip().lower()

if user_input == 'y':
    start = True
elif user_input == 'n':
    start = False
else:
    print("Invalid input. Please enter 'Y' or 'n'.")
    start = False

if start:
    market_controller_instance.process()
