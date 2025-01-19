import pandas as pd

def main_menu():
    while True:
        print("\nPortfolio Generator")
        print("1. Portfolio mit neuer Gewichtung erstellen")
        print("2. Portfolio an gewünschte Gewichtung anpassen")
        print("3. Beenden")
        choice = input("Wähle eine Option (1-3): ")

        if choice == '1':
            create_portfolio()
        elif choice == '2':
            adjust_portfolio()
        elif choice == '3':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle erneut.")

def create_portfolio():
    print("\nNeues Portfolio erstellen")
    allocation = get_allocation()
    total_amount = float(input("Gib die Gesamtsumme des Portfolios ein (in Euro): "))

    portfolio = calculate_portfolio(allocation, total_amount)
    print("\nBerechnetes Portfolio:")
    print(portfolio)

def adjust_portfolio():
    print("\nPortfolio anpassen")
    allocation = get_allocation()

    num_classes = len(allocation)
    print("\nGib die aktuellen Werte der Anlageklassen ein (in Euro):")
    current_values = []
    for category in allocation.keys():
        value = float(input(f"{category}: "))
        current_values.append(value)

    current_total = sum(current_values)
    desired_total = float(input("Gib den gewünschten Gesamtwert des Portfolios ein (in Euro): "))

    portfolio_df = adjust_to_allocation(allocation, current_values, current_total, desired_total)
    print("\nPortfolio-Anpassung:")
    print(portfolio_df)

def get_allocation():
    allocation = {}
    while True:
        print("\nAnlageklassen (Gib die Gewichtung in Prozent an):")
        allocation["Globale Aktien-ETFs"] = float(input("Globale Aktien-ETFs (%): "))
        allocation["Einzelaktien"] = float(input("Einzelaktien (%): "))
        allocation["Anleihen/Barreserven"] = float(input("Anleihen/Barreserven (%): "))
        allocation["Themen/Branchen-ETFs"] = float(input("Themen/Branchen-ETFs (%): "))

        if sum(allocation.values()) == 100:
            break
        else:
            print("Die Gesamtgewichtung muss 100% ergeben. Bitte erneut eingeben.")

    return allocation

def calculate_portfolio(allocation, total_amount):
    data = {
        "Anlageklasse": [],
        "Gewichtung (%)": [],
        "Betrag (Euro)": []
    }

    for category, percentage in allocation.items():
        data["Anlageklasse"].append(category)
        data["Gewichtung (%)"].append(percentage)
        data["Betrag (Euro)"].append(round(total_amount * (percentage / 100), 2))

    return pd.DataFrame(data)

def adjust_to_allocation(allocation, current_values, current_total, desired_total):
    categories = list(allocation.keys())
    desired_values = [round(desired_total * (allocation[cat] / 100), 2) for cat in categories]
    adjustments = [round(desired - current, 2) for desired, current in zip(desired_values, current_values)]

    data = {
        "Anlageklasse": categories,
        "Aktueller Wert (Euro)": current_values,
        "Gewünschter Wert (Euro)": desired_values,
        "Differenz (Euro)": adjustments,
        "Gewünschte Gewichtung (%)": [allocation[cat] for cat in categories],
        "Aktuelle Gewichtung (%)": [round((current / current_total) * 100, 2) for current in current_values]
    }

    total_adjustment = round(sum(adjustments), 2)
    data["Gesamtanpassung (Euro)"] = ["" for _ in categories]
    data["Gesamtanpassung (Euro)"][0] = total_adjustment

    return pd.DataFrame(data)

if __name__ == "__main__":
    main_menu()
