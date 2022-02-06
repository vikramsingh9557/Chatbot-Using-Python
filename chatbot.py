import random



hellow = ["hi","is anyone there?", "hello", "good day","hello there","hey"]
bye = ["bye bye", "see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
howare = ["how are you","whats up","how you doing"]
name = ["whats your name","what is your name","do you have any name","what should i call you","name"]
menu = ["i want to buy something", "what is on the menu", "what do you reccommend?", "could i get something to eat"]
hours = ["when are you guys open", "what are your hours", "hours of operation","time","work time","time period"]









print("*******************************************************\n")

while True:
	a = input('User said -')

	if a.lower() in hellow:
		botans = ["Hello !","hi","hi there","welcome","yes","hey",]
		print('Bot said - '+random.choice(botans)+'\n')

	elif a.lower() in bye:
		botans = ["sad to see you go","bye","okay bye","keep in touch","see you soon","nice to meet you"]
		print('Bot said - '+random.choice(botans)+'\n')

	elif a.lower() in howare:
		botans = ["I am fine ,thanks ","Happy","I am good","fine ","i am happy",]
		print('Bot said -'+ random.choice(botans)+'\n')

	elif a.lower() in name:
		botans = ["My name is bot","You can call me bot","TVC Bot in your service","My friends call me Bot"]
		print('Bot said -'+ random.choice(botans)+'\n')

	elif a.lower() in bye:
		botans = ["Sad to see you go :(", "Talk to you later", "Goodbye!","Have a nice Day"]
		print('Bot said - '+random.choice(botans)+'\n')

	elif a.lower() in menu:
		botans = ["We sell apples!", "Apples are on the menu!","Please take a look at Apples"]
		print('Bot said - '+random.choice(botans)+'\n')

	elif a.lower() in hours:
		botans = ["We are open 7am-4pm Monday-Friday!"]
		print('Bot said - '+random.choice(botans)+'\n')

	else:
		print('Bot said - Sorry, I did not get it''\n')