from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)(my name is|I'm|I am) (.*)",
        ["Hello %3, IT chatbot here! How can I assist you?", "Hello IT, what is your emergency %3?",
         "Hi there %3, this is IT chatbot, what is on your mind?",
         "Hey, %3, IT chatbot here! What can't wait for a ticket?",
         "Hello %3, this is your IT chatbot, how may I be of service?",
         ]
    ],
    [
        r"(.*)(computer|browser|program|keyboard|mouse|laptop|monitor|printer|phone|tablet) "
        r"(.*) (not working|broken|stopped|crashed|down)(.*)",
        ["Did you try turning it off and on again?", "Did you change anything recently?",
         "Are there any flashing lights?", "Are you sure it's turned on?",
         "Did you try jiggling the cables! Did it work?",
         "Try turning it off and on again! Did it work?"]
    ],
    [
        r"(.*)(no|No|NO)(.*)",
        ["Try jiggling the cables! Did it work?", "Try clearing your browser cookies and history."
         "Try turning it off and on again! Did it work?", "Are you sure it's turned on?",
         "Put it back as it was! Is it working?", "Are there any flashing red lights?" ]
    ],
    [
        r"(.*)(yes|Yes|YES)(.*)",
        ["Did you try turning it off and on again?", "Put it back as it was! Is it working?",
         "Are there any flashing (green|yellow|orange) lights?", "Turn it on! Is it working?",
         "Reinstall the drivers. Is it working?",
         "Did you try jiggling the cables! Did it work?",
         "Try clearing your browser cookies and cache. Is it working?",
         "Try turning it off and on again! Did it work?"]
    ],
    [
        r"(.*)(works|working|ok|fine|OK|Ok|properly|)(.*)",
        ["I'm glad this is resolved, %3, please type 'quit' and leave us your feedback!",
         "Great to hear, %3! Have a swell day, mate! Please type 'quit' and leave us your feedback!",
         "You're welcome mate! Please type 'quit' and leave us your feedback!",
         "See how easy it was, %3, next time you can do it yourself!Please type 'quit' and leave us your feedback!"]
    ],
    [
        r"(.*) (question|query|ask|check|browse|) (.*)",
        ["I'm sorry, your %2 is out of the scope of IT chatbot, please forward your %2 to our customer support:\n "
         "email: support@itcrowd.co.uk"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)",
         "One is glad to be of service! Have a great day ahead :)",
         "It was nice chatting with you. May the odds be ever in your favour! :)",
         "I enjoyed our chat! May the force be with you Obi! :)"]
    ],
    [
        r"(.*)",
        ["I'm sorry, this is out of the scope of IT chatbot, please log a ticket with our customer support"
         " and type 'quit' to exit the chat or rephrase your question."]
    ],
]

# default message at the start of chat
print("\nWelcome to our new automated IT support powered by NLTK an open source Natural Language Processing toolkit. ",
      "\n\nPlease start by typing 'Hello, my name is...'\nType 'quit' to leave this chat.")

# Create Chat Bot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()
