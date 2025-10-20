# Django Models – Advanced Relationships

### Overview
In this task, I explored Django’s ORM capabilities by creating models that demonstrate different types of relationships — `ForeignKey`, `ManyToMany`, and `OneToOne`. This helped me understand how to represent complex data connections in a Django project.

---

### Steps I Followed

1. **Created a new app** called `relationship_app` using:
   ```bash
   python manage.py startapp relationship_app
Defined the models in models.py:

Author has many Books (ForeignKey)

Library contains many Books (ManyToMany)

Librarian is linked to one Library (OneToOne)

Applied migrations using:

bash
Copy code
python manage.py makemigrations relationship_app
python manage.py migrate
Created sample queries in query_samples.py:

Get all books by a specific author

List all books in a library

Retrieve the librarian for a library

Result
The models and queries work as expected. I can now easily query related data in Django using relationships.

Folder Structure
markdown
Copy code
django-models/
│
├── LibraryProject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── relationship_app/
    ├── models.py
    ├── query_samples.py
    ├── views.py
    └── ...

