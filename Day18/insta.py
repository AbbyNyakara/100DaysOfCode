class User:
    # The init function gets called every time a new onject is being created

    # You can also create an attribute in the init functin, with a default value. 
    def __init__(self, user_id, username):
        self.id = user_id
        self.user_name = username 
        self.followers = 0 
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# When you create a User object, you will be required to pass in 2 positional argumnts
user1 = User("001", "Abby")
user2 = User("002", "Moh")


user1.follow(user2)

print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)
