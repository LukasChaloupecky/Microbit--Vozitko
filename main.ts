let rychlost_vetsi = 600
// pro usnadnění 
let rychlost_mensi = 100
// pro usnadnění 
let rychlost_otaceni = 600
// pro usnadnění 
let barvaLinie = 1
// funguje tak cerna i bila paska
let barvaOkoli = 0
// funguje tak cerna i bila paska
let OdbockaL = false
// u odbocky vleva
let OdbockaP = false
// u odbocky vprava
let first = true
// dulezita hloupost k otaceni na druhou stranu
let Turnaround = false
// variable pro příkaz pro otoceni
let TurnBackL = false
// otaceni dozadu vlevo
let TurnBackR = true
// otaceni dozadu vpravo
pins.setPull(DigitalPin.P4, PinPullMode.PullUp)
// nevim
pins.setPull(DigitalPin.P5, PinPullMode.PullUp)
// nevim
led.enable(false)
// nevim
// #####################################################################xx
radio.onReceivedString(function on_received_string(receivedString: string) {
    let L: number;
    let O: number;
    let barvaLinie: number;
    let barvaOkoli: number;
    let odbockaP: boolean;
    let TurnBackL: boolean;
    let TurnBackR: boolean;
    
    if (receivedString == "ProhodBarvy") {
        L = barvaLinie
        O = barvaOkoli
        barvaLinie = O
        barvaOkoli = L
    }
    
    if (receivedString == "OdbockaL") {
        if (OdbockaL == true) {
            OdbockaL = false
        } else {
            OdbockaL = true
            odbockaP = false
        }
        
    }
    
    if (receivedString == "OdbockaP") {
        if (OdbockaP == true) {
            OdbockaP = false
        } else {
            OdbockaL = false
            OdbockaP = true
        }
        
    }
    
    if (receivedString == "Otocka") {
        if (Turnaround == true) {
            Turnaround = false
        } else {
            Turnaround = true
        }
        
    }
    
    if (receivedString == "TurnBackL") {
        TurnBackL = true
        TurnBackR = false
    }
    
    if (receivedString == "TurnBackR") {
        TurnBackL = false
        TurnBackR = true
    }
    
})
// #####################################################################xx
function turnrightR() {
    pins.analogWritePin(AnalogPin.P1, rychlost_otaceni)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

function turnleftL() {
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, rychlost_otaceni)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

function turnbackR() {
    let Turnaround: boolean;
    
    if (first && pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
        turnrightR()
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
        turnrightR()
        first = false
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
        turnrightR()
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
        first = true
        Turnaround = false
    }
    
}

function turnbackL() {
    let Turnaround: boolean;
    
    if (first && pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
        turnleftL()
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
        turnleftL
        first = false
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
        turnleftL
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
        first = true
        Turnaround = false
    }
    
}

// #####################################################################xx
function turnright() {
    pins.analogWritePin(AnalogPin.P1, rychlost_vetsi)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, rychlost_mensi)
    pins.digitalWritePin(DigitalPin.P12, 1)
    let item = 0
}

function stop() {
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P12, 0)
}

function forward() {
    pins.analogWritePin(AnalogPin.P1, rychlost_vetsi)
    pins.analogWritePin(AnalogPin.P2, rychlost_vetsi)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

function turnleft() {
    pins.analogWritePin(AnalogPin.P1, rychlost_mensi)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, rychlost_vetsi)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

function backward() {
    pins.analogWritePin(AnalogPin.P1, -1 * rychlost_vetsi)
    pins.analogWritePin(AnalogPin.P2, -1 * rychlost_vetsi)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

// #####################################################################xx
basic.forever(function on_forever() {
    radio.setGroup(77)
    if (Turnaround) {
        if (TurnBackR) {
            turnbackR()
        } else if (TurnBackL) {
            turnbackL()
        }
        
    } else if (OdbockaL) {
        if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
            turnleft()
        } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
            forward()
        } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
            backward()
        } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
            turnleft()
        }
        
    } else if (OdbockaP) {
        if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
            turnright()
        } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
            turnright()
        } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
            backward()
        } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
            forward()
        }
        
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
        forward()
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
        backward()
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaOkoli && pins.digitalReadPin(DigitalPin.P5) == barvaLinie) {
        turnright()
    } else if (pins.digitalReadPin(DigitalPin.P4) == barvaLinie && pins.digitalReadPin(DigitalPin.P5) == barvaOkoli) {
        turnleft()
    }
    
})
