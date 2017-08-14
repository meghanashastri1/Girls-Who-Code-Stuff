class User:
    # Define the fields and methods for your object here.
    def __init__(self, username, name, birthday, age, aboutMe):
        self.username = username
        self.name = name
        self.birthday = birthday
        self.age = age
        self.connections = []

    def getUsername(self):
        return self.username

    def getName(self):
        return self.name

    def getBirthday(self):
        return self.birthday

    def getAge(self):
        return self.age

    def getAboutMe(self):
        return self.aboutMe

    def addConnections(self, user2):
        self.connections.append(user2)

class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.users = []

    def numUser(self):
        return len(self.users)

    def addUser(self, username):
        #self.users.append(new_user)
        for user in self.users:
            if username == user.getUsername():
                print ("Sorry, that name is taken.")
                return
            else self.users.append(username)

    def getUserID(self, username):
        user_id = -1
        for user in self.users:
            if username == user.getUsername():
                user_id = user.getUserID
        return user_id

    def printUsers(self):
        print(self.users)
        for users in self.users:

            print (users.getUsername()) #print("network users:")

    def addConnection(self, user1_id, user2_id):

        self.users[user1_id].addConnection()
        self.users[user2_id].addConnection()

    def printConnections(self):
        for users in self.users:
            print (self.users)

    def printUserProfile(self, user):
        return self.user

def main():
    # Define the program flow for your user interface here.
  username = input("Enter your username   ")
  name = input("Enter your profile name   ")
  birthday = input("Enter your birthday   ")
  age = input("Enter your age   ")
  aboutMe = input("Enter about me   ")

  username2 = input("Enter your username   ")
  name2 = input("Enter your profile name   ")
  birthday2 = input("Enter your birthday   ")
  age2 = input("Enter your age   ")
  aboutMe2 = input("Enter about me   ")

  user1 = User(username, name, birthday, age, aboutMe)
  user2 = User(username, name, birthday, age, aboutMe)
  my_network = Network()
  my_network.addUser(user1)
  my_network.addUser(user2)
  my_network.printUsers()
  my_network.addConnection(username,username2)

# Runs your program.
if __name__ == '__main__':
    main()
