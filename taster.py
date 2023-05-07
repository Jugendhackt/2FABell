import time
import RPi.GPIO as GPIO

# SET GPIO Button-Pin
gpio = 5

# Main Function
def main():
  value = 0

  while True:

    if not GPIO.input(gpio):
      value += 0.01

    if value > 0:

      if GPIO.input(gpio):
        print "gedrueckt"
        main()

    time.sleep(0.03)

  return 0

if __name__ == '__main__':
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(gpio, GPIO.IN)
  main()
