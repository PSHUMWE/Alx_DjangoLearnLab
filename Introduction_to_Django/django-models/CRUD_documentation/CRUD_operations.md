# Create Operation

**Command used:**
```python
book = Book.objects.create(title='Django Basics', author='John Doe', publication_year=2024)

---

#### **retrieve.md**
```bash
echo "# Retrieve Operation

**Command used:**
```python
books = Book.objects.all()

---

#### **update.md**
```bash
echo "# Update Operation

**Command used:**
```python
book = Book.objects.get(id=1)
book.title = 'Advanced Django'
book.save()

---

#### **delete.md**
```bash
echo "# Delete Operation

**Command used:**
```python
book = Book.objects.get(id=1)
book.delete()

---

### 🪜 Step 6.5 — (Optionally) Create a Summary File

Create one file that summarizes all the CRUD operations together:
```bash
echo "# CRUD Operations Summary

## Create
\`Book.objects.create(...)\` → Adds a new record.

## Retrieve
\`Book.objects.all()\` → Retrieves all records.

## Update
\`book.title = 'New Title'\` + \`book.save()\` → Updates an existing record.

## Delete
\`book.delete()\` → Deletes a record from the database.


