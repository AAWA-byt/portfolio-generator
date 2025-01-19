# Portfolio Generator 📊

This project is a Python-based **Portfolio Generator** that allows users to:

1. **Create a new portfolio** with desired asset class allocations.
2. **Adjust an existing portfolio** to align with a target allocation by calculating required changes.

## Features ✨

- Interactive **console-based menu** for user input.
- Support for **dynamic allocation percentages**.
- **Detailed portfolio calculations** with current, desired values, and adjustment recommendations.
- Outputs results in a clear tabular format using `pandas`.

---

## How to Use 🚀

### Prerequisites

1. **Python**: Ensure Python 3.7 or higher is installed.
2. **Dependencies**: Install the required Python library:
   ```bash
   pip install pandas
   ```

### Running the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/AAWA-byt/portfolio-generator
   cd portfolio-generator
   ```
2. Run the program:
   ```bash
   python portfolio_generator.py
   ```

### Menu Options

- **Option 1: Create a New Portfolio**
  1. Input the desired allocation percentages for each asset class.
  2. Enter the total portfolio amount (in Euros).
  3. View the calculated portfolio with amounts per asset class.

- **Option 2: Adjust an Existing Portfolio**
  1. Input the desired allocation percentages.
  2. Enter current values for each asset class.
  3. Provide the desired total portfolio amount.
  4. View the adjustments needed in both percentage and Euro amounts.

- **Option 3: Exit**
  - Exit the program.

---

## Code Documentation 🧑‍💻

### Main Functions

#### `main_menu()`
Displays the main menu and handles user selection:
- **1**: Calls `create_portfolio()`.
- **2**: Calls `adjust_portfolio()`.
- **3**: Exits the program.

#### `create_portfolio()`
- Prompts the user to enter desired allocation percentages and the total portfolio amount.
- Calls `calculate_portfolio()` to compute the portfolio.
- Displays the results in a table.

#### `adjust_portfolio()`
- Prompts the user to enter desired allocation percentages, current values, and the desired total amount.
- Calls `adjust_to_allocation()` to calculate adjustments.
- Displays the required changes in a table.

#### `get_allocation()`
- Collects allocation percentages for asset classes from the user.
- Ensures the total allocation equals 100%.

#### `calculate_portfolio(allocation, total_amount)`
- Takes the allocation percentages and total amount.
- Returns a `pandas` DataFrame with calculated amounts per asset class.

#### `adjust_to_allocation(allocation, current_values, current_total, desired_total)`
- Calculates the required adjustments to align the current portfolio with the desired allocation.
- Returns a `pandas` DataFrame with detailed changes.

---

## Example Output 🖥️

### Option 1: Create a New Portfolio

```
Enter the total portfolio amount (in Euros): 10000

Calculated Portfolio:
               Asset Class  Allocation (%)  Amount (Euros)
0      Global Equity ETFs            50.0         5000.00
1       Individual Stocks            20.0         2000.00
2  Bonds/Cash Reserves               20.0         2000.00
3  Thematic/Industry ETFs            10.0         1000.00
```

### Option 2: Adjust an Existing Portfolio

```
Enter current values of the asset classes (in Euros):
Global Equity ETFs: 4000
Individual Stocks: 3000
Bonds/Cash Reserves: 2000
Thematic/Industry ETFs: 1000

Enter the desired total portfolio value (in Euros): 12000

Portfolio Adjustment:
               Asset Class  Current Value (Euros)  Desired Value (Euros)  Difference (Euros)  Desired Allocation (%)  Current Allocation (%)
0      Global Equity ETFs                 4000.0                 6000.0             2000.0                    50.0                  40.0
1       Individual Stocks                 3000.0                 2400.0             -600.0                    20.0                  30.0
2  Bonds/Cash Reserves                    2000.0                 2400.0              400.0                    20.0                  20.0
3  Thematic/Industry ETFs                 1000.0                 1200.0              200.0                    10.0                  10.0

Total Adjustment (Euros): 2000.0
```

---

## Contributing 🤝

Feel free to open issues or submit pull requests if you have ideas for improvements or new features.

---

## License 📜
This project is licensed under the MIT License.
