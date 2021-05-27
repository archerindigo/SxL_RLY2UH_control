#!/usr/bin/env python3
import sys, getopt, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
active_high = True  # default active high
relay1_pin = 20     # set the signal pin of relay 1 here
relay2_pin = 26     # set the signal pin of relay 2 here

def usage():
    print("Usage:")
    print("%s -r <1|2> [-t <s>] [-lh] <on|off>" % sys.argv[0])
    print("\t-r <1|2>\t: select relay 1 or 2")
    print("\t<on|off|\t: turn on / off the relay")
    print("\t-l\t\t: use active LOW logic")
    print("\t-t <s>\t: delay the operation by s seconds")
    print("\t-h\t\t: show this help")

def relay_control(relay_pin, active_high, on):
    GPIO.setup(relay_pin, GPIO.OUT)     # set the pin to output

    # Output signal to the pin
    if on == True:
        GPIO.output(relay_pin, active_high)     # if active_high == True, we should output HIGH (True)
    else:
        GPIO.output(relay_pin, not active_high) # if active_high == False, we should output LOW (False)

if __name__ == "__main__":

    target_relay = -1
    delay_sec = -1

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'r:t:lh')
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            usage()
        if opt == "-r":
            if arg == "1":
                target_relay = relay1_pin
            elif arg == "2":
                target_relay = relay2_pin
            else:
                usage()
                sys.exit(2)
        if opt == "-l":
            active_high=False
        if opt == "-t":
            delay_sec = int(arg)

    if target_relay == -1 or not args:
        print("Unknown operation!")
        usage()
        sys.exit(1)

    if delay_sec > 0:
        print("Operation in %d seconds..." % delay_sec)
        time.sleep(delay_sec)

    # Control the relay based on input arguments
    if args[0] == "on":
        relay_control(target_relay, active_high, True)
    elif args[0] == "off":
        relay_control(target_relay, active_high, False)
    else:
        print("Unknown operation!")
        usage()
