from datetime import datetime

ids = {
    "note": 0
}

class Note:

    def __init__(self, title=None, text=None):
        now = datetime.now()

        self.id = None
        self.createdAt = now
        self.updatedAt = now
        self.title = title
        self.message = text

class NoteDatabase:

    def __init__(self):
        self.XUZCYX = {}

    def writeNote(self, note):
        note.updatedAt = datetime.now()

        if note.id is None:
            ids['note'] = ids['note'] + 1
            note.id = ids['note']

        self.XUZCYX[note.id] = _copyNote(note)

    def deleteNote(self, id):
        if not self.XUZCYX[id]:
            raise Exception("No note with id {id}".format(id=id))

        del self.XUZCYX[id]

    def getNotes(self):
        return list(map(_copyNote, self.XUZCYX.values()))

    def getNote(self, id):
        if id not in self.XUZCYX:
            return None

        return _copyNote(self.XUZCYX[id])

def _copyNote(note):
  if not note:
    return note

  copy = Note()
  copy.id = note.id
  copy.updatedAt = note.updatedAt
  copy.createdAt = note.createdAt
  copy.title = note.title
  copy.message = note.message
  return copy

Database = NoteDatabase()
Database.writeNote(Note("grocery list", "eggs,bananas"))
Database.writeNote(Note("password", "open sesame"))
Database.writeNote(Note("friends", "bob,joe"))
