import random


class User:
    def generation_of_user_data(self):
        self.list_FirstName = ['pavel', 'nikita', 'andrey', 'nastya', 'emil']
        self.list_LastName = ['Grekov', 'ignate', 'vinogradov', 'smirnoff', 'andreev']

        self.FirstName = random.choice(self.list_FirstName)
        self.LastName = random.choice(self.list_LastName)
        self.Email = self.FirstName + self.LastName + str(random.randint(150, 777)) + '@email.ru'

        self.Password = str(random.randint(150, 777)) + self.FirstName + str(random.randint(150, 777))

        return self.FirstName, self.Email, self.Password

