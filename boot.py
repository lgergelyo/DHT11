# This file is executed on every boot (including wake-boot from deepsleep)
import esp


# esp.osdebug(None)
# Connects to the wifi AP providing a hostname, AP Name and passord
def do_connect():
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        # Sets the device hostname
        sta_if.config(dhcp_hostname='ESP_ROOM1')
        print(sta_if.config('dhcp_hostname'))
        # CHANGE THE VALUES TO YOUR ACCESSPOINT NAME AND PASSWORD
        sta_if.connect('gergely', 'vW7u545n')
        while not sta_if.isconnected():
            pass

    print('network config:', sta_if.ifconfig())


# Imports various modules for network, webrepl and garbage collector
import gc
import webrepl
import network

do_connect()
webrepl.start()
gc.collect()