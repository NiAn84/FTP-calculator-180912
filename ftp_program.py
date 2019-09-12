import time
from time import sleep
from os import path


def new_entry():
    print("\nEnter your test result")
    print("=" * 22)
    while True:
        power = input("Enter your FTP test result (W): ")
        weight = input("Enter your weight (kg): ")
        try:
            wkg = get_wkg(power, weight)
        except ValueError as e:
            print(e)
        else:
            break
    date = get_date()
    print(f"You have entered date {date}, FTP {power}W and weight {weight}kg.")
    correct = get_correct()
    if correct == 1:
        write_data(power, weight, wkg, date)
        get_latest_result()
    else:
        pass


def get_wkg(power, weight): # Räknar ut watt per kg men innan det kontrollerar så de inmatade värdena är rimliga.
    power = int(power)
    weight = int(weight)
    if not 50 <= power <= 500:
        raise ValueError("Did you enter a correct FTP power value? FTP should be between 50 and 500Watt.")
    if not 20 <= weight <= 200:
        raise ValueError("Did you enter a correct weigt? Weight must be between 20 and 200kg.")
    wkg = power / weight
    return round(wkg, 2)


def get_date():
    while True:
        choice = input("Do you wan't to use todays date? (Y/N): ")
        if choice.lower() == "y":
            date =(time.strftime("%y/%m/%d"))
            print(date)
            return date
        if choice.lower() == "n":
            while True:
                print("Enter the date you took the test")
                year = input("Year (YY): ")
                month = input("Month (MM): ")
                day = (input("Day (DD): "))
                try:
                    date = assemble_date(year, month, day)
                except ValueError as e:
                    print(e)
                else:
                    return date
        else:
            print("Ooops, you didn't answer yes (Y) or no (N)")


def assemble_date(year, month, day): # Sätta ihop datum och kontrollera så värden på år, månad och dag är ok.
    year = int(year)
    month = int(month)
    day = int(day)
    if not 00 <= year <= 99:
        raise ValueError("Did you enter a correct year? It should be between 00 and 99")
    if not 1 <= month <= 12:
        raise ValueError("Did you enter a correct month? It should be between 01 and 12")
    if not 1 <= day <= 31:
        raise ValueError("Did you enter a correct day? It should be between 01 and 31")
    date = str(f"{year}/{month}/{day}")
    return date


def get_correct(): # Användaren ska kontrollera så den matat in rätt uppgifter innan de sparas i data.txt
    while True:
        correct = 1
        choice = input("Is this correct? (Y/N): ")
        if choice.lower() == "y":
            return correct
        if choice.lower() == "n":
            return 0
        else:
            print("Ooops, you didn't answer yes (Y) or no (N)")


def write_data(power, weight, wkg, date):
    with open("data.txt", "a") as f:
        f.write(f"\n{power};{weight};{wkg};{date}")


def get_latest_result():
    if path.exists("data.txt") is True: # Ser till att programmet ej kraschar om fil data.txt saknas
        with open("data.txt", "r") as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            data = last_line.split(";")
            print(f"\nYour latest entered test result were made on date {data[3]} and the result were:")
            print(f"{data[2]}W/kg, {data[0]}W and your weight were {data[1]}kg")
            sleep(10)
    else:
        print("No data file exist, create one by select choice 1 in the menu") # Informerar användaren om att data.txt saknas
        sleep(5)


def get_highest_wkg_result():
    if path.exists("data.txt") is True: # Ser till att programmet ej kraschar om fil data.txt saknas
        highest_result = [0.0, 0.0, 0.0, 0.0]
        zero = [0.0, 0.0, 0.0, 0.0]
        for line in open(str(level)+".txt", "r"):
            data = line.split(";")
            data[2] = float(data[2])
            if highest_result[2] == zero[2] or data[2] > highest_result[2]:
                highest_result = data
        print(f"\nYour highest W/kg test result were made on date {highest_result[3]}")
        print("And the results were:")
        print(f"{highest_result[2]}W/kg, {highest_result[0]}W and your weight were {highest_result[1]}kg")
        sleep(10)
    else:
        print("No data file exist, create one by select choice 1 in the menu") # Informerar användaren om att data.txt saknas
        sleep(5)


