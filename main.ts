input.onSound(DetectedSound.Quiet, function () {
    pins.servoWritePin(AnalogPin.P1, randint(38, 145))
})
led.enable(false)
pins.servoWritePin(AnalogPin.P1, 90)
basic.pause(5000)