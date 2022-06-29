class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

    def comment_info(self):
        return f'user: {self.username}\ncontent: {self.content}\nlikes: {self.likes}'


comment = Comment("user1", "I like this book")

print(comment.comment_info())
