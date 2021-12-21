class Ebook():
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page_number = 1
        self.is_open = False
    def open(self):
        if not self.is_open:
            self.is_open = True
            print(f"The ebook has been opened on the last read page ({self.current_page_number}).")
        else:
            print("The ebook is already open.")
    def close(self):
        if self.is_open:
            self.is_open = False
            print("The ebook has been closed.")
        else:
            print("The ebook is already closed.")
    def go_to_next_page(self):
        if self.is_open:
            if self.current_page_number == self.number_of_pages:
                print(f"You are at the end (page {self.current_page_number}), there are no more pages.")
            else:
                self.current_page_number += 1
                print(f"You are now on the next page ({self.current_page_number}).")
        else:
            print("The ebook is closed, please open it before trying to switch pages.")
    def go_to_previous_page(self):
        if self.is_open:
            if self.current_page_number == 1:
                print(f"You are at the beginning (page {self.current_page_number}), there are no prior pages.")
            else:
                self.current_page_number -= 1
                print(f"You are now on the previous page ({self.current_page_number}).")
        else:
            print("The ebook is closed, please open it before trying to switch pages.")
    def display_status(self):
        print(f"Ebook status\n - title: {self.title}\n - author: {self.author}\n - number of pages: {self.number_of_pages}\n - current page: {self.current_page_number}\n - state: {'open' if self.is_open else 'closed'}")