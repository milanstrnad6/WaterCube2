#APNS

from pushjack import APNSClient

# client = APNSClient(certificate='<path/to/certificate.pem>',
#                     default_error_timeout=10,
#                     default_expiration_offset=2592000,
#                     default_batch_size=100,
#                     default_retries=5)

# token = '<device token>'
# alert = 'Hello world.'

# # Send to single device.
# # NOTE: Keyword arguments are optional.
# res = client.send(token,
#                   alert,
#                   badge='badge count',
#                   sound='sound to play',
#                   category='category',
#                   content_available=True,
#                   title='Title',
#                   title_loc_key='t_loc_key',
#                   title_loc_args='t_loc_args',
#                   action_loc_key='a_loc_key',
#                   loc_key='loc_key',
#                   launch_image='path/to/image.jpg',
#                   extra={'custom': 'data'})

# # Send to multiple devices by passing a list of tokens.
# client.send([token], alert, **options)