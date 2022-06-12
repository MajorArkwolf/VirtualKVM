from system import System

def SwapUSBSwitch(system_from: System, system_to: System):
    if (system_from.id == system_to):
        # No op
        return