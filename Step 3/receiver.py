##################
# receiver.py
# Sami Rothstein, Kate Wujciak, Rachel Moore
# This script receives data from the microbit attached to the pendulum.
# The accelerations in each axis (x, y, z) are converted into a readable
# tuple. This way we can read a files of a table of each acceleration vs.
# time for each length.
#################

#Import Statements
import microbit as mb
import radio  # Needs to be imported separately

#Main Script
radio.on()
radio.config(channel=1, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive()

    if incoming is not None: 
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        split = incoming.split(',')

        incoming = [int(split[0]), int(split[1]), int(split[2]), int(split[3])]
        incoming = tuple(incoming)
        print(incoming)

        mb.sleep(10)
