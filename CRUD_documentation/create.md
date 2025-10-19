# CREATE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

**Output:**
```python
<Book: 1984 by George Orwell (1949)>
```

**Explanation:**  
Creates a new Book record and saves it in the database using Django ORM.
