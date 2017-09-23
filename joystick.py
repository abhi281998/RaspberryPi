import Rpi.GPIO as GPIO
import time

left = 19
right = 20
up = 21
down = 16
center = 26

count = 0
lat_a =0
lat_b =0
lat_c =0
lon_a =0
lon_b =0
lon_c =0

def display()
	print "\n\n\n\n\nLattitude :", lat_a, ".", lat_b, lat_c
	print "\n\nLongitude :", lon_a, ".", lon_b, lon_c


GPIO.setmode(GPIO.BCM)
GPIO.setup(left,GPIO.IN)
GPIO.setup(right,GPIO.IN)
GPIO.setup(up,GPIO.IN)
GPIO.setup(down,GPIO.IN)
GPIO.setup(center,GPIO.IN)

def pluslat_a()	
	lat_a += 1
	display()

def pluslat_b()
	if(lat_b < 9):
		lat_b += 1
		display()
	else:
		lat_b = 0
		pluslat_a()

def pluslat_c()
	if(lat_c < 9):
		lat_c += 1
		display()
	else:
		lat_c = 0
		pluslat_b()

def pluslon_a()	
	lon_a += 1
	display()

def pluslon_b()
	if(lon_b < 9):
		lon_b += 1
		display()
	else:
		lon_b = 0
		pluslon_a()

def pluslon_c()
	if(lon_c < 9):
		lon_c += 1
		display()
	else:
		lon_c = 0
		pluslon_b()

def declat_a()
	if(lat_a > 0):
		lat_a -= 1
		display()

def declat_b()
	if(lat_b > 0):
		lat_b -= 1
	else:
		lat_b = 9
		declat_a()

def declat_c()
	if(lat_c > 0):
		lat_c -= 1
	else:
		lat_c = 9
		declat_b()

def declon_a()
	if(lon_a > 0):
		lon_a -= 1
		display()

def declon_b()
	if(lon_b > 0):
		lon_b -= 1
	else:
		lon_b = 9
		declon_a()

def declon_c()
	if(lon_c > 0):
		lon_c -= 1
	else:
		lon_c = 9
		declon_b()


while True:
	if(GPIO.input(left) == 0):
		#print "left pressed"
		if(count > 0):
			count = count - 1

	if(GPIO.input(right) == 0):
		#print "right pressed"
		if(count < 5):
			count = count + 1

	if(GPIO.input(up) == 0):
		#print " up pressed"
		if(count == 0):
			pluslat_a()
		if(count == 1):
			pluslat_b()
		if(count == 2):
			pluslat_c()
		if(count == 3):
			pluslon_a()
		if(count == 4):
			pluslon_b()
		if(count == 5):
			pluslon_c()
	if(GPIO.input(down) == 0):
		#print " down pressed"
		if(count == 0):
			declat_a()
		if(count == 1):
			declat_b()
		if(count == 2):
			declat_c()
		if(count == 3):
			declon_a()
		if(count == 4):
			declon_b()
		if(count == 5):
			declon_c()
	if(GPIO.input(center) == 0):
		#print "center pressed"
		break


lattitude = lat_a + lat_b/10.0 + lat_c/100.0
longitude = lon_a + lon_b/10.0 + lon_c/100.0

print "LATTITUDE :", lattitude
print "LONGITUDE :", longitude