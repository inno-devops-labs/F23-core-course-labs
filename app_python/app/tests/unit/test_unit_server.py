import os
from server.server import Visits


def test_visits():
    test_file_path = '/tmp/visits_temp_file.txt'
    try:
        os.remove(test_file_path)
    except OSError:
        pass  # rm -f

    visits = Visits(test_file_path)
    assert visits.get_visits() == 0
    for i in range(1, 11):
        visits.increment_visits()
        assert visits.get_visits() == i

    visits = None
    visits = Visits(test_file_path)
    visits.increment_visits()
    assert visits.get_visits() == i + 1
