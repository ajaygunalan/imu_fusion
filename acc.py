# -------------------------------------------------------
import socket, traceback
import math

host = "10.156.248.168"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

while 1:
	try:
		message_str, address = s.recvfrom(8192)
		
		# Convert string into List of float and put them into a dictionary
		data_ls = message_str.split(",")
		data_ls = [float(i) for i in data_ls]
		# print data_ls
		var_ls = ['time_stamp','accl_id','accl_x','accl_y','accl_z', 'magn_id', 'magn_x', 'magn_y', 'magn_z', 'gyro_id', 'gyro_x', 'gryo_y', 'gyro_z']
		data = dict(zip(var_ls, data_ls))
        # acc = m/s^2;  gyro=rad/sec;  magno=microTelsa

		# Combine Accelerometer(m/s^2) to get angle values
		
		pitch_x_accel = 180 * math.atan2(data['accl_x'], math.sqrt((data['accl_y']*data['accl_y']) + (data['accl_z']*data['accl_z'])))/math.pi;
		roll_y_accel = 180 * math.atan2(data['accl_y'], math.sqrt((data['accl_x']*data['accl_x']) + (data['accl_z']*data['accl_z'])))/math.pi;
		print "pitch_x_accel :", pitch_x_accel, "roll_y_accel :", roll_y_accel
		

		# Calculate YAW from magnetometer formual taken from http://students.iitk.ac.in/roboclub/2017/12/21/Beginners-Guide-to-IMU.html

		mag_x_update = data['magn_x']*cos(pitch_x_accel) + data['magn_y']*sin(roll_y_accel)*sin(pitch_x_accel) + data['magn_z']*cos(roll_y_accel)*sin(pitch_x_accel)
		mag_y_update = data['magn_y']*cos(roll_y_accel) - data['magn_z']*sin(roll_y_accel)
		yaw_z_magn = 180 * atan2(-mag_y_update,mag_x_update)/M_PI;

		# Calculate the loop time from the timestamp


		# Calculate the angles from the gyro
		# gyroXangle+=rate_gyr_x*DT;
		# gyroYangle+=rate_gyr_y*DT;
		# gyroZangle+=rate_gyr_z*DT;

		# #Fusion to get Pitch 
		# CFangleX=AA*(CFangleX+rate_gyr_x*DT) +(1 - AA) * AccXangle;
		# CFangleY=AA*(CFangleY+rate_gyr_y*DT) +(1 - AA) * AccYangle;
		# CFangleY=AA*(CFangleY+rate_gyr_y*DT) +(1 - AA) * yaw;
      

	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
#-----------------------------------------------------------



# Combine Accelerometer(m/s^2) to get angle values
# pitch = 180 * atan2(accelX, sqrt(accelY*accelY + accelZ*accelZ))/PI;
# roll = 180 * atan2(accelY, sqrt(accelX*accelX + accelZ*accelZ))/PI;



# #Calculate YAW from magnetometer
# mag_x = magReadX*cos(pitch) + magReadY*sin(roll)*sin(pitch) + magReadZ*cos(roll)*sin(pitch)
# mag_y = magReadY * cos(roll) - magReadZ * sin(roll)
# yaw = 180 * atan2(-mag_y,mag_x)/M_PI;



# #Fusion to get Pitch 
# CFangleX=AA*(CFangleX+rate_gyr_x*DT) +(1 - AA) * AccXangle;
# CFangleY=AA*(CFangleY+rate_gyr_y*DT) +(1 - AA) * AccYangle;
# CFangleY=AA*(CFangleY+rate_gyr_y*DT) +(1 - AA) * yaw;


