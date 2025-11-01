"""GPIO input helper using libgpiod to map GPIO lines to pygame key events.

This module uses the libgpiod Python bindings (imported as `gpiod`) and
listens for both-edge events on the specified BCM GPIO lines on `gpiochip0`.

Behavior:
- Posts pygame.KEYDOWN when a line has a rising edge (pressed/high).
- Posts pygame.KEYUP when a line has a falling edge (released/low).
- If `gpiod` is not available the module is a harmless no-op.

Wiring expectation: 3V3 -> button -> resistor -> input pin (active HIGH when pressed).
If you use pull-ups externally, the logic may need flipping or use active-low flags.
"""

import atexit
import threading
import time
import pygame

try:
    import gpiod
except Exception:
    print("Failed to import gpiod")
    gpiod = None

# BCM pin -> pygame key mapping requested by the user.
# Accept either an integer offset (e.g. 26) or a gpiod line name (e.g. 'GPIO26').
PIN_KEY_MAP = {
    # use the GPIO<nn> name style so tools like gpiomon work the same way
    "GPIO26": pygame.K_a,      # LEFT (A)  -> physical pin 37
    "GPIO19": pygame.K_d,      # RIGHT (D) -> physical pin 35
    "GPIO13": pygame.K_w,      # UP (W)    -> physical pin 33
    "GPIO6":  pygame.K_s,      # DOWN (S)  -> physical pin 31
    "GPIO5":  pygame.K_ESCAPE, # MENU (ESCAPE) -> physical pin 29
    "GPIO21": pygame.K_SPACE   # BUTTON_X (SPACE) -> physical pin 40
}

CHIP_NAME = "gpiochip0"

_initialized = False
_workers = []
_stop_event = None


def _line_worker(chip, pin, key, stop_event):
    """Worker that waits for edge events on a single line and posts pygame events."""
    try:
        line = chip.get_line(pin)
        # request both edges
        line.request(consumer="lego-arcade-gpio", type=gpiod.LINE_REQ_EV_BOTH_EDGES)
    except Exception:
        return

    while not stop_event.is_set():
        try:
            # wait for an event with timeout so we can react to stop_event periodically
            if line.event_wait(1):
                ev = line.event_read()
                if ev.event_type == gpiod.LineEvent.RISING:
                    print("UNPRESSED BUTTON")
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {"key": key}))
                elif ev.event_type == gpiod.LineEvent.FALLING:
                    print("PRESSED BUTTON")
                    pygame.event.post(pygame.event.Event(pygame.KEYUP, {"key": key}))
        except Exception:
            # if any error occurs, break the loop for this worker
            break

    try:
        line.release()
    except Exception:
        pass


def init():
    """Initialize gpiod listeners for configured pins.

    Safe to call multiple times. If `gpiod` is not installed this is a no-op.
    """
    global _initialized, _workers, _stop_event
    if _initialized:
        return
    if gpiod is None:
        _initialized = True
        return

    try:
        chip = gpiod.Chip(CHIP_NAME)
    except Exception:
        # cannot open the chip; behave as no-op
        _initialized = True
        return

    _stop_event = threading.Event()
    _workers = []

    for pin, key in PIN_KEY_MAP.items():
        # spawn a worker thread per pin; resilient to per-pin failures
        t = threading.Thread(target=_line_worker, args=(chip, pin, key, _stop_event), daemon=True)
        t.start()
        _workers.append(t)

    atexit.register(cleanup)
    _initialized = True


def cleanup():
    """Stop worker threads and release resources."""
    global _initialized, _workers, _stop_event
    if gpiod is None:
        _initialized = False
        return

    if _stop_event is not None:
        _stop_event.set()

    # give threads a moment to finish
    for t in _workers:
        try:
            t.join(timeout=0.5)
        except Exception:
            pass

    _workers = []
    _stop_event = None
    _initialized = False
