from urllib.request import urlretrieve
from urllib.error import HTTPError

from itertools import count

save_directory = './rao-notes/'

note_url = lambda n: f'http://www.eecs70.org/static/notes/n{n}.pdf'
note_file = lambda n: save_directory + f'n{n}.pdf'

for n in count():
    try:
        urlretrieve(note_url(n), note_file(n))
    except HTTPError:
        break
