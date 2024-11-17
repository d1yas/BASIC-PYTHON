class Personal():
    name = None
    age = None
    experience = None

    def set_data(self, name, age, experience):
        print(self.name,self.age, self.experience)


per = Personal()
per.set_data('John', 25, 30)


print(per.name)