class Book:
    book_count = 0

    def __init__(self, title: str, author: str, genre: str, publication_year: int, price: float, availability: bool = True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.__price = price
        self.__availability = availability
        Book.book_count += 1
    
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        self.__price = new_price
    
    def is_available(self):
        return self.__availability

    def set_availability(self, is_ava):
        self.__availability = is_ava

    def display_details(self):
        return f'Book title: {self.title} \nBook author: {self.author} \nBook genre: {self.genre} \nYear of publish: {self.publication_year} \nBook price: {self.__price} \nIs available: {self.__availability}'
    
    def apply_discount(self, discount_persentage):
        return self.__price - self.__price * discount_persentage // 100
    
    def get_book_count (self):
        return Book.book_count


