#!/usr/bin/env python3

"""
This script monitors Raspberry Pi GPIO pins and translates button presses
into keyboard key presses using the 'uinput' kernel module.

It uses the 'gpiozero' library for GPIO interaction.

This script must be run as root for write access to /dev/uinput.
"""

import uinput
from gpiozero import Button
import signal
import time

PIN_TO_KEY_MAP = {
    26: uinput.KEY_SPACE,
    19: uinput.KEY_S,  
    13: uinput.KEY_ESC,
    6:  uinput.KEY_W,  
    5:  uinput.KEY_A,   
    20: uinput.KEY_D,  
    21: uinput.KEY_ENTER,
}

ENABLED_KEYS = tuple(PIN_TO_KEY_MAP.values())

try:
    device = uinput.Device(ENABLED_KEYS, name="gpio-keyboard")
except Exception as e:
    print(f"Error creating uinput device: {e}")
    print("Please ensure you have write permissions to /dev/uinput.")
    print("Run the setup steps in 'setup_instructions.md'.")
    exit(1)

buttons = []

def handle_press(button):
    """
    Callback function for when a button is pressed.
    Finds the corresponding key and emits a 'press' event.
    """
    key = PIN_TO_KEY_MAP.get(button.pin.number)
    if key:
        print(f"Pin {button.pin.number} PRESSED -> Key {key[1]}")
        device.emit(key, 1)  # 1 = Key press

def handle_release(button):
    """
    Callback function for when a button is released.
    Finds the corresponding key and emits a 'release' event.
    """
    key = PIN_TO_KEY_MAP.get(button.pin.number)
    if key:
        print(f"Pin {button.pin.number} RELEASED -> Key {key[1]}")
        device.emit(key, 0)  # 0 = Key release

def main():
    print("Starting GPIO keyboard service...")
    print(f"Monitoring {len(PIN_TO_KEY_MAP)} pins.")

    try:
        # Initialize all buttons
        for pin_number in PIN_TO_KEY_MAP.keys():
            # pull_up=False configures the pin to use the internal pull-down
            # resistor. This is correct for wiring a button
            # from the GPIO pin to the 3.3V pin.
            # bouncetime=0.05 adds 50ms of debouncing.
            button = Button(pin_number, pull_up=False, bounce_time=0.05)

            button.when_pressed = handle_press
            button.when_released = handle_release

            buttons.append(button)

        print("Service running. Press Ctrl+C to exit.")
        signal.pause()

    except KeyboardInterrupt:
        print("\nCaught Ctrl+C. Exiting gracefully.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Cleaning up...")

if __name__ == "__main__":
    main()