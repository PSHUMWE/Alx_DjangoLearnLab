# DELETE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
```

**Output:**
```python
(1, {'bookshelf.Book': 1})
<QuerySet []>
```

**Explanation:**  
Deletes the Book record from the database and confirms that no records remain.
