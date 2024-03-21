import badger2040
from badger2040 import WIDTH

TEXT_SIZE = 1
LINE_HEIGHT = 15

display = badger2040.Badger2040()
display.led(128)

# Clear to white
display.set_pen(15)
display.clear()

display.set_font("bitmap8")
display.set_pen(0)

display.rectangle(0, 0, WIDTH, 16)
display.set_pen(15)
display.text("New App", 3, 4, WIDTH, 1)
display.text("Write your code here!", 150,4, scale = 1)

display.set_pen(0)

y = 16 + int(LINE_HEIGHT / 2)

display.text("What are you going to create?", 5, y, scale = 2)
y += LINE_HEIGHT


display.update()

# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    display.keepalive()
    display.halt()