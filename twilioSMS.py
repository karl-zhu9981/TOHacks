from twilio.rest import Client 
 
account_sid = 'ACff9600ba55bb111039e8bda624c9893e' 
auth_token = 'd36e38aa07652dcf5582915250bc4eac'
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGfbb43ebb86df86cd68ed514e6f80eea4', 
                              body='Welcome to reciPings!',      
                              to='[phone number]' 
                          ) 
 
print(message.sid)