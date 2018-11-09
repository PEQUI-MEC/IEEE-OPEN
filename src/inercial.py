import logging
import sys
import time
import math
import rospy
from std_msgs.msg import Float32MultiArray

from Adafruit_BNO055 import BNO055

bno = BNO055.BNO055(rst=18, address=BNO055.BNO055_ADDRESS_B)

# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin(BNO055.OPERATION_MODE_NDOF):
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))


print("Inicializando ros node..")
pub = rospy.Publisher("Mirela/imu", Float32MultiArray, queue_size=1)
rospy.init_node("Publisher", anonymous=True)
mat = Float32MultiArray()

print('Reading BNO055 data, press Ctrl-C to quit...')
while not rospy.is_shutdown():    
    # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
    sys, gyro, accel, mag = bno.get_calibration_status()

    # Read the Euler angles
    if sys == 3:
        z, y, x = bno.read_euler()
        mat.data = [x,y,z]
        pub.publish(mat)

    #print('x={0:0.2F} y={1:0.2F} z={2:0.2F}'.format(x, y, z))
    #print('giro na normal do sensor = theta ={0}'.format(z))
    
    # Sensor temperature in degrees Celsius:
    #temp_c = bno.read_temp()
    # Magnetometer data (in micro-Teslas):
    #x,y,z = bno.read_magnetometer()
    # Gyroscope data (in degrees per second):
    #x,y,z = bno.read_gyroscope()
    # Accelerometer data (in meters per second squared):
    #x,y,z = bno.read_accelerometer()
    # Linear acceleration data (i.e. acceleration from movement, not gravity--
    # returned in meters per second squared):
    #x,y,z = bno.read_linear_acceleration()
    # Gravity acceleration data (i.e. acceleration just from gravity--returned
    # in meters per second squared):
    #x,y,z = bno.read_gravity()
    # Sleep for a second until the next reading.
    #time.sleep(1)
