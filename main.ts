radio.onReceivedString(function on_received_string(receivedString: string) {
    let L: any;
    let O: any;
    let barvaLinie: any;
    let barvaOkoli: any;
    let odbockaP: boolean;
    
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
    
})
let barvaLinie = 1
// funguje tak cerna i bila paska
let barvaOkoli = 0
let OdbockaL = false
let OdbockaP = false
let first = true
let Turnaround = false
function turnrightR() {
    pins.analogWritePin(AnalogPin.P1, 600)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

function turnleftL() {
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, 600)
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

function turnright() {
    pins.analogWritePin(AnalogPin.P1, 600)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, 100)
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
    pins.analogWritePin(AnalogPin.P1, 600)
    pins.analogWritePin(AnalogPin.P2, 600)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

function turnleft() {
    pins.analogWritePin(AnalogPin.P1, 100)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.analogWritePin(AnalogPin.P2, 600)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

function backward() {
    pins.analogWritePin(AnalogPin.P1, -600)
    pins.analogWritePin(AnalogPin.P2, -600)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
}

led.enable(false)
pins.setPull(DigitalPin.P4, PinPullMode.PullUp)
pins.setPull(DigitalPin.P5, PinPullMode.PullUp)
basic.forever(function on_forever() {
    radio.setGroup(77)
    if (Turnaround) {
        turnbackR()
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
