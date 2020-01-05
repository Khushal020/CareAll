import math

class Young:
    count = 0
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__number_of_olders_cared_by = 0
        Young.count += 1
        self.__id = Young.count
        self.__rating = None
        self.__reviews = []
        self.__olders_cared_by = []
        
    def show_olders_cared_by(self):
        print("*---------------*--------------*")
        print("Id of olders that are taking care by this young man")
        print(self.__older_cared_by)
        
    def show_detail_of_young(self):
        print("Name: {0}, Age: {1}, address: {2}, Rating: {3}, number of olders cared by: {4}".format(self.__name, self.__age, self.__address, self.__rating, self.__number_of_olders_cared_by))
        
    def get_old_for_care(self, id):
        if self.__number_of_older_cared_by > 4:
            print("you have exceed your limit of 4 old")
        else:
            print("old man with id {0} is allocated to you")
            self.__olders_cared_by.append(id)
            self.__number_of_olders_cared_by = len(self.__olders_cared_by)
            
    def get_review(self, id, review, rating):
        self.__review.append([id, rating, review])
        self.rating = math.avg(self.__review[:,1])
        
class Old:
    count = 0
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__is_cared_by = False
        self.__cared_by = None
        Old.count += 1
        self.__id = Old.count
        self.__rating = None
        self.__reviews = []
        
    def older_cared_by(self):
        if self.__is_cared_by == False:
            print("Currently, this old man is not taking care by any young man")
        else:
            print("*---------------*--------------*")
            print("Id of young man who is taking care of this old man")
            print(self.__cared_by)
            
    def show_detail_of_old(self):
        print("Name: {0}, Age: {1}, address: {2}, Rating: {3}, is cared by: {4}".format(self.__name, self.__age, self.__address, self.__rating, self.__cared_by))
        
    
    def allocate_to_young(self, id):
        self.__is_cared_by = True
        self.__cared_by = id
            
    def get_review(self, id, review, rating):
        self.__reviews.append([id, rating, review])
        self.rating = math.avg(self.__review[:,1])
    
    
    
    
    
    
if __name__ == "__main__":
    
    youngs = []
    olds = []
    
    
    
    print("*-------------------MENU--------------------*")
    print("1.create new young object")
    print("2.create new old object")
    print("3.show list of old couples that are taking care")
    print("4.show list of young chap who is taking care")
    print("5.show list of all young chap")
    print("6.show list of all old couples")
    
    while(True):
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            address = input("Enter your address: ")
            y = Young(name, age, address)
            youngs.append(y)
            
        elif choice == 2:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            address = input("Enter your address: ")
            o = Old(name, age, address)
            olds.append(o)
        
        elif choice == 3:
            print("*--------------------------------*")
            print("Id of old couples that are taking care")
            for old in olds:
                if old.__is_cared_by == True:
                    print(olds.__id)
        
        elif choice == 4:
            print("*--------------------------------*")
            print("Id of young chap that are taking care")
            for young in youngs:
                if young.__number_of_older_cared_by > 0:
                    print(young.__id)
                    
        elif choice == 5:
            print("*--------------------------------*")
            print("List of all young chap")
            for young in youngs:
                young.show_detail_of_young()
                
        elif choice == 6:
            print("*--------------------------------*")
            print("List of all old couplt")
            for old in olds:
                old.show_detail_of_old()
    
    
        if(choice > 6 or choice < 1):
            break
    
