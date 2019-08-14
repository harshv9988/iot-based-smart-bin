import smtplib
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN)
GPIO.setup(8,GPIO.IN)
flag1=1
def mail():
    global flag1
    i=GPIO.input(10)
    j=GPIO.input(8)
    if i==1 and j==1:
        if flag1==2:
            smtpuser = "your email id"
            smtppass = "password"

            toadd = "email on which file to be sent"
            fromadd = smtpuser
            subject = "Python Test"
            header = "To: "+toadd+'\n'+"From: "+fromadd+'\n'+"Subject: "+subject+'\n'
            body = "full"
            message = header+'\n'+body
    
            print(message)

            s = smtplib.SMTP("smtp.gmail.com",587)

            s.ehlo()
            s.starttls()
            s.ehlo()
            
            s.login(smtpuser, smtppass)
            s.sendmail(fromadd, toadd, message)
            s.quit()
            flag1=3
    elif i==1 and j==0:
        if flag==1:
            smtpuser = "your email id"
            smtppass = "password"

            toadd = "email id on which file to be sent"
            fromadd = smtpuser
            subject = "Python Test"
            header = "To: "+toadd+'\n'+"From: "+fromadd+'\n'+"Subject: "+subject+'\n'
            body = "half"
            message = header+'\n'+body
    
            print(message)

            s = smtplib.SMTP("smtp.gmail.com",587)

            s.ehlo()
            s.starttls()
            s.ehlo()
            
            s.login(smtpuser, smtppass)
            s.sendmail(fromadd, toadd, message)
            s.quit()
            flag1=2
    elif i==0 and j==0:
        flag1=1
#!/usr/bin/python

# Date   : 28/01/2013

# -----------------------
# 
# -----------------------

# -----------------------
# Define some functions
# -----------------------

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(2,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(2,False)
    pwm.ChangeDutyCycle(duty)

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers

GPIO.setup(3,GPIO.OUT)

pwm = GPIO.PWM(3,50)

# Define GPIO to use on Pi
GPIO_TRIGGER = 16
GPIO_ECHO    = 18
flag = False

print ("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  while True:
    distance = measure_average()
    print ("Distance : %.1f" % distance)
    if distance < 30 :
        if flag == False :
            pwm.start(0)
            SetAngle(0)
            print("open")
            flag = True
    elif flag == True:
        pwm.start(1)
        SetAngle(90)
        print("closed")
        flag = False
    else:
        mail()
        
    
    time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()



    




