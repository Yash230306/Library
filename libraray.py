import sys
class Libraray:
    def __init__(self, list, name):
        self.list=list
        self.name=name
        self.dict={}
    def displaybook(self):
        print("We have following books")
        for book in self.list:
            print(book)
    def addboook(self, book):
        self.list.append(book)
        print("Book has been added")
    def lendbook(self,user,book):
        if book not in self.dict.keys():
            self.dict.update({user:book})
            print(f"Your {book} book has been updated.You add book now")
        elif book in self.dict.keys():
            print("Book is already lended")
    def returnbook(self,  book):
        if book not in self.dict.keys():
            print("This book is already in your libraray ")
        elif book in self.dict.keys():
            self.dict.pop()
            print("Book has been removed")


if __name__ == '__main__':
    while True:    
        bharat=Libraray(["Bharat" , "Toofani"],"Bharat")
        b=input("Press 1 to display books \nPress 2 to lend the book \nPress 3 to add the book. \nPress 4 to return the book")
        if b=="1":
            bharat.displaybook()
        elif b=="2":
            book=input("Enter the book name")
            user=input("Enter you name ")
            bharat.lendbook(user,book)
        elif b=="3":
            book=input("Enter the book name")
            bharat.addboook(book)
        elif b=="4":
            book=input("Enter the book name")
            bharat.returnbook(book)
        c=input("Press q to quit to exit and c to continue ")
        if c=="q":
            sys.exit()
        elif c=="c":
            continue 
