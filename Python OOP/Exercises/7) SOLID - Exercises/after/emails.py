from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyMl(IContent):

    def format(self):
        return ''.join(['<myML>', self.text, '</myML>'])


class IProtocol(ABC):

    def __init__(self, protocol):
        self.protocol = protocol

    @abstractmethod
    def format(self):
        pass


class ImProtocol(IProtocol):

    def format(self):
        return ''.join(["I'm ", self.protocol])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: IProtocol):
        self.__sender = sender.format()

    def set_receiver(self, receiver: IProtocol):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')

sender = ImProtocol('gmal')
email.set_sender(sender)

receiver = ImProtocol('james')
email.set_receiver(receiver)

content = MyMl('Hello, there!')
email.set_content(content)

print(email)