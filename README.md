# Project1
Project 1 Starter Code

Names: Sami, Kate, Rachel
Team Name: Group 1

Your primary tasks will be to:

- build a pendulum,
- use theoretical equations (from physics) to calculate the period of the pendulum,
- collect real-world experimental data from your pendulum,
- create a computer simulation of your pendulum numerically,
- plot and extract meaningful results 2 through 4

Your final submission should include (on GitHub):

All of your updated Python files
A README.md file explaining what .py files to run to get your results
A .pdf file containing your final plots and a brief report and discussion of results
At least five micro:bit data files from a pendulum for testing your parsing code.


In order to find the theoretical period of our pendulum, run step1_theoretical_period.py, located in the Step 2 folder. This will give the graphs of the theoretical period vs. lengths disregarding friction and air resistance. We collected our real world data by using the files named logger.py and receiver.py. Our logger is used to collect data on the motion of the pendulum for the 3 accelerations, while the receiver is used to convert the received data into code that can be used with the MU plotter. In order to view the acceleration v time graphs and code, run the file named acceleration vs time located in the step 4 folder. This will allow you to view the X and Y accelerations vs. time for each of our 5 lengths. In order to view our calculations and graphs for theta vs. time, run the file step 4 theta v time. Use this same file to run the period calculation and our graph which shows period v length. In order to view our numerical simulation, run the file step 5 simulation.