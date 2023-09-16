from functools import lru_cache
from main import InMemoryNoteRepo, app, note_repo
from fastapi.testclient import TestClient


@lru_cache(maxsize=1)
def note_repo_factory():
    return InMemoryNoteRepo()

app.dependency_overrides[note_repo] = note_repo_factory
test_client = TestClient(app)


def test_add_get_note():
    body = {'text': 'abcd'}
    resp = test_client.post('/notes/', json=body)
    assert resp.status_code == 200

    resp_body = resp.json()
    assert 'uuid' in resp_body
    uid = resp_body['uuid']

    resp = test_client.get(f'/notes/{uid}')
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['text'] == body['text']

