function RegistraNumero (numero_uscito: number) {
    if (numero_uscito == 1) {
        uno += 1
    } else if (numero_uscito == 2) {
        due += 1
    } else if (numero_uscito == 3) {
        tre += 1
    } else if (numero_uscito == 4) {
        quattro += 1
    } else if (numero_uscito == 5) {
        cinque += 1
    } else {
        sei += 1
    }
}
input.onGesture(Gesture.Shake, function () {
    numero_uscito = LanciaDado()
    MostraFaccia(numero_uscito)
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.OnceInBackground)
    RegistraNumero(numero_uscito)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("1: " + uno + " 2: " + due + " 3: " + tre + " 4: " + quattro + " 5: " + cinque + " 6: " + sei)
})
function LanciaDado () {
    for (let index = 0; index < 16; index++) {
        MostraFaccia(randint(1, 6))
        basic.pause(50)
    }
    return randint(1, 6)
}
function MostraFaccia (num: number) {
    if (num == 1) {
        faccia1.showImage(0)
    } else if (num == 2) {
        faccia2.showImage(0)
    } else if (num == 3) {
        faccia3.showImage(0)
    } else if (num == 4) {
        faccia4.showImage(0)
    } else if (num == 5) {
        faccia5.showImage(0)
    } else {
        faccia6.showImage(0)
    }
}
let numero_uscito = 0
let sei = 0
let cinque = 0
let quattro = 0
let tre = 0
let due = 0
let uno = 0
let faccia6: Image = null
let faccia5: Image = null
let faccia4: Image = null
let faccia3: Image = null
let faccia2: Image = null
let faccia1: Image = null
faccia1 = images.createImage(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
faccia2 = images.createImage(`
    . . . . .
    . # . . .
    . . . . .
    . . . # .
    . . . . .
    `)
faccia3 = images.createImage(`
    # . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . #
    `)
faccia4 = images.createImage(`
    . . . . .
    . # . # .
    . . . . .
    . # . # .
    . . . . .
    `)
faccia5 = images.createImage(`
    # . . . #
    . . . . .
    . . # . .
    . . . . .
    # . . . #
    `)
faccia6 = images.createImage(`
    . # . # .
    . . . . .
    . # . # .
    . . . . .
    . # . # .
    `)
uno = 0
due = 0
tre = 0
quattro = 0
cinque = 0
sei = 0
basic.forever(function () {
	
})
