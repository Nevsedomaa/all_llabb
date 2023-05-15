class Restaurant:
    def __init__(self, Name, Type, rating):
        self.Name = Name
        self.Type = Type
        self.rating = rating

    def Describe(self):

        print("Название ресторана", self.Name)
        print("Тип ресторанаf", self.Type)
        print("Рейтинг- ", self.rating)

    def Open(self):
        print("Ресторан", self.Name, "Открыт")

    def update_rating(self, new_rating):
        self.rating = new_rating

newRestaurant  =   Restaurant(input("Введите начвание ресторана - "), input("Введите тип ресторана -"), input("Введите рейтинг - "))


newRestaurant.Describe()
newRestaurant.Open()
newRestaurant.update_rating(input("Введите новый рейтинг -  "))
newRestaurant.Describe()



print()

restaurant1 = Restaurant(input("Введите начвание ресторана - "), input("Введите тип ресторана -"), input("Введите рейтинг - "))
restaurant2 = Restaurant(input("Введите начвание ресторана - "), input("Введите тип ресторана -"), input("Введите рейтинг - "))
restaurant3 = Restaurant(input("Введите начвание ресторана - "), input("Введите тип ресторана -"), input("Введите рейтинг - "))

restaurant1.Describe()
print()
restaurant2.Describe()
print()
restaurant3.Describe()