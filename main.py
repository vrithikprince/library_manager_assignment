# main.py
from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 45)
dvd = DVD("Inception", 3, 148)

priya = Member("Priya", 101)
rahul = Member("Rahul", 102, max_items=1)

# 1. Borrowing with error handling
print("=== 1. Borrowing ===")
try:
    priya.borrow(book)
    print("Priya borrowed:", book.describe())
    rahul.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Borrow limit error and not-borrowed error
print("\n=== 2. More errors ===")
try:
    rahul.borrow(magazine)
    print("Rahul borrowed:", magazine.describe())
    rahul.borrow(dvd)  # rahul can only have 1 item
except ValueError as e:
    print("Could not borrow:", e)

try:
    priya.return_item(dvd)  # priya never borrowed the dvd
except ValueError as e:
    print("Could not return:", e)

print("Priya has:", priya.borrowed_titles())
print("Rahul has:", rahul.borrowed_titles())

# returning things properly
print("\n=== Returning items ===")
try:
    fee = priya.return_item(book, days_late=3)
    print(f"Priya returned {book.title}, late fee: Rs {fee}")
    fee = rahul.return_item(magazine)
    print(f"Rahul returned {magazine.title}, late fee: Rs {fee}")
except ValueError as e:
    print("Could not return:", e)

# now that rahul gave back the magazine he has space again
try:
    rahul.borrow(dvd)
    print("Rahul borrowed:", dvd.describe())
except ValueError as e:
    print("Could not borrow:", e)

print("Priya has:", priya.borrowed_titles())
print("Rahul has:", rahul.borrowed_titles())

# 3. Polymorphism: one loop, no type checks
print("\n=== 3. Late fees for 3 days ===")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("\n=== 4. Class attribute ===")
print("Total items created:", Book.total_items)
print("Same value through LibraryItem:", LibraryItem.total_items)

# 5. Encapsulation - trying to read the private variable directly
print("\n=== 5. Encapsulation ===")
try:
    print(dvd.__available)
except AttributeError as e:
    print("AttributeError:", e)
print("Is the DVD available?", dvd.is_available())
print("Is the book available?", book.is_available())

# 6. LibraryItem is abstract so we can't make an object of it
print("\n=== 6. Abstract class ===")
try:
    thing = LibraryItem("x", 1)
except TypeError as e:
    print("TypeError:", e)
