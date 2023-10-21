airport_data = {}
def enter_new_airport():
    icao = input("Enter the ICAO code of the airport: ").strip().upper()
    name = input("Enter the name of the airport: ")
    airport_data[icao] = name
    print(f"Airport data for {icao} ({name}) has been stored.")
def fetch_airport_information():
    icao = input("Enter the ICAO code of the airport you want to fetch: ").strip().upper()
    if icao in airport_data:
        print(f"The name of the airport with ICAO code {icao} is {airport_data[icao]}.")
    else:
        print(f"No information found for ICAO code {icao}.")
while True:
    print("Airport Data Program")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Choose one option (1/2/3): ")
    if choice == "1":
        enter_new_airport()
    elif choice == "2":
        fetch_airport_information()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")