
def createJSON(json3,json4):
	for k,v in json3.items():
		if isinstance(v,dict):
			try:
				createJSON(v,json4[str(k)])
			##no such key in json4/key is [],int,str-->just instant replace
			except:
				json4[str(k)]=v
		elif isinstance(v,list):
			json4[str(k)]=v
		elif isinstance(v,bool):
			json4[str(k)]=v
		else:
			for key,value in json4.items():
				if k==key:
					json4[str(k)]=v
createJSON(json3,json4)
print('json4=',json4)	
