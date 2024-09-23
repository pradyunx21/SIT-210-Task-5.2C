import RPi.GPIO as GPIO
from guizero import App, Slider

# Set up GPIO
GPIO.setmode(GPIO.BCM)

# GPIO pins for the LEDs
LED_PINS = [18, 23, 24]

# Set up the GPIO pins as output and PWM
pwm = []
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    pwm.append(GPIO.PWM(pin, 100))  # 100Hz frequency for PWM
    pwm[-1].start(0)  # Start with 0 duty cycle (LED off)

# Function to change LED brightness based on slider value
def change_brightness(value, index):
    pwm[index].ChangeDutyCycle(int(value))

# Create the GUI app
app = App("LED Brightness Control")

# Create sliders for each LED
slider1 = Slider(app, start=0, end=100, command=lambda value: change_brightness(value, 0))
slider1.text = "LED 1 Brightness"
slider2 = Slider(app, start=0, end=100, command=lambda value: change_brightness(value, 1))
slider2.text = "LED 2 Brightness"
slider3 = Slider(app, start=0, end=100, command=lambda value: change_brightness(value, 2))
slider3.text = "LED 3 Brightness"

# Start the GUI
app.display()

# Cleanup GPIO after closing the GUI
for p in pwm:
    p.stop()
GPIO.cleanup()
