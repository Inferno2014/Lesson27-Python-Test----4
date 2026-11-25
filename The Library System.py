class Book():
    def __init__ (self,title,author,mode):
        title == input('Enter title of book: ')
        author == input('Enter name of author: ')
        mode == input('Borrow or Return: ').lower()
        def borrow(self,title,author,mode):
            super().__init__(self,title,author,mode)
            print('You have borrowed',self.title,'and the author is',self.author,'! Please return the book after you are done reading it!')
        def return_book(self,title,author,mode):
            super().__init__(self,title,author,mode)
            print('You have returned',self.title,'and the author is',self.author,'! Thank you for returning the book safely!')
        if mode == 'borrow':
            borrow()
        elif mode == 'return':
            return_book()
b = Book.__init__('self','title','author','mode')