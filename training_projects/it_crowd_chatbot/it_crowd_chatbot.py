from nltk.chat.util import Chat, reflections
from termcolor import colored

pairs = [
    [
        r"(.*)(my name is|I'm|I am|this is|im'|i'm) (.*)",
        [colored("Hello %3, IT chatbot here! How can I assist you?", "blue"),
         colored("Hello IT, what is your emergency, %3?", "blue"),
         colored("Hi there %3, this is IT chatbot, what is on your mind?", "blue"),
         colored("Hey, %3, IT chatbot here! What can't wait for a ticket?", "blue"),
         colored("Hello %3, this is your IT chatbot, how may I be of service?", "blue"),
         ]
    ],
    [
        r"(.*)(computer|browser|program|keyboard|mouse|laptop|monitor|printer|phone|tablet)"
        r"(.*)(not working|broke|broken|stopped|crashed|down)(.*)",
        [colored("Did you try turning it off and on again?", "blue"),
         colored("Did you change anything recently?", "blue"),
         colored("Are there any flashing lights?", "blue"),
         colored("Are you sure it's turned on?", "blue"),
         colored("Did you try jiggling the cables! Did it work?", "blue"),
         colored("Try turning it off and on again! Did it work?", "blue")]
    ],
    [
        r"(.*)(no|No|NO)(.*)",
        [colored("Try jiggling the cables! Did it work?", "blue"),
         colored("Try clearing your browser cookies and history.", "blue"),
         colored("Try turning it off and on again! Did it work?", "blue"),
         colored("Are you sure it's turned on?", "blue"),
         colored("Put it back as it was! Is it working?", "blue"),
         colored("Are there any flashing red lights?", "blue")]
    ],
    [
        r"(.*)(yes|Yes|YES)(.*)",
        [colored("Did you try turning it off and on again?", "blue"),
         colored("Put it back as it was! Is it working?", "blue"),
         colored("Are there any flashing green lights?", "blue"),
         colored("Turn it on! Is it working?", "blue"),
         colored("Reinstall the drivers. Is it working?", "blue"),
         colored("Did you try jiggling the cables! Did it work?", "blue"),
         colored("Try clearing your browser cookies and cache. Is it working?", "blue"),
         colored("Try turning it off and on again! Did it work?", "blue")]
    ],
    [
        r"(.*)(works|worked|working|ok|fine|OK|Ok|properly|all good)(.*)",
        [colored("I'm glad this is resolved, please type 'quit' and leave us your feedback!", "blue"),
         colored("Great to hear! Have a swell day, mate! Please type 'quit' and leave us your feedback!", "blue"),
         colored("You're welcome mate! Please type 'quit' and leave us your feedback!", "blue"),
         colored(
             "See how easy it was, next time you can do it yourself! Please type 'quit' and leave us your feedback!",
             "blue")]
    ],
    [
        r"(.*) (question|query|ask|check|browse)(.*)",
        [colored(
            "I'm sorry, your %2 is out of the scope of IT chatbot, please forward your %2 to our customer support:\n "
            "email: support@itcrowd.co.uk", "blue")]
    ],
    [
        r"quit",
        [colored("Bye for now. See you soon :)", "blue"),
         colored("It was nice talking to you. See you soon :)", "blue"),
         colored("One is glad to be of service! Have a great day ahead :)", "blue"),
         colored("It was nice chatting with you. May the odds be ever in your favour! :)", "blue"),
         colored("I enjoyed our chat! May the force be with you Obi-Wan Kenobi! :)", "blue")]
    ],
    [
        r"(.*)",
        [colored("I'm sorry, this is out of the scope of IT chatbot, please log a ticket with our customer support"
         " and type 'quit' to exit the chat or rephrase your question.", "blue")]
    ],
]

# default message at the start of chat
print(colored("\nWelcome to our new automated IT support powered by NLTK an open source Natural Language Processing toolkit. "
      "\n\nPlease use lower case and start by typing 'Hello, my name is...'\n\nType 'quit' to leave this chat.\n", "blue"))

# Create Chat Bot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()
