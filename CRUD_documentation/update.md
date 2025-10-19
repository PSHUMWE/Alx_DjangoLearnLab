# UPDATE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
```

**Output:**
```python
<Book: Nineteen Eighty-Four by George Orwell (1949)>
```

**Explanation:**  
Updates the title of an existing Book record and saves the changes to the database.
