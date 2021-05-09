import json
import os
#from twilio.rest import Client
import requests
from trycourier import Courier
from serpapi import GoogleSearch

account_sid = 'ACff9600ba55bb111039e8bda624c9893e' 
auth_token = 'd36e38aa07652dcf5582915250bc4eac'
#client = Client(account_sid, auth_token) 

client = Courier(auth_token="dk_prod_7MTXC74P0D4ZWZG94SD0HJ507FWF")

params = {
  "api_key": "e61e09984c68bf6aa40bb477fb5bf5ebb5802ac55f9ce17ac7325575e7765257",
  "engine": "google",
  "q": "onion, carrot, tomato, garlic, pepper" + "recipes",
  "location": "Austin, Texas, United States",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en"
}

final_result = ['']
def goSearch(parameters, ):
	search = GoogleSearch(params)
	results = search.get_dict()

	for key,value in results.items():
		out1 = results.get('recipes_results')
		
	for i in range(len(out1)):
		for key1, value1 in out1[i].items():
			#out2 = ['']
			#out3 = ['']
			outDes = out1[0].get('title')
			#outTitle2 = out1[1].get('title')
			#outTitle3 = out1[2].get('title')
			outIng = out1[0].get('ingredients')
			#outIngredients2 = out1[1].get('ingredients')
			#outIngredients3 = out1[2].get('ingredients')
			outWeb = out1[0].get('link')
			#outLink2 = out1[1].get('link')
			#outLink3 = out1[2].get('link')
			#outF1 = [outTitle1, outIngredients1, outLink1]
			#outF2 = [outTitle2, outIngredients2, outLink2]
			#outF3 = [outTitle3, outIngredients3, outLink3]

		#print(outF1, outF2)
		#return(outF1, outF2, outF3)
		return(outDes, outWeb, outIng)
		#return out1
			
	


def POSTmessage(cl, res):
	message = client.messages.create(
	                              body=res,
	                              from_='+16092514685',
	                              to='+18087241921'
	                          )
	print(message.sid)
	return message.sid


def POSTCourier(cl, des, web, ing):

	resp = client.send(
	  event="ND2CQ0TZ0G4C61MB4N2QCT1R0QKT",
	  recipient="201b636a-9ab2-4568-be9b-964e3bec289f",
	  profile={
	    #'phone_number': "+16475056177",
	    #'email' : 
	    'phone_number' : '+18087241921'
	  },
	  data={
	    'website': web,
	    'description' : des,
	    'ingredients' : ing,
	  },
	)

	print(resp['messageId'])
	#return resp(['messageId'])



#print(resp['messageId'])

def Getmessage():
	
	url = "https://api.courier.com/messages"

	headers = {
	    "Accept": "application/json",
	    "Authorization": "Bearer dk_prod_7MTXC74P0D4ZWZG94SD0HJ507FWF"
	}

	response = requests.request("GET", url, headers=headers)

	print(response.text)




###RESULTS###

#print (json.dumps(final, indent=1))
#print (json.dumps(out1, indent=1))
googleOut = goSearch(params)
#print(googleOut)
print('************ NEXT FUNCTION ************\n')

POSTCourier(client, googleOut[0], googleOut[1], googleOut[2])

print('************ NEXT FUNCTION ************\n')
#doesn't work yet
Getmessage()