class User:
    def __init__(self, first_name, last_name, like_count, friends_name):
        self.first_name = first_name
        self.last_name = last_name
        self.like_count = like_count
        self.friends_name =friends_name  
    def introduce(self):
        print("Hi i'm " + self.first_name + " " + self.last_name) 
        
    def fullprofile(self):
        print("Full Name: " + self.first_name + " " + self.last_name)
        print("Like: " + str(self.like_count))
        print("Friend")
        for friends in self.friends_name:
            print(" - " + friends)    
                              
user1 = User("gwen", "nuqui", 100, ["cpp", "java"])
user1.introduce()
user1.fullprofile()
