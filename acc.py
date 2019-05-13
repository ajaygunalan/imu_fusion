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
		var_ls = ['time_stamp','accl_id','accl_x','accl_y','accl_z']
		data = dict(zip(var_ls, data_ls))

		# Combine Accelerometer(m/s^2) to get angle values
		
		pitch_x_accel = 180 * math.atan2(data['accl_x'], math.sqrt((data['accl_y']*data['accl_y']) + (data['accl_z']*data['accl_z'])))/math.pi;
		roll_y_accel = 180 * math.atan2(data['accl_y'], math.sqrt((data['accl_x']*data['accl_x']) + (data['accl_z']*data['accl_z'])))/math.pi;
		print "pitch_x_accel : ", pitch_x_accel, "roll_y_accel : ", roll_y_accel
		


         
        # print data_ls[2]
        # , accl_z, accl_z
        # print (data_ls[2])
        # , type(accl_z), type(accl_z))



		#data_ls[5]
		# gryo_x = data_ls[6] #in rad/sec 
		# gryo_y = data_ls[7] #in rad/sec
		# gyro_z = data_ls[8] #in rad/sec

		# #data_ls[9]
		# magn_x = data_ls[10] #in micro-Telsa
		# magn_y = data_ls[11] #in micro-Telsa
		# magn_z = data_ls[12] #in micro-Telsa

	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
#-----------------------------------------------------------



# Combine Accelerometer(m/s^2) to get angle values
# pitch = 180 * atan2(accelX, sqrt(accelY*accelY + accelZ*accelZ))/PI;
# roll = 180 * atan2(accelY, sqrt(accelX*accelX + accelZ*accelZ))/PI;

# # Calculate the angles from the gyro
# gyroXangle+=rate_gyr_x*DT;
# gyroYangle+=rate_gyr_y*DT;
# gyroZangle+=rate_gyr_z*DT;


# #Calculate YAW from magnetometer
# mag_x = magReadX*cos(pitch) + magReadY*sin(roll)*sin(pitch) + magReadZ*cos(roll)*sin(pitch)
# mag_y = magReadY * cos(roll) - magReadZ * sin(roll)
# yaw = 180 * atan2(-mag_y,mag_x)/M_PI;



# #Fusion to get Pitch 
# CFangleX=AA*(CFangleX+rate_gyr_x*DT) +(1 - AA) * AccXangle;
# CFangleY=AA*(CFangleY+rate_gyr_y*DT) +(1 - AA) * AccYangle;
# CFangleY=AA*(CFangleY+rate_gyr_y*DT) +(1 - AA) * yaw;


