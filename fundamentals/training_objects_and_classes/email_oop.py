class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        sender = self.sender
        receiver = self.receiver
        content = self.content
        is_sent = self.is_sent
        return f"{sender} says to {receiver}: {content}. Sent: {is_sent}"


email_list = []

command_line = input()
while command_line != 'Stop':
    sender_name, receiver_name, content_text = command_line.split()
    email = Email(sender_name, receiver_name, content_text)
    email_list.append(email)
    command_line = input()

send_emails_indices = list(map(int, (input().split(', '))))

for index, current_email in enumerate(email_list):
    if index in send_emails_indices:
        current_email.send()
    print(current_email.get_info())
