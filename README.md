# Library Manager

A small program for a campus library that stores books, magazines and DVDs and lets members borrow and return them. It uses classes, inheritance, an abstract class, private attributes and exceptions.

## How to run

```
python3 main.py
```

(on Windows use `python main.py`). No external packages are needed, it runs on Python 3.12+. The output of my final run is saved in `output.txt`.

## Files

- `models.py` - the classes: `LibraryItem` (abstract parent), `Book`, `Magazine`, `DVD` and `Member`
- `main.py` - demo that uses every feature and prints the results
- `output.txt` - console output from running main.py

## Reflection

**1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**

LibraryItem is just a general idea of an item, every real item in the library is a book, magazine or DVD, so it doesn't make sense to create a plain LibraryItem object. Making it abstract with `@abstractmethod` on `late_fee()` forces every child class to write its own late fee. If DVD forgets to write `late_fee()`, Python gives a `TypeError` as soon as you try to create a DVD object (`Can't instantiate abstract class DVD...`), so the mistake is caught early instead of later when a fee is calculated.

**2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?**

You get an `AttributeError` saying the object has no attribute `__available`. This is because Python renames attributes starting with two underscores (name mangling, it becomes `_LibraryItem__available`), so it's hidden from code outside the class. We use `is_available()` because it lets other code read the value without being able to change it directly, the only way to change it is through `mark_borrowed()` and `mark_returned()`, so the item can't end up in a wrong state by accident.

**3. What is the difference between LibraryItem.total_items and self.title?**

`total_items` is a class attribute, so there is only one copy shared by all the objects, and it goes up by 1 every time any item is created (that's why `Book.total_items` and `LibraryItem.total_items` both print 3). `self.title` is an instance attribute, so every object has its own title, changing the title of the book does not affect the magazine or the DVD.
