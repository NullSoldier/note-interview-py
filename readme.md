# Note app API
Create a flask API for a note taking app.

The API should allow the user to do the following:

 * Get all notes
 * Get a note by id
 * Create a note
 * Update a note
 * Delete a note


Here is an example of how to use the note taking database.

```python
from database import Database, Note

note = Note("grocery list", "eggs,bananas")
Database.writeNote(note)

note = Database.getNote(note.id)
print(note.message)
```
