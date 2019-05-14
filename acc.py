# -------------------------------------------------------
import socket, traceback
import math

host = "10.156.248.168"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

prev_time_stamp = 0
prev_magno_ls =  []
prev_gyro_ls  = []

AA = 0.9

gyroXangle = 0
gyroYangle = 0 
gyroZangle = 0

CFangleX = 0
CFangleY = 0
CFangleZ = 0


while 1:
	try:

		# accl, gryo, magno
		# acc = m/s^2;  gyro=rad/sec;  magno=microTelsa

		# read from socket
		message_str, address = s.recvfrom(8192)
		print message_str

		
		# Convert string into list of float 
		# data_ls = message_str.split(",")
		# data_ls = [float(i) for i in data_ls]
		# # print len(data_ls)
		# print data_ls


		# #append previous values if len is not 13
		# if len(data_ls) == 9:
		# 	data_ls.append(prev_magno_ls)

		# elif len(data_ls) == 5:
		# 	data_ls.append(prev_gyro_ls)
		# 	data_ls.append(prev_magno_ls)

		# #convert into a dictionary
		# var_ls = ['time_stamp','accl_id','accl_x','accl_y','accl_z', 'gyro_id', 'gyro_x', 'gyro_y', 'gyro_z', 'magn_id', 'magn_x', 'magn_y', 'magn_z']
		# data = dict(zip(var_ls, data_ls))
		# print data

		# # Combine Accelerometer(m/s^2) to get angle values
		
		# pitch_x_accel = 180 * math.atan2(data['accl_x'], math.sqrt((data['accl_y']*data['accl_y']) + (data['accl_z']*data['accl_z'])))/math.pi;
		# roll_y_accel = 180 * math.atan2(data['accl_y'], math.sqrt((data['accl_x']*data['accl_x']) + (data['accl_z']*data['accl_z'])))/math.pi;
		# # print "pitch_x_accel :", pitch_x_accel, "roll_y_accel :", roll_y_accel
		

		# # Calculate YAW from magnetometer formual taken from http://students.iitk.ac.in/roboclub/2017/12/21/Beginners-Guide-to-IMU.html

		# mag_x_update = data['magn_x']*math.cos(pitch_x_accel) + data['magn_y']*math.sin(roll_y_accel)*math.sin(pitch_x_accel) + data['magn_z']*math.cos(roll_y_accel)*math.sin(pitch_x_accel)
		# mag_y_update = data['magn_y']*math.cos(roll_y_accel) - data['magn_z']*math.sin(roll_y_accel)
		# yaw_z_magn = 180 * math.atan2(-mag_y_update, mag_x_update)/math.pi;
		# # print "yaw_z_magn :", yaw_z_magn
		
		# # Calculate the loop time from the timestamp
		# dt = data_ls[0] - prev_time_stamp
		# # print "sensor dt from timestamp :", dt


		# # Calculate the angles from the gyro
		# gyroXangle+= data['gyro_x']*dt;
		# gyroYangle+= data['gyro_y']*dt;
		# gyroZangle+= data['gyro_z']*dt;

		# #Fusion to get Pitch 
		# CFangleX = AA*(gyroXangle) +(1 - AA) * pitch_x_accel;
		# CFangleY = AA*(gyroYangle) +(1 - AA) * roll_y_accel;
		# CFangleY = AA*(gyroZangle) +(1 - AA) * yaw_z_magn;
 

		# print "Final Pitch(X) :", CFangleX , "Final Roll(Y) :", CFangleY, "Final Pitch(Z) :", CFangleZ


		# # Update previous value
		# prev_magno_ls = data_ls[-4:]
		# prev_gyro_ls  = data_ls[5:8]
		# prev_time_stamp = data_ls[0]

		# print prev_gyro_ls
		# print prev_magno_ls

	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()
#-----------------------------------------------------------



