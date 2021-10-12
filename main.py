def on_sound_quiet():
    pins.servo_write_pin(AnalogPin.P0, randint(38, 145))
input.on_sound(DetectedSound.QUIET, on_sound_quiet)

led.enable(False)
pins.servo_write_pin(AnalogPin.P0, 90)
strip = neopixel.create(DigitalPin.P1, 17, NeoPixelMode.RGB)

def on_every_interval():
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P10, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P10, 0)
    pins.digital_write_pin(DigitalPin.P13, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P13, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P12, 0)
loops.every_interval(randint(1000, 4000), on_every_interval)

def on_every_interval2():
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(50)
    pins.digital_write_pin(DigitalPin.P12, 0)
    basic.pause(50)
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(50)
    pins.digital_write_pin(DigitalPin.P12, 0)
    basic.pause(50)
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(50)
    pins.digital_write_pin(DigitalPin.P12, 0)
    basic.pause(50)
loops.every_interval(10000, on_every_interval2)

def on_forever():
    while True:
        strip.show_color(neopixel.rgb(25, 0, 5))
        strip.show()
        for index in range(18):
            strip.rotate(1)
            strip.set_pixel_color(index, neopixel.colors(NeoPixelColors.WHITE))
            strip.set_pixel_color(index - 1, neopixel.rgb(255, 0, 50))
            strip.set_pixel_color(index + 1, neopixel.rgb(255, 0, 50))
            basic.pause(40)
            strip.show()
basic.forever(on_forever)
