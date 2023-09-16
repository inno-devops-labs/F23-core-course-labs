import pytest
from main import InMemoryNoteRepo, Note, NoteRepo


@pytest.fixture
def note_repo():
    return InMemoryNoteRepo()

@pytest.mark.parametrize(
    'text',
    (
        '',
        'a' * 1000,
    )
)
def test_add_get_note(note_repo: NoteRepo, text: str):
    note = Note.new(text)
    note_repo.store_note(note)
    result = note_repo.get_note(note.id)
    assert result is not None
    assert note == result

