#APNS

from pushjack import APNSClient

import DATA

#PROPERTIES

CERTIFICATE = '</home/pi/CUBE/DATA/pushcert.pem>'

#MAIN

def sendNotification():
	client = APNSClient(certificate=CERTIFICATE,default_error_timeout=10,default_expiration_offset=2592000,default_batch_size=100,default_retries=5)

	token = DATA.load_token()
	print("TOKEN --> ")
	print(token)
	alert = 'Water level below 20%, please refill.'

	tokenOK = '<' + token '>'

	# Send to single device.
	# NOTE: Keyword arguments are optional.
	res = client.send(
		tokenOK,
		alert,
		badge='badge count',
		sound='sound to play',
		category='category',
		content_available=True,
		title='WARNING',
		title_loc_key='t_loc_key',
		title_loc_args='t_loc_args',
		action_loc_key='a_loc_key',
		loc_key='loc_key',
		launch_image='path/to/image.jpg',
		extra={'custom': 'data'}
	)

	# Send to multiple devices by passing a list of tokens.
	#client.send([token], alert, **options)

sendNotification()