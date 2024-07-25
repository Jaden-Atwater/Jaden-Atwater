import time
from Motor import *
import RPi.GPIO as GPIO





class Line_Tracking:
    def __init__(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01, GPIO.IN)
        GPIO.setup(self.IR02, GPIO.IN)
        GPIO.setup(self.IR03, GPIO.IN)

    def correction(self):

        print("Self correction...")
        PWM.setMotorModel()

    def stop(self):
        print("Stopping motors...")
        PWM.setMotorModel(0, 0, 0, 0)
        time.sleep(0.5)

    def backup(self):

        print("Backing up...")
        PWM.setMotorModel(-200, -200,-200, -200)
        time.sleep(1)
        self.stop()

    def turnRight(self):
        print("Turning right...")
        PWM.setMotorModel(1000, 1000, -2000, -2000)
        time.sleep(0.40)
        self.stop()

    def slightRight(self):
        print("Slight right turn...")
        PWM.setMotorModel(800, 800, -800, -800)
        time.sleep(0.8)
        self.stop()

    def turnLeft(self):
        print("Turning left...")
        PWM.setMotorModel(-2000, -2000, 1000, 1000)
        time.sleep(0.40)
        self.stop()

    def slightLeft(self):
        print("Slight left turn...")
        PWM.setMotorModel(890, 890, -890, -890)
        time.sleep(0.8)

    def straight(self):
        #print("Going straight...")
        PWM.setMotorModel(520, 520, 520, 520)

    def selfcorrection(self):

        print("Self correction...")

        if self.LMR == 7:

            self.turnRight()
            time.sleep(0.5) 
            #self.straight()
            #self.correction()

    


    def correction(self):

        #print("Run Function...")

        if self.LMR != 1 and self.LMR != 2 and self.LMR != 4 :

            self.straight()

        elif self.LMR == 1 and self.LMR == 2:

            self.slightRight()

        else:

            if self.LMR == 2 and self.LMR == 4:

                self.slightLeft()

     


    # def correction(self):

    #     print("Self correction...")
    #     self.backup()

    #     if self.LMR == 1 and self.LMR == 2:

    #         self.turnRight()

    #     else:
            
    #         if self == 2 and self.LMR == 4:

    #             self.turnLeft()


    def run(self):
        print("Starting run loop...")
        while True:
            self.LMR = 0x00
            
            #if find ball returns true
            #stop moving
            #take a picture
            #move forward till gpio.input(self.IR01) == 7
            #back up
            #continue

            #call the find ball function with an argument that's at index 0 of the list
            #when it finds 

            # Read sensor inputs
            if GPIO.input(self.IR01):
                self.LMR |= 4
            if GPIO.input(self.IR02):
                self.LMR |= 2
            if GPIO.input(self.IR03):
                self.LMR |= 1
            
            #print(f"LMR value: {self.LMR}")
            
            # Motor control based on sensor readings


            if self.LMR == 7:
                print("All sensors detected")
                self.correction()
                self.backup()
                self.turnRight()

            elif self.LMR == 1 and self.LMR == 2:

                self.slightLeft()
                
            elif self.LMR == 2:
                print("LMR = 2: Going straight")
                self.straight()
            elif self.LMR == 4:
                print("LMR = 4: Turning right")
                self.turnRight()
            elif self.LMR == 1:
                print("LMR = 1: Turning left")
                self.turnLeft()
            elif self.LMR == 1 and self.LMR == 2:
                print ("Making a slight right")
                self.slightLeft()
            elif self.LMR == 2 and self.LMR == 4:
                print ("Making a slight left")
                self.slightRight()
            else:
                print("No clear path, going straight...")
                self.straight()
                self.correction()
                

# Instantiate the Line_Tracking class
infrared = Line_Tracking()

# Main program logic follows:
if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        #open file with the order to find the balls
        #pass the order into the run function
        infrared.run()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping motors...")
        PWM.setMotorModel(0, 0, 0, 0)
