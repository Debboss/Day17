import re
import calendar
import random

class HotelBookingSystem:
    def __init__(self):
        self.new_customers = {}
        self.users_accounts = {'despoina': 123, 'sofia': 321}
        self.available_rooms = {'Room3': 32, 'Room4': 45}
        self.unavailable_rooms = {'Room1': 29, 'Room2': 9}
        self.available_days = [5, 7, 12, 18, 23]
        self.year = 2023
        self.month = 7

    def run(self):
        print("Welcome to the Hotel Booking System\nLogin is required")
        print("If you do not have an account, please type: 'new' to the 'username' section and press enter to the 'password' section")

        username = input("Username: ")
        password = input("Password: ")

        if self.check_credentials(username, password):
            exit()

    def check_credentials(self, username, password):
        attempts = 0
        while attempts < 2:
            if (username == 'root' and password == 'admin'):
                print(f"You have logged in as admin\nWelcome {username}")
                while True:
                    if self.admin_options():
                        break
                return True

            elif (username in self.users_accounts) and (int(password) == self.users_accounts[username]):
                print(f"You have logged in as a client\nWelcome {username}")
                while True:
                    if self.user_options():
                        break
                return True

            elif (username == 'new') and (password == ''):
                while True:
                    if self.new_account():
                        break
                return True

            else:
                attempts += 1
                print("Wrong credentials.\nPlease try again.")
                username = input("Username: ")
                password = input("Password: ")

        print("You have exceeded the maximum number of attempts. Exiting...")
        return False

    def admin_options(self):
        print("How would you like to proceed?: ")
        print("\n1) Available rooms")
        print("2) Registered Accounts")
        print("3) Restaurant Reservation")
        print("4) Logout")

        option = int(input("Input here: "))
        if option == 1:
            self.display_rooms()
        elif option == 2:
            self.display_registered_accounts()
        elif option == 3:
            self.restaurant_reservation()
        elif option == 4:
            print("You have successfully logged out")
            exit()
        else:
            print("Invalid option.")

    def display_rooms(self):
        print("These are the available rooms:")
        for room in self.available_rooms:
            print(f"The following room is \033[92mavailable\033[0m: {room}")
        for room in self.unavailable_rooms:
            print(f"The following room is \033[91munavailable\033[0m: {room}")

    def display_registered_accounts(self):
        print("These are the registered accounts: ")
        for user in self.users_accounts:
            print(user)

    def restaurant_reservation(self):
        print("These are the available days for reservation: ")
        self.generate_calendar()

    def generate_calendar(self):
        cal = calendar.Calendar()
        month_calendar = cal.monthdatescalendar(self.year, self.month)

        print(f"{calendar.month_name[self.month]} {self.year}")
        print("Mon Tue Wed Thu Fri Sat Sun")

        for week in month_calendar:
            for day in week:
                if day.month == self.month:
                    day_display = f"\033[92m{day.day:2d}\033[0m" if day.day in self.available_days else f"{day.day:2d}"
                else:
                    day_display = "  "
                print(day_display, end=" ")
            print()

        choice = int(input("Enter the date for reservation: "))
        if choice in self.available_days:
            print(f"The date you chose is: {calendar.month_name[self.month]} {choice}, {self.year}")
        else:
            print("The chosen date is not available for reservation.")

    def new_account(self):
        while True:
            new_username = input("Please choose a username: ")
            if new_username not in self.users_accounts:
                print(f"Your username is: {new_username}")
                random_number = self.generate_random_3_digit_number()
                print(f"Your account's number is: {random_number}")
                break
            else:
                print("This username is already taken. Please choose another username.")

    def generate_random_3_digit_number(self):
        return random.randint(100, 999)

    def user_options(self):
        print("How would you like to proceed?: ")
        print("1) Cancellation Request")
        print("2) Restaurant Reservation")
        print("3) Logout")

        option = int(input("Input here: "))
        if option == 1:
            self.cancellation_request()
        elif option == 2:
            self.restaurant_reservation()
        elif option == 3:
            print("You have successfully logged out")
            exit()
        else:
            print("Invalid option.")

    def cancellation_request(self):
        email = input("For your cancellation request, your email address is required: ")
        if self.is_valid_email(email):
            print("Valid email address.")
            print("The reservation has successfully been cancelled.")
        else:
            print("Invalid email address.")

    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

if __name__ == "__main__":
    hotel_system = HotelBookingSystem()
    hotel_system.run()
