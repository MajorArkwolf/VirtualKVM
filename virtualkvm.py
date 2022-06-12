import argparse
from system import System
from swapdisplay import SwapDisplay
from swapusb import SwapUSBSwitch

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fro", help = "The computer from", type=int, default=-1)
parser.add_argument("-t", "--to", help = "The computer to", type=int, default=-1)
parser.add_argument("-a", "--all", help = "swap all")
parser.add_argument("-u", "--usb", help = "swap usb switch")
parser.add_argument("-d", "--display", help = "swap display")
args = parser.parse_args()

def main():
    swap_display: bool = args.display != None or args.all != None
    swap_usb: bool = args.usb != None or args.all != None

    if (swap_display == False and swap_usb == False):
        print("No operation selected, exiting")
        return

    # ID 0 in array is Windows PC and 0x0f is Displayport 1
    # ID 1 in array is Mac Mini m1 and 0x10 is Displayport 2
    systems = [ System(0, "0x0f"), System(1, "0x10") ]
    size = len(systems)
    if args.fro > size or args.fro < 0 or args.to > size or args.to < 0:
        print("ID was out of range of systems")
        return

    system_from: System = systems[args.fro]
    system_to: System = systems[args.to]
    
    if (swap_display):
        SwapDisplay(system_from, system_to, 1)
    if (swap_usb):
        SwapUSBSwitch(system_from, system_to)

if __name__ == "__main__":
    main()
