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
        self.connections.append()

class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.users = []

    def addUser(self, new_user):
        self.users.append(new_user)
        for user in self.users:
            if user.getUsername() == new_user:
                print ("there can't be multiple users with the same username.")
                return

    def getUserID(self, username):
        return self.username
        return self.username2

    def numUser(self):
        return len(self.users)

    def printUsers(self):
        for users in self.users:
            print (users.getUsername()) #print("network users:")
            print (users.getUsername()) #for user in self.users

    def addConnection(self, user2, user3):
        self.users.append()

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
  my_network = Network()
  my_network.addUser(user1)
  user2 = User(username, name, birthday, age, aboutMe)
  my_network.printUsers()


# Runs your program.
if __name__ == '__main__':
    main()
