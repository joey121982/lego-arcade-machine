"""GPIO input helper to map Raspberry Pi GPIO pins to pygame key events.

This module is optional — if RPi.GPIO is not available it becomes a no-op so
the project can run on non-Pi machines.

Wired as: 3V3 -> button -> resistor -> input pin (active HIGH when pressed).
We use BCM numbering and enable a pull-down on inputs.
"""
import atexit
import pygame

try:
    import RPi.GPIO as GPIO
except Exception:
    GPIO = None

# BCM pin -> pygame key mapping requested by the user
PIN_KEY_MAP = {
    26: pygame.K_a,      # LEFT (A)
    19: pygame.K_d,      # RIGHT (D)
    13: pygame.K_w,      # UP (W)
    6:  pygame.K_s,      # DOWN (S)
    5:  pygame.K_ESCAPE, # MENU (ESCAPE)
    21: pygame.K_SPACE   # BUTTON_X (SPACE)
}

# debounce in milliseconds
BOUNCE_MS = 150

_initialized = False

def _gpio_callback_factory(pin, key):
    def _callback(channel):
        try:
            state = GPIO.input(channel)
            if state:
                ev = pygame.event.Event(pygame.KEYDOWN, {"key": key})
            else:
                ev = pygame.event.Event(pygame.KEYUP, {"key": key})
            # posting events from callback threads — pygame.event.post is thread-safe
            pygame.event.post(ev)
        except Exception:
            # swallow errors to avoid crashing the callback thread
            return
    return _callback

def init():
    """Initialize GPIO pins and attach event callbacks.

    Safe to call multiple times; if RPi.GPIO is not present this is a no-op.
    """
    global _initialized
    if _initialized:
        return
    if GPIO is None:
        _initialized = True
        return

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    for pin, key in PIN_KEY_MAP.items():
        try:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            cb = _gpio_callback_factory(pin, key)
            GPIO.add_event_detect(pin, GPIO.BOTH, callback=cb, bouncetime=BOUNCE_MS)
        except Exception:
            # ignore setup errors per-pin to be resilient to different hardware
            continue

    # ensure GPIO cleaned on exit
    atexit.register(cleanup)
    _initialized = True

def cleanup():
    global _initialized
    if GPIO is None:
        _initialized = False
        return
    try:
        GPIO.cleanup()
    except Exception:
        pass
    _initialized = False
