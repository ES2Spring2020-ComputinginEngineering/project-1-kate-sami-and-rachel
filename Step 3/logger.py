##################
# logger.py
# Sami Rothstein, Kate Wujciak, Rachel Moore
# This script records data from the attached microbit used.
# The accelerations in each axis (x, y, z) are converted into a string
# and sent to the receiver over the radio.
#################

# Import Statements
import microbit as mb
import radio  # Needs to be imported separately

# Main Script
radio.on()
radio.config(channel=1, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed(): 
    mb.sleep(10)

radio.send('start') 
mb.sleep(1000)
mb.display.show(mb.Image.HEART)
time0 = mb.running_time()

while not mb.button_a.is_pressed():
    acc_x=(mb.accelerometer.get_x())
    acc_y=(mb.accelerometer.get_y())
    acc_z=(mb.accelerometer.get_z())
    time1 = mb.running_time()
    current_time = time1 - time0
    message = str(current_time) + ',' + str(acc_x) + ',' + str(acc_y) + ','+ str(acc_z)
    print(message)

    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)
