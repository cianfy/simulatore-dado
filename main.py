def on_button_pressed_a():
    for index in range(10):
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.SMALL_HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def RegistraNumero(numero_uscito: number):
    global uno, due, tre, quattro, cinque, sei
    if numero_uscito == 1:
        uno += 1
    elif numero_uscito == 2:
        due += 1
    elif numero_uscito == 3:
        tre += 1
    elif numero_uscito == 4:
        quattro += 1
    elif numero_uscito == 5:
        cinque += 1
    else:
        sei += 1

def on_gesture_shake():
    global numero_uscito2
    makerbit.clear_lcd1602()
    makerbit.show_string_on_lcd1602("Sto lanciando",
        makerbit.position1602(LcdPosition1602.POS1),
        16,
        TextOption.ALIGN_CENTER)
    makerbit.show_string_on_lcd1602("il dado!",
        makerbit.position1602(LcdPosition1602.POS17),
        16,
        TextOption.ALIGN_CENTER)
    numero_uscito2 = LanciaDado()
    MostraFaccia(numero_uscito2)
    music.start_melody(music.built_in_melody(Melodies.BA_DING),
        MelodyOptions.ONCE_IN_BACKGROUND)
    RegistraNumero(numero_uscito2)
    makerbit.clear_lcd1602()
    makerbit.show_string_on_lcd1602("E' uscito",
        makerbit.position1602(LcdPosition1602.POS1),
        16,
        TextOption.ALIGN_CENTER)
    makerbit.show_string_on_lcd1602("il " + str(numero_uscito2) + " !!!",
        makerbit.position1602(LcdPosition1602.POS17),
        16,
        TextOption.ALIGN_CENTER)
    basic.pause(2000)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    makerbit.clear_lcd1602()
    if numero_uscito2 == 0:
        makerbit.show_string_on_lcd1602("Non hai ancora",
            makerbit.position1602(LcdPosition1602.POS1),
            16,
            TextOption.ALIGN_CENTER)
        makerbit.show_string_on_lcd1602("lanciato il dado",
            makerbit.position1602(LcdPosition1602.POS17),
            16,
            TextOption.ALIGN_CENTER)
    else:
        makerbit.show_string_on_lcd1602("L'ultimo numero",
            makerbit.position1602(LcdPosition1602.POS1),
            16,
            TextOption.ALIGN_CENTER)
        makerbit.show_string_on_lcd1602("uscito è il " + str(numero_uscito2),
            makerbit.position1602(LcdPosition1602.POS17),
            16,
            TextOption.ALIGN_CENTER)
    basic.pause(2000)
input.on_button_pressed(Button.B, on_button_pressed_b)

def LanciaDado():
    for index2 in range(8):
        MostraFaccia(randint(1, 6))
        basic.pause(50)
    return randint(1, 6)
def MostraFaccia(num: number):
    if num == 1:
        faccia1.show_image(0)
    elif num == 2:
        faccia2.show_image(0)
    elif num == 3:
        faccia3.show_image(0)
    elif num == 4:
        faccia4.show_image(0)
    elif num == 5:
        faccia5.show_image(0)
    else:
        faccia6.show_image(0)
numero_uscito2 = 0
faccia6: Image = None
faccia5: Image = None
faccia4: Image = None
faccia3: Image = None
faccia2: Image = None
faccia1: Image = None
makerbit.connect_lcd(39)
makerbit.show_string_on_lcd1602("Lancia dado",
    makerbit.position1602(LcdPosition1602.POS1),
    16,
    TextOption.ALIGN_CENTER)
makerbit.show_string_on_lcd1602("CLASSE 2D",
    makerbit.position1602(LcdPosition1602.POS17),
    16,
    TextOption.ALIGN_CENTER)
faccia1 = images.create_image("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
""")
faccia2 = images.create_image("""
    . . . . .
        . # . . .
        . . . . .
        . . . # .
        . . . . .
""")
faccia3 = images.create_image("""
    . . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . .
""")
faccia4 = images.create_image("""
    . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
""")
faccia5 = images.create_image("""
    . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
""")
faccia6 = images.create_image("""
    . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
""")
uno = 0
due = 0
tre = 0
quattro = 0
cinque = 0
sei = 0
numero_uscito2 = 0
basic.pause(2000)
makerbit.clear_lcd1602()

def on_forever():
    makerbit.show_string_on_lcd1602("1=" + str(uno) + " 2=" + str(due) + " 3= " + str(tre),
        makerbit.position1602(LcdPosition1602.POS1),
        16,
        TextOption.ALIGN_CENTER)
    makerbit.show_string_on_lcd1602("4=" + str(quattro) + " 5=" + str(cinque) + " 6= " + str(sei),
        makerbit.position1602(LcdPosition1602.POS17),
        16,
        TextOption.ALIGN_CENTER)
basic.forever(on_forever)
