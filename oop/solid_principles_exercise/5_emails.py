########################################################################################################################
#                                ____  _             _                                                                 #
#                               / ___|(_)_ __   __ _| | ___                                                            #
#                               \___ \| | '_ \ / _` | |/ _ \                                                           #
#                                ___) | | | | | (_| | |  __/                                                           #
#                               |____/|_|_| |_|\__, |_|\___|                                                           #
#                                              |___/                                                                   #
#                                                                    _ _     _ _ _ _                                   #
#                                _ __ ___  ___ _ __   ___  _ __  ___(_) |__ (_) (_) |_ _   _                           #
#                               | '__/ _ \/ __| '_ \ / _ \| '_ \/ __| | '_ \| | | | __| | | |                          #
#                               | | |  __/\__ \ |_) | (_) | | | \__ \ | |_) | | | | |_| |_| |                          #
#                               |_|  \___||___/ .__/ \___/|_| |_|___/_|_.__/|_|_|_|\__|\__, |                          #
#                                             |_|                                      |___/                           #
#                                                                                                                      #
# The old code violated the Single Responsibility Principle because apart from handling sender and receiver the        #
# Email class was also handling the content formatting. This was fixed by creating an Abstract class IContent and      #
# subclass MyContent that is handling the formatting. Additionally, the code was violating the Open / Close Principle  #
# because if we introduce additional protocols or content types the Email class had to be changed.                     #
#                                                                                                                      #
########################################################################################################################

from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        ...

    @abstractmethod
    def set_receiver(self, receiver):
        ...

    @abstractmethod
    def set_content(self, content):
        ...


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyContent(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class IProtocol(ABC):

    @staticmethod
    @abstractmethod
    def protocol(self):
        ...


class MyProtocol(IProtocol):

    @staticmethod
    def protocol(person):
        return ''.join(["I'm ", person])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = self.protocol.protocol(sender)

    def set_receiver(self, receiver):
        self.__receiver = self.protocol.protocol(receiver)

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


protocol = MyProtocol()
email = Email(protocol)
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)


