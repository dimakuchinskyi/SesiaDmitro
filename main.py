class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        print("Назва: ", self.title)
        print("Автор: ", self.author)
book1 = Book("Війна і мир", "Лев Толстой")
book1.get_info()
book2 = Book("Гра Престолів", "Джордж Мартін")
book2.get_info()
