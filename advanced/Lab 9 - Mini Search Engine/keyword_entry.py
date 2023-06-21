"""
Alex Yazdani
CWID: 20399751

Code taken from Eric Reed, Foothill College, Spring/Summer 2023
"""

class KeywordEntry:

    def __init__(self, word: str, url: str = None, location: int = None):
        self._word = word.upper()
        if url:
            self._sites = {url: [location]}
        else:
            self._sites = {}

    def add(self, url: str, location: int) -> None:
        if url in self._sites:
            self._sites[url].append(location)
        else:
            self._sites[url] = [location]

    def get_locations(self, url: str) -> list:
        try:
            return self._sites[url]
        except IndexError:
            return []

    @property
    def sites(self) -> list:
        return [key for key in self._sites]

    def __lt__(self, other):
        if isinstance(other, KeywordEntry):
            return self._word < other._word
        else:
            return self._word < other.upper()

    def __gt__(self, other):
        if isinstance(other, KeywordEntry):
            return self._word > other._word
        else:
            return self._word > other.upper()

    def __eq__(self, other):
        if isinstance(other, KeywordEntry):
            return self._word == other._word
        else:
            return self._word == other.upper()

    def __hash__(self):
        return hash(self._word)
    