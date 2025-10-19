
---

#### update.md
```bash
cat > update.md <<'EOF'
# UPDATE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