def get_lowest_wkg_result():
    if path.exists("data.txt") is True: # Ser till att programmet ej kraschar om fil data.txt saknas
        lowest_result = [0.0, 0.0, 0.0, 0.0]
        zero = [0.0, 0.0, 0.0, 0.0]
        for line in open("data.txt", "r"):
            data = line.split(";")
            data[2] = float(data[2])
            if lowest_result[2] == zero[2] or data[2] < lowest_result[2]:
                lowest_result = data
        print(f"\nYour lowest W/kg test result were made on date {lowest_result[3]}")
        print("And the results were:")
        print(f"{lowest_result[2]}W/kg, {lowest_result[0]}W and your weight were {lowest_result[1]}kg")
        sleep(10)
    else:
        print("No data file exist, create one by select choice 1 in the menu") # Informerar användaren om att data.txt saknas
        sleep(5)


def get_highest_w_result():
    if path.exists("data.txt") is True: # Ser till att programmet ej kraschar om fil data.txt saknas
        highest_result = [0.0, 0.0, 0.0, 0.0]
        zero = [0.0, 0.0, 0.0, 0.0]
        for line in open("data.txt", "r"):
            data = line.split(";")
            data[0] = float(data[0])
            if highest_result[0] == zero[0] or data[0] > highest_result[0]:
                highest_result = data
        print(f"\nYour highest FTP (W) test result were made on date {highest_result[3]}")
        print("And the results were:")
        print(f"{highest_result[2]}W/kg, {highest_result[0]}W and your weight were {highest_result[1]}kg")
        sleep(10)
    else:
        print("No data file exist, create one by select choice 1 in the menu") # Informerar användaren om att data.txt saknas
        sleep(5)


def get_lowest_w_result():
    if path.exists("data.txt") is True: # Ser till att programmet ej kraschar om fil data.txt saknas
        lowest_result = [0.0, 0.0, 0.0, 0.0]
        zero = [0.0, 0.0, 0.0, 0.0]
        for line in open("data.txt", "r"):
            data = line.split(";")
            data[0] = float(data[0])
            if lowest_result[0] == zero[0] or data[0] < lowest_result[0]:
                lowest_result = data
        print(f"\nYour lowest FTP (W) test result were made on date {lowest_result[3]}")
        print("And the results were:")
        print(f"{lowest_result[2]}W/kg, {lowest_result[0]}W and your weight were {lowest_result[1]}kg")
        sleep(10)
    else:
        print("No data file exist, create one by select choice 1 in the menu") # Informerar användaren om att data.txt saknas
        sleep(5)


def menu():
    choice = "0"
    while choice != "7":
        print("\nMain Menu - Functional Threshold Power")
        print("=" * 38)
        print("\n1. Enter test value FTP (W) and weight (kg)")
        print("2. Show the latest entered test result")
        print("3. Show the highest W/kg test result")
        print("4. Show the lowest W/kg test result")
        print("5. Show the highest FTP (W) test result")
        print("6. Show the lowest FTP (W) test result")
        print("7. Exit")
        choice = input("Enter your choice: ") # Jag valde att ha menyval som str, detta för att undvika krash om användare matar in bokstav istället för siffra.
        if choice == "1":
            new_entry()
        if choice == "2":
            get_latest_result()
        if choice == "3":
            get_highest_wkg_result()
        if choice == "4":
            get_lowest_wkg_result()
        if choice == "5":
            get_highest_w_result()
        if choice == "6":
            get_lowest_w_result()


def main():
    menu()


if __name__ == '__main__':
    main()