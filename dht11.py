# Module to read temperature and humidity with dht11 sensor
import dht
import machine

TPin = 2  # GPIO Pin


def temperatura():
    d = dht.DHT11(machine.Pin(5))

    d.measure()

    temperatura = d.temperature()
    umidita = d.humidity()

    print(d.temperature())
    print(d.humidity())
    return temperatura, umidita