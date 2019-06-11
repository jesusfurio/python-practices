import subprocess
from datetime import datetime, date, timedelta
from enum import Enum
import requests
import json

def print_head(message):
    print('=' * len(message))
    print(message)
    print('=' * len(message))


def print_bottom(message):
    print('=' * len(message))
    print(message)
    print('=' * len(message))

class Commands:

    network_commands = [['ping','-c 5',input_server_domain(server_ip)],['nmap','-Pn',input_server_domain(server_ip)]]
    website_commands = [['wget',input_server_domain(server_ip)]]

    def input_server_domain():
        server_ip = input("Write the server IP or domain to check:")
        return server_ip

    def execute_commands():  

        if function_by_state[option] == 1:
            for i in commands(network_commands):
                subprocess.call(i)
            return subprocess.call(i)

        elif function_by_state[option] == 2:
            for i in commands(website_commands):
                subprocess.call(i)
            return subprocess.call(i)


class MenuStatus(Enum):
    network_commands = "1-Realize network test"
    website_commands = "2-Realize web service test"
    execute_sla = "3-Calculate SLA of Cloud service"
    close_menu = "4-Exit"

class Menu:

    def date_epoch(date):
        d = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
        convert = d.strftime("%s") 

        return convert

    def input_sla_params():
        try:
            st_date = input("Start date of the incident. The correct format is YYYY-MM-DD hh:mm:ss : ")
            st_epoch = date_epoch(st_date)

            end_date = input("End date of the incident. The correct format is YYYY-MM-DD hh:mm:ss : ")
            end_epoch = date_epoch(end_date)

            ip = input("Write affected IP: ")

            return st_epoch, end_epoch, ip
    
        except ValueError:

            exit("Invalid date format.")
    
    def get_sla(start,end,ip):
        url = "URL".format(ip)

        response = requests.get(url , params = {"start":start,"end":end})
    
        if response.status_code == 200:
            payload = response.json()
            availability = payload["availability"]
            print(availability * 100, "% of time available")    

        if response.status_code == 500:
            print("Invalid IP address.")

    def execute_sla():
        start, end, ip = input_sla_params()
        get_sla(start,end,ip)

    def close_menu():
        print ('Goodbye!')

    def main():
        print_head(message="Select your option:")
        for item in MenuStatus:
            print (item.value)

        option = int(input())

        return option

function_by_state = {
    0:Menu.main,
    1:Commands.input_server_domain,
    2:Commands.input_server_domain,
    3:Menu.execute_sla,
    4:Menu.close_menu,
}

if __name__ == '__main__':
    option = 0
    while option != 3:
        option = Menu.main()
        if option not in function_by_state:
            print ('Value not correct')
            continue
        function_by_state[option]()
