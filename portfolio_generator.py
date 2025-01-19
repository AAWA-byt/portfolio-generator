import pandas as pd

def main_menu():
    while True:
        # Main menu for the portfolio generator
        print("\nPortfolio Generator")
        print("1. Create a new portfolio with desired allocation")
        print("2. Adjust an existing portfolio to match desired allocation")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            create_portfolio()
        elif choice == '2':
            adjust_portfolio()
        elif choice == '3':
            print("Program exited.")
            break
        else:
            print("Invalid input. Please try again.")

def create_portfolio():
    # Create a new portfolio based on user-defined allocation
    print("\nCreate a New Portfolio")
    allocation = get_allocation()
    total_amount = float(input("Enter the total portfolio amount (in Euros): "))

    portfolio = calculate_portfolio(allocation, total_amount)
    print("\nCalculated Portfolio:")
    print(portfolio)

def adjust_portfolio():
    # Adjust an existing portfolio to match a desired allocation
    print("\nAdjust Existing Portfolio")
    allocation = get_allocation()

    num_classes = len(allocation)
    print("\nEnter the current values of the asset classes (in Euros):")
    current_values = []
    for category in allocation.keys():
        value = float(input(f"{category}: "))
        current_values.append(value)

    current_total = sum(current_values)
    desired_total = float(input("Enter the desired total portfolio value (in Euros): "))

    portfolio_df = adjust_to_allocation(allocation, current_values, current_total, desired_total)
    print("\nPortfolio Adjustment:")
    print(portfolio_df)

def get_allocation():
    # Get desired allocation percentages for asset classes from the user
    allocation = {}
    while True:
        print("\nAsset Classes (Enter allocation percentages):")
        allocation["Global Equity ETFs"] = float(input("Global Equity ETFs (%): "))
        allocation["Individual Stocks"] = float(input("Individual Stocks (%): "))
        allocation["Bonds/Cash Reserves"] = float(input("Bonds/Cash Reserves (%): "))
        allocation["Thematic/Industry ETFs"] = float(input("Thematic/Industry ETFs (%): "))

        if sum(allocation.values()) == 100:
            break
        else:
            print("The total allocation must equal 100%. Please try again.")

    return allocation

def calculate_portfolio(allocation, total_amount):
    # Calculate portfolio distribution based on allocation percentages and total amount
    data = {
        "Asset Class": [],
        "Allocation (%)": [],
        "Amount (Euros)": []
    }

    for category, percentage in allocation.items():
        data["Asset Class"].append(category)
        data["Allocation (%)"].append(percentage)
        data["Amount (Euros)"].append(round(total_amount * (percentage / 100), 2))

    return pd.DataFrame(data)

def adjust_to_allocation(allocation, current_values, current_total, desired_total):
    # Adjust portfolio to match desired allocation
    categories = list(allocation.keys())
    desired_values = [round(desired_total * (allocation[cat] / 100), 2) for cat in categories]
    adjustments = [round(desired - current, 2) for desired, current in zip(desired_values, current_values)]

    data = {
        "Asset Class": categories,
        "Current Value (Euros)": current_values,
        "Desired Value (Euros)": desired_values,
        "Difference (Euros)": adjustments,
        "Desired Allocation (%)": [allocation[cat] for cat in categories],
        "Current Allocation (%)": [round((current / current_total) * 100, 2) for current in current_values]
    }

    total_adjustment = round(sum(adjustments), 2)
    data["Total Adjustment (Euros)"] = ["" for _ in categories]
    data["Total Adjustment (Euros)"][0] = total_adjustment

    return pd.DataFrame(data)

if __name__ == "__main__":
    main_menu()
