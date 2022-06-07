rychlost_vetsi = 600    #pro usnadnění 
rychlost_mensi = 100    #pro usnadnění 
rychlost_otaceni = 600  #pro usnadnění 

automaticke_ovladani = True #False při ovládání ovladačem


barvaLinie = 1 #funguje tak cerna i bila paska
barvaOkoli = 0 #funguje tak cerna i bila paska


OdbockaL = False #u odbocky vleva
OdbockaP = False #u odbocky vprava

first = True #dulezita hloupost k otaceni na druhou stranu
Turnaround = False #variable pro příkaz pro otoceni

TurnBackL = False #otaceni dozadu vlevo
TurnBackR = True  #otaceni dozadu vpravo


pins.set_pull(DigitalPin.P4, PinPullMode.PULL_UP) #nevim
pins.set_pull(DigitalPin.P5, PinPullMode.PULL_UP)#nevim
led.enable(False) #nevim

######################################################################xx


def on_received_string(receivedString):
    global OdbockaL, OdbockaP, Turnaround, TurnBackL, TurnBackR, barvaLinie, barvaOkoli, automaticke_ovladani
    if receivedString == "KontrolaNadVozítkemPřesOvladač":
        if automaticke_ovladani:
            automaticke_ovladani = False
        else:
            automaticke_ovladani = True
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



######################################################################xx



def turnrightR():  #funkce umožnující otočku vzadu vpravo
    pins.analog_write_pin(AnalogPin.P1, rychlost_otaceni) 
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)

def turnleftL(): #funkce umožnující otočku vzadu vlevo
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, rychlost_otaceni)
    pins.digital_write_pin(DigitalPin.P12, 1)


def turnbackR(): #funkce vykonávající otočku dozadu vpravo
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

def turnbackL(): #funkce vykonávající otočku dozadu vlevo
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


######################################################################xx

def turnright(): #klasické vprava
    pins.analog_write_pin(AnalogPin.P1, rychlost_vetsi)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, rychlost_mensi)
    pins.digital_write_pin(DigitalPin.P12, 1)
def stop(): #funkce stop
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.analog_write_pin(AnalogPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
def forward(): #klasické vpřed
    pins.analog_write_pin(AnalogPin.P1, rychlost_vetsi)
    pins.analog_write_pin(AnalogPin.P2, rychlost_vetsi)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
def turnleft(): #klasické vlevo
    pins.analog_write_pin(AnalogPin.P1, rychlost_mensi)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.analog_write_pin(AnalogPin.P2, rychlost_vetsi)
    pins.digital_write_pin(DigitalPin.P12, 1)
def backward(): #klasické vzad-MOŽNÁ NEFUNGUJE-negativní rychlost
    pins.analog_write_pin(AnalogPin.P1, -1*rychlost_vetsi)
    pins.analog_write_pin(AnalogPin.P2, -1*rychlost_vetsi)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)

######################################################################xx

#      AUTOMATICKÉ OVLÁDÁNÍ
def on_forever():
    radio.set_group(77) #radio group
    if automaticke_ovladani:
        ##################################
        if Turnaround:
            if TurnBackR:
                turnbackR()  #funkce pro otoceni vzadu (L/P)
            elif TurnBackL:
                turnbackL()
        ##################################

                    # funkce pro odpocku u krizovatky (L/P)
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
        ###############################
                # NORMÁLNÍ AUTOMATICKÁ JÍZDA
        elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
            forward()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
            backward()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaOkoli and pins.digital_read_pin(DigitalPin.P5) == barvaLinie:
            turnright()
        elif pins.digital_read_pin(DigitalPin.P4) == barvaLinie and pins.digital_read_pin(DigitalPin.P5) == barvaOkoli:
            turnleft()
basic.forever(on_forever)

#######################################################################
#       OVLÁDÁNÍ PŘES OVLADAČ
def on_received_number(receivedNumber):
    if automaticke_ovladani == False:
        if receivedNumber == 1: #dopředu
            forward()
        if receivedNumber == 2: #doleva
            turnleft()
        if receivedNumber == 3: #doprava
            turnright()
        if receivedNumber == 4: #dozadu
            backward()
    radio.on_received_number(on_received_number)