from system import System
import requests

def SwapDisplay(system_from: System, system_to: System, display_number: int = 1):
    x = requests.get(f'http://192.168.128.187:3485/{display_number}/input/{system_to.display_source}')
    return