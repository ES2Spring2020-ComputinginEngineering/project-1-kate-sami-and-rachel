##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=1, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        split = incoming.split(',')
#         current_time = int(split[0])
#         acc_x = int(split[1])
#         acc_y = int(split[2])
#         acc_z = int(split[3])

        incoming = [int(split[0]), int(split[1]), int(split[2]), int(split[3])]
        incoming = tuple(incoming)
        print(incoming)


        # Incoming is string sent from logger
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################

        mb.sleep(10)
