def on_received_string(receivedString):
    global OdbockaL, OdbockaP, Turnaround
    if receivedString == "ProhodBarvy":
        L = barvaLinie
        O = barvaOkoli
        barvaLinie = O
        barvaOkoli = L
    if receivedString == "OdbockaL":
        if OdbockaL == True:
            OdbockaL = False
        else:
            OdbockaL = True
            odbockaP = False

    if receivedString == "OdbockaP":
        if OdbockaP == True:
            OdbockaP = False
        else:
            OdbockaL = False
            OdbockaP = True
    if receivedString == "Otocka":
        if Turnaround == True:
            Turnaround = False
        else:
            Turnaround = True
    if receivedString == "TurnBackL":
        TurnBackL = True
        TurnBackR = False
    if receivedString == "TurnBackR":
        TurnBackL = False
        TurnBackR = True

radio.on_received_string(on_received_string)





barvaLinie = 1 #funguje tak cerna i bila paska
barvaOkoli = 0
OdbockaL = False
OdbockaP = False
first = True
Turnaround = False
def turnrightR():
    pins.analog_write_pin(AnalogPin.P1, 600)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)
def turnleftL():
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, 600)
    pins.digital_write_pin(DigitalPin.P12, 1)
def turnbackR():
    global first
    if first and pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
        turnrightR()
    elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
        turnrightR()
        first = False
    elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
        turnrightR()
    elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
        first = True
        Turnaround = False
def turnbackL():
    global first
    if first and pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
        turnleftL()
    elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
        turnleftL
        first = False
    elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
        turnleftL
    elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
        first = True
        Turnaround = False
def turnright():
    pins.analog_write_pin(AnalogPin.P1, 600)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, 100)
    pins.digital_write_pin(DigitalPin.P12, 1)
    item = 0
def stop():
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.analog_write_pin(AnalogPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
def forward():
    pins.analog_write_pin(AnalogPin.P1, 600)
    pins.analog_write_pin(AnalogPin.P2, 600)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
def turnleft():
    pins.analog_write_pin(AnalogPin.P1, 100)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, 600)
    pins.digital_write_pin(DigitalPin.P12, 1)
def backward():
    pins.analog_write_pin(AnalogPin.P1, -600)
    pins.analog_write_pin(AnalogPin.P2, -600)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
led.enable(False)
pins.set_pull(DigitalPin.P4, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P5, PinPullMode.PULL_UP)
TurnBackL = False
TurnBackR = True
def on_forever():
    radio.set_group(77)
    if Turnaround:
        if TurnBackR:
            turnbackR()
        elif TurnBackL:
            turnbackL()
    elif OdbockaL:
        if pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
            turnleft()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
            forward()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
            backward()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
            turnleft()
    elif OdbockaP:
        if pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
            turnright()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
            turnright()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
            backward()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
            forward()
    elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
        forward()
    elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
        backward()
    elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
        turnright()
    elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
        turnleft()
basic.forever(on_forever)
