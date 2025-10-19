# RETRIEVE Operation

**Command:**
```python
from bookshelf.models import Book
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)
```

**Output:**
```python
1984 George Orwell 1949
```

**Explanation:**  
Retrieves all Book records from the database and displays their details.
