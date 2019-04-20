from datetime import date
import smtplib
from enum import Enum


class MenuStatus(Enum):
    transfer_days = "1- Transfer days between services."
    calculate_voucher = "2- Create voucher for PCI."
    between_days = "3- Calculate days."
    close_menu = "4- Exit"


def print_head(message):
    print('=' * len(message))
    print(message)
    print('=' * len(message))


def print_bottom(message):
    print('=' * len(message))
    print(message)
    print('=' * len(message))


class Menu:
    def __init__(self):
        print ('Object initialized')

    def send_email(message):
        mailTo = "mail@to"
        mailFrom = "mail@from"
    
        server = smtplib.SMTP("mailserver","port")
        server.starttls()
        server.login("mail@example","password")
        server.sendmail(mailFrom,mailTo,message)
        server.quit() 

    @staticmethod
    def transfer_days():
        print ('=== Transfer days ===')
        """
        oldService: price of old service
        type: float
        newService: price of new service
        type: float
        """

        oldService = float(input("Enter the monthly amount of the service to be removed: "))
        oldServiceDays = int(input("How many days do you have to leave the service?: "))
        newService = float(input("Enter the monthly amount of the new service: "))

        calculOld = oldService / 30
        calculNew = newService / 30

        if oldService > newService:
            print("The old service amount is higher, so you can not make the commercial gesture")

        elif oldServiceDays < 30:
            print("You can't make the commercial gesture if there are less than 30 days left")

        elif oldService <= 0:
            print("The price entered must be greater than 0")

        else:
            return print("They must be transferred the following days: ",round((calculOld / calculNew) * oldServiceDays))

    @staticmethod
    def calculate_voucher():
        print ('=== Calculate voucher ===')
        """
        service: service price
        type: float
        days: remaining days of service
        type: int
        """

        service = float(input("Enter the monthly amount of the service to be removed: "))
        days = int(input("How many days do you have to leave the service?: "))

        if days < 30:
            print("There must be more than 30 days to generate a voucher")

        elif service == 0:
            print("The value of the service can't be 0")

        else:
            result = round((service / 30) * days)
            return print("The amount of the voucher is: ", result, "€")

    @staticmethod
    def between_days():
        print ('=== Between days ===')
        """
        dateExpiration: date expiration of old service
        type: int
        dateElimination: date elimination of old service
        type: int
        """

        print("Date of expiration service: ")
        yearOld = int(input("Year "))
        monthOld = int(input("Month "))
        dayOld = int(input("Day "))

        dateExpiration = date(yearOld, monthOld, dayOld)

        print("Date of deleted service: ")

        yearNew = int(input("Year "))
        monthNew = int(input("Month "))
        dayNew = int(input("Day "))

        dateElimination = date(yearNew, monthNew, dayNew)

        result = (dateElimination - dateExpiration).days

        return print(result, " days of difference.")

    @staticmethod
    def close_menu():
        print ('Goodbye!')

    @staticmethod
    def main():
        print_head(message="Select your option:")
        for item in MenuStatus:
            print (item.value)

        option = int(input())

        return option


function_by_state = {
    0: Menu.main,
    1: Menu.transfer_days,
    2: Menu.calculate_voucher,
    3: Menu.between_days,
    4: Menu.close_menu
}

if __name__ == '__main__':
    option = 0
    while option != 4:
        option = Menu.main()
        if option not in function_by_state:
            print ('Value not correct')
            continue
        function_by_state[option]()

    print_bottom('End of script')