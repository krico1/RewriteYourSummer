from pyrebase import pyrebase

config = {  
"apiKey": "AIzaSyCu1Bj2CHI6h1ViakdFp5oWuskiYMa3M2M",  
"authDomain": "chat-bo-c5be1.firebaseapp.com",  
"databaseURL": "https://chat-bo-c5be1.firebaseio.com",  
"storageBucket": "chat-bo-c5be1.appspot.com",  
}

firebase = pyrebase.initialize_app(config)

# ref = db.reference('dinosaurs')
# snapshot = ref.order_by_child('height').get()
# for key, val in snapshot.items():
#     print('{0} was {1} meters tall'.format(key, val))

# print(ref.get())
db = firebase.database()

# responses = {}
# for i in range(1):
#     Sheet1 = db.child("Sheet1").child(i).get()
#     print(Sheet1.key())
#     # dict = (Sheet1.val())
#     # print(dict['name'])

ChatBot = db.child("1ttg3LdOg7Vcq2ttzoiih7Ze4LIMKKZVrIkx_xkLFAM4").get()
ChatBotVal = ChatBot.val()
#print(ChatBotval)
# print(ChatBotval['Keys'])
chatbot_items = ChatBotVal['ChatBot']
chatbot_words = ChatBotVal['Words']
chatbot_keys = ChatBotVal['Keys']
# print(chatbot_items[1]) # gets first item under chatbot
# print(chatbot_items[1]['id']) # gets id of first item
# print(chatbot_items[1]['key']) # gets key

responsesDict = {}
# print(chatbot_items)
for i in range(1, len(chatbot_items)):
    curr_item = chatbot_items[i]
    responsesDict[curr_item['key']] = curr_item['response']

# print(responsesDict)

wordArr = []
for i in range(len(chatbot_words)):
    wordArr.append(chatbot_words[i]['word'])

# print(wordArr)

keyArr = []
for i in range(len(chatbot_keys)):
    keyArr.append(chatbot_keys[i]['key'])

# print(keyArr)

