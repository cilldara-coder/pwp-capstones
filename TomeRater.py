#-----------------------------
#Tome Rater - Brendan McEvoy
#
#------------------------------

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return(self.email)

    def change_email(self, address):
        new_email = address
        self.email = new_email
        print("The email address of " + str(self.name) +" has been updated")

    def __repr__(self):
        books_read = len(self.books)
        return("User: "+ str(self.name) + ", email: " + str(self.email) + ", books read: " + str(books_read) ) 

    def __eq__(self, other_user):
        other_name = other_user.name
        other_email = other_user.email
        if ((self.name in other_name) and (self.email in other_email)):
            return("Users are equal")
        else:
            return("Users are not equal")
    
    def read_book(self,book, rating=None):
        self.books[book] = rating
        
    def get_average_rating(self):
        tot_rates = 0
        for i in self.books.values():
            tot_rates += i
        avg_rate = tot_rates / len(self.books)
        return(avg_rate)

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return(self.title)
    
    def get_isbn(self):
        return(self.isbn)
        
    def set_isbn(self, change_isbn):
        self.isbn = change_isbn
        print("The ISBN of " + str(self.title) +" has been updated")
        
    def add_rating(self, new_rating):
        if new_rating and 0 <= new_rating <= 4:
            self.ratings.append(new_rating)
        else:
            print("Invalid Rating..." + str(new_rating))
    
    def __eq__(self, other_book):
        other_title = other_book.title
        other_isbn = other_book.isbn
        if ((self.title in other_title) and (self.isbn in other_isbn)):
            return("Books are equal")
        else:
            return("Books are not equal")
            
    def get_average_rating(self):
        tot_rates = 0
        for i in self.ratings:
            tot_rates += i
        
        avg_rate = tot_rates / len(self.ratings)
        return(avg_rate)
        

    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def __repr__(self):
        return("{title} and {isbn}".format(title=self.title, isbn = self.isbn))

#Check ISBN for unique values    
    def check_isbn(self, new_isbn):
        #print("New_ISBN = " +str(new_isbn))
        isbn_list = [book.get_isbn() for book in self.books.keys()]
        if new_isbn in isbn_list:
            print("ISBN ("+str(new_isbn)+") in use")
            return(True)
        else:
            #print ("ISBN available")
            return(False)
            
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return(self.author)
    
    def __repr__(self):
        return("{title} by {author}".format(title=self.title, author = self.author))

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return(self.subject)
        
    def get_level(self):
        return(self.level)
        
    def __repr__(self):
        return("{title}, a {level} manual on {subject}".format(title=self.title, level = self.level, subject = self.subject))
        

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self,title, isbn):
        #print("in Create Book")
        if Book.check_isbn(self, isbn) == False:
            print("Creating Book..." + str(title))
            return Book(title, isbn)
        else:
            print("Failed to create book - ISBN not unique")
           
    def create_novel(self,title, author, isbn):
        if Book.check_isbn(self, isbn) == False:
            print("Creating Novel..." + str(title))
            return Fiction(title, author, isbn)
        else:
            print("Failed to create novel - ISBN not unique")
    
    def create_non_fiction(self,title, subject, level, isbn):
        if Book.check_isbn(self, isbn) == False:
            print("Creating Non-fiction..." + str(title))
            return Non_Fiction(title, subject, level, isbn)
        else:
            print("Failed to create non-fiction - ISBN not unique")
    
    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] +=1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}".format(email))
        
    def add_user(self, name, email, user_books = None):
        new_user = User(name,email)
        print("Attempting to add user " + str(new_user.email))
        if "@" not in new_user.email:
            print("Invalid email ("+str(email)+") - no @ symbol")
        elif (".com" not in new_user.email) and (".org" not in new_user.email) and (".edu" not in new_user.email):
            print("Invalid email ("+str(email)+") - wrong extension")
        else:
            if new_user.email in self.users:
                print("User email already exists")
            else:
                self.users[email] = new_user
                if user_books is not None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
                
    def print_catalog(self):
        #print("In print_catalog")
        for book in self.books.keys():
           print(book)
            
    def print_users(self):
        print("Printing Users...")
        for i in self.users.values():
            print(i)
            
    def get_most_read_books(self):
        count = 0
        most_read = ""
        for i in self.books.keys():
            if self.books[i] > count:
                count = self.books[i]
            if self.books[i] == count:
                most_read = i
        return(most_read)
        
    def highest_rated_book(self):
        highest_rating = 0
        top_rated = ""
        for i in self.books.keys():
            if Book.get_average_rating(i) > highest_rating:
                highest_rating = Book.get_average_rating(i)
                top_rated = Book.get_title(i)
        return(top_rated)
        
    def most_positive_user(self):
        highest_rating = 0
        top_rated = ""
        for i in self.users.values():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                top_rated = i
        return(top_rated)
        
        
                         