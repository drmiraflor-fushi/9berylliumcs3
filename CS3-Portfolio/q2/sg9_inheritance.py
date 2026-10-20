class Publication:
  # Set attributes for Publication class
  def __init__(self, title, author):
    self.__title = title
    self.__author = author

    # calling @property enables the functions to be bundled together
    @property
    def get_title(self):
      return f"(self.__title)

    @property
    def get_author(self):
      return f"(self.__author)
      #'get' returns values

    @set_title
    def set_title(self):
      t1 = "Six of Crows"
    
    @set_author(author)
    def set_author(self):
      a1 = "Leigh Bardugo"
      #'set' enables values to be set
  
class Book(Publication):
  # Sets attributes for subclass 'Book' under parent class 'Publication'
  def __init__(self, title, author, number_pages):
    super().__init__(title, author)
    self.number_pages = number_pages

    @property
    def get_number_pages(self):
      return number_pages

    @set_number_of_pages(new_number_pages)
    def number_pages(self):
      np2 = "496"

    @set_title
    def set_title(self):
      t2 = "Once Upon A Broken Heart"
    
    @set_author(author)
    def set_author(self):
      a2 = "Stephanie Garber"
      

class Magazine(Publication):
  # Set attributes for subclass 'Magazine' under parent class 'Publication'
  def __init__(self, title, author, issue_number):
    super().__init__(title, author)
    self.issue_number = issue_number
    
    @get_issue_number(new_issue_number)
    def issue_number(self):
      return issue_number

    @set_issue_number(issue_number)
    def issue_number(self):
      in1 = "1031"

    @set_title
    def set_title(self):
      t3 = "The Umbrella Academy"
    
    @set_author(author)
    def set_author(self):
      a3 = "Gerard Way"
   
# Doesn't work because no functions were called, such as display_info() and others, like set_author, set_issue_number
print("Publication Information:")
print("Title:", t1)
print("Author:", a1)

print("Book Information:")
print("Title:", t2)
print("Author:", a2)
print("Number of pages:", np2)

print("Magazine Information:")
print("Title:", t3)
print("Author:", a3)
print("Issue number:", in1)

      
      
