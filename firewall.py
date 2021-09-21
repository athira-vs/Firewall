#!/usr/bin/python3

import pprint
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import os

CONF ={}

console = Console()


def colour_print(colour, string):
    console.print(string, style = f'bold {colour}')


def execute_shell(cmd):
    return os.popen(cmd).read()


def fw_reload():
    print(execute_shell("sudo firewall-cmd --reload"))


def fw_activate():
    colour_print("#00FF00", "Activating the firewall")
    execute_shell("sudo systemctl start firewalld")


def fw_get_status():
    state = execute_shell("sudo firewall-cmd --state")
    if state == "running\n":
        colour_print("#00FF00", "Firewall is active")
    else:
        colour_print("#FF0000", "Firewall is not active")
        fw_activate()
    fw_get_active_zones()


def get_zone_list():
    zone_lst = execute_shell("sudo firewall-cmd --get-zones").split(" ")
    zone_lst[-1] = zone_lst[-1][:-1] 
    return zone_lst


def fw_add_port():
    port = Prompt.ask("Enter port number")
    proto = Prompt.ask("Enter protocol", choices=["tcp","udp"],default="tcp")
    zone =  Prompt.ask("Enter zone", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = f"sudo firewall-cmd --add-port={port}/{proto} --zone={zone} --permanent "
    print(execute_shell(cmd))


def fw_get_services():
    colour_print("#00FF00", "_________________________________________________________")
    colour_print("#00FF00", "Service List:")
    cmd = "sudo firewall-cmd --get-services"
    print(execute_shell(cmd))
    colour_print("#00FF00", "_________________________________________________________")


def fw_add_services():
    fw_get_services()
    service = Prompt.ask("Enter service name from above list")
    zone =  Prompt.ask("Enter zone", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = f"sudo firewall-cmd --add-service={service} --zone={zone} --permanent" 
    print(execute_shell(cmd))


def fw_add_sources():
    ip = Prompt.ask("\tEnter the ip address/mask")
    zone =  Prompt.ask("Enter zone", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = f"sudo firewall-cmd --add-source={ip} --zone={zone} --permanent" 
    print(execute_shell(cmd))


def fw_add_rule_menu():
    colour_print("#00FF00", "\t[1]Add Port")
    colour_print("#00FF00", "\t[2]Add services")
    colour_print("#00FF00", "\t[3]Add sources")
    colour_print("#00FF00", "\t[4]Back to Main menu")


def fw_add_rule():
    while True:
        fw_add_rule_menu()
        ch = Prompt.ask("Enter your option", choices=["1", "2", "3","4"])
        if ch == "1":
            fw_add_port()
        elif ch == "2":
            fw_add_services()
        elif ch == "3":
            fw_add_sources()
        elif ch == "4":
            break
        else:
            colour_print("red", "Wrong option!! Try again")


def fw_delete_rule_menu():
    colour_print("#00FF00", "\t[1]Delete Port")
    colour_print("#00FF00", "\t[2]Delete services")
    colour_print("#00FF00", "\t[3]Delete sources")
    colour_print("#00FF00", "\t[4]Back to Main menu")


def fw_delete_port():
    port = Prompt.ask("Enter port number")
    proto = Prompt.ask("Enter protocol", choices=["tcp","udp"],default="tcp")
    zone =  Prompt.ask("Enter zone", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = f"sudo firewall-cmd --remove-port={port}/{proto} --zone={zone} --permanent "
    print(execute_shell(cmd))


def fw_delete_services():
    fw_get_services()
    service = Prompt.ask("Enter service name from above list")
    zone =  Prompt.ask("Enter zone", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = f"sudo firewall-cmd --remove-service={service} --zone={zone} --permanent" 
    print(execute_shell(cmd))


def fw_delete_sources():
    ip = Prompt.ask("\tEnter the ip address/mask")
    zone =  Prompt.ask("Enter zone", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = f"sudo firewall-cmd --remove-source={ip} --zone={zone} --permanent" 
    print(execute_shell(cmd))


def fw_delete_rule():
    while True:
        fw_delete_rule_menu()
        ch = Prompt.ask("Enter your option", choices=["1", "2", "3","4"])
        if ch == "1":
            fw_delete_port()
        elif ch == "2":
            fw_delete_services()
        elif ch == "3":
            fw_delete_sources()
        elif ch == "4":
            break
        else:
            colour_print("red", "Wrong option!! Try again")


def fw_get_active_zones():
    zone = execute_shell("sudo firewall-cmd --get-active-zones")
    CONF["ZONE"] = zone.split("\n")[0]
    print(zone)


def fw_active_zone_details():
    #for zone in CONF["ZONE"].values():
    zone = CONF["ZONE"]
    cmd = f"sudo firewall-cmd --info-zone={zone}"
    print(execute_shell(cmd))



