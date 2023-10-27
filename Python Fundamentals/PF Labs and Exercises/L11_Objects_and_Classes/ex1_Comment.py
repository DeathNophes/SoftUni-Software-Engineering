class Comment:
    def __init__(self, username, content, likes=0):     # Optional argument is always on the end!
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
