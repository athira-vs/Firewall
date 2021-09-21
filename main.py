#!/usr/bin/python3

from rich.prompt import Prompt
from firewall import *

while True:
    fw_get_status()
    colour_print("green", f"{'_'*20}MENU{'_'*20}")
    colour_print("green", "[1] Add rules")
    colour_print("green", "[2] Delete rules")
    colour_print("green", "[3] Get Active Zones")
    colour_print("green", "[4] Get Details of Active Zones")
    colour_print("green", "[5] Reload firewall")
    colour_print("red", "[6] Exit")

    ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,7)])
    
    if ch == '1':
        fw_add_rule()
    elif ch == '2':
        fw_delete_rule()
    elif ch == '3':
        fw_get_active_zones()
    elif ch == '4':
        fw_active_zone_details()
    elif ch == '5':
        fw_reload()
    elif ch == '6':
        break
    else:
        colour_print("red", "Wrong option!! Try again")