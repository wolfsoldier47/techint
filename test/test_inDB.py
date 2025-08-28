
from app.db.inmemoryDB import InMemDB


def test_create_and_get_note():
    db = InMemDB()
    note_id = db.create_note("Test Title", "Test Content")
    note = db.get_note(note_id)
    assert note is not None
    assert note["title"] == "Test Title"
    assert note["content"] == "Test Content"

def test_update_note():
    db = InMemDB()
    note_id = db.create_note("Old Title", "Old Content")
    updated = db.update_note(note_id, title="New Title", content="New Content")
    assert updated
    note = db.get_note(note_id)
    assert note["title"] == "New Title"
    assert note["content"] == "New Content"

def test_update_note_partial():
    db = InMemDB()
    note_id = db.create_note("Title", "Content")
    db.update_note(note_id, title="Partial Update")
    note = db.get_note(note_id)
    assert note["title"] == "Partial Update"
    assert note["content"] == "Content"

def test_delete_note():
    db = InMemDB()
    note_id = db.create_note("Title", "Content")
    deleted = db.delete_note(note_id)
    assert deleted
    assert db.get_note(note_id) is None

def test_list_notes():
    db = InMemDB()
    ids = [db.create_note(f"Title {i}", f"Content {i}") for i in range(3)]
    notes = db.list_notes()
    assert len(notes) == 3
    for i, note_id in enumerate(ids):
        assert notes[note_id]["title"] == f"Title {i}"
        assert notes[note_id]["content"] == f"Content {i}"

def test_get_nonexistent_note():
    db = InMemDB()
    assert db.get_note(999) is None

def test_update_nonexistent_note():
    db = InMemDB()
    assert not db.update_note(999, title="Nope")

def test_delete_nonexistent_note():
    db = InMemDB()
    assert not db.delete_note(999)
