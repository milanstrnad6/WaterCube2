#APNS

from pushjack import APNSClient
from pushjack import APNSSandboxClient

import time
import DATA

#PROPERTIES

#CERTIFICATE = '/home/pi/CUBE/DATA/pushcertdev.pem'
CERTIFICATE = '/home/pi/CUBE3/WaterCube2/DATA/ccc.pem'

#MAIN

def sendNotification():
	print("SEND NOTIFICATION...............................................")
	token = DATA.load_token()
	time.sleep(5)
	print("SEND NOTIFICATION...............................................REALLY NOW")

	alert = 'Bonsai: Water level below 20%, please refill.'

	client = APNSSandboxClient(certificate=CERTIFICATE,default_error_timeout=10,default_expiration_offset=2592000,default_batch_size=100,default_retries=10)

	# Send to single device.
	# NOTE: Keyword arguments are optional.
	res = client.send(
		token,
		alert,
		badge='1',
		sound='sound to play',
		# category='category',
		# content_available=True,
		title='WARNING'
		# title_loc_key='t_loc_key',
		# title_loc_args='t_loc_args',
		# action_loc_key='a_loc_key',
		# loc_key='loc_key',
		# launch_image='path/to/image.jpg',
		# extra={'custom': 'data'}
	)

	print(res.tokens)
	print(res.errors)
	print(res.token_errors)

	DATA.save_shouldSend(0)

	# print("SENDING FINISHEEEEEED")
	# DATA.save_sending(0)
