import RPi.GPIO as IO
import requests
import time

#r = requests.post("http://f30f71f1.ngrok.io/acapi/edit", data={'status': 0 })
#ss = requests.get("http://f30f71f1.ngrok.io/acapi/currentstatus")
#print ss.content

IO.setmode(IO.BOARD)                    ## Use BOARD pin numbering.
IO.setup(22, IO.OUT)                    ## set output.
IO.setup(11,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(13,IO.OUT)
IO.setup(16,IO.OUT)

pwm=IO.PWM(22,100)
p = IO.PWM(11,40)
q = IO.PWM(12,40)
r = IO.PWM(13,40)

#ac = air.json()
#change = changer.json()
#lock = door.json()
#lamp = lamp.json()

#r = requests.post("http://f30f71f1.ngrok.io/changemeapi/currentbool", data={'status': 1 })
a = 0
b = 0
while 1:
	
	changer = requests.get("https://thawing-fortress-67733.herokuapp.com/changemeapi/changerequired")
	change = changer.json()
	chng = change['message']
	door = requests.get("https://thawing-fortress-67733.herokuapp.com/doorapi/currentstatus")
	lock = door.json()
	lck = lock['message']
	air = requests.get("https://thawing-fortress-67733.herokuapp.com/acapi/currentstatus")
	ac = air.json()
	cond = ac['message']
	print lck
	light = requests.get("https://thawing-fortress-67733.herokuapp.com/lightapi/status")
	ligh = light.json()
	status = ligh['status']
	red = ligh['red']
	green = ligh['green']
	blue = ligh['blue']
	if chng == True:
		print "Hi"
		if lck == True:
			pwm.start(5)
			angle1=0
			duty1= float(angle1)/10 + 2.5               ## Angle To Duty cycle  Conversion
			angle2=90
			duty2= float(angle2)/10 + 2.5
			a = 1

		elif lck == False:
			print "in false"
			pwm.start(5)
                	angle1=0
	                duty1= float(angle1)/10 + 2.5               ## Angle To Duty cycle  Conversion
        	        angle2=150
	                duty2= float(angle2)/10 + 2.5

	                pwm.ChangeDutyCycle(duty1)
#	                time.sleep(0.8)
	                pwm.ChangeDutyCycle(duty2)
#	                time.sleep(0.8)
			a = 0

		if cond == True:
			IO.output(16, IO.HIGH)
			b = 1
		elif cond == False:
			IO.output(16, IO.LOW)
			b = 0

		

		if status == True or a == 0:
		
			while status == True:
				p.start(20)                              #generate PWM signal with 20% duty cycle
				p.ChangeDutyCycle(red/3)               #change duty cycle for varying the brightness of LED.
				time.sleep(0.1)  
			
				q.start(20)
				q.ChangeDutyCycle(green/3)
				time.sleep(0.1)

				r.start(20)				
				r.ChangeDutyCycle(blue/3)
				time.sleep(0.1)
				r = 1
				light2 = requests.get("https://thawing-fortress-67733.herokuapp.com/lightapi/status")
				ligh1 = light2.json()
				status = ligh1['status']


  		ff =  requests.post("https://thawing-fortress-67733.herokuapp.com/changemeapi/currentbool", data={'status': 0 })




