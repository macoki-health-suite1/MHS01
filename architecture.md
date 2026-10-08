# MHS Architecture

MHS is a React/Vite frontend backed by Django REST Framework. The database schema is owned by Django migrations. Uploaded media is stored outside Git and is represented by `media/.gitkeep` in the repository.

The organisation hierarchy is the foundation for multi-facility operation. Patients belong to an organisation and facility. Additional clinical modules will reference these core entities rather than creating competing patient or organisation records.
