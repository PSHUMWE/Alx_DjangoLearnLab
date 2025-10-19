cat > bookshelf/retrieve.md <<'EOF'
# RETRIEVE Operation

**Command:**
```python
from bookshelf.models import Book
book = ["Book.objects.get", "1984"]
book
