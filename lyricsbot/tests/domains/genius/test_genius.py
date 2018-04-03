"""
Tests.
"""
import unittest

from ddt import ddt, data, unpack

from lyricsbot.domains.genius.genius import (
    format_request_data_url,
    parse_lyrics
)
from lyricsbot.tests.domains.utils import EXPECTED_GENIUS


@ddt
class TestURL(unittest.TestCase):
    """
    Test for verify data song with url and parser.
    """

    @data(
        (
            'Kopecky',
            'Talk To Me',
            'https://genius.com/Kopecky-talk-to-me-lyrics',
        ),
        (
            'Florence + The Machine',
            'Rabbit Heart (Raise It Up)',
            'https://genius.com/Florence-the-machine-rabbit-heart-raise-it-up-lyrics',
        ),
    )
    @unpack
    def test_format_request_data_url(self, author_song, title_song, expected_url):
        """
        Case: author and title should be indicated in the link.
        Expected: url with concatenated lowercase characters author and title.
        """
        result = format_request_data_url(author_song, title_song)

        self.assertEqual(expected_url, result)

    def test_parse_lyrics(self):
        """
        Case: get song lyrics thru URL.
        Expected: song lyrics.
        """
        url = 'https://genius.com/Kopecky-talk-to-me-lyrics'
        result = parse_lyrics(url)

        self.assertEqual(EXPECTED_GENIUS, result)

    def test_parse_lyrics_without_text(self):
        """
        Case: get song lyrics thru URL.
        Expected: .
        """
        url = 'https://genius.com/Eminem-beautiful-lyrics'
        expected_error = 'The song is not available, sorry.'

        result = parse_lyrics(url)

        self.assertEqual(expected_error, result)

    def test_parse_lyrics_text_exist(self):
        """
        Case: get song lyrics thru URL.
        Expected: .
        """
        url = 'https://genius.com/Emptyself-artificial-light-lyrics'
        expected_text_exist = 'To get song lyrics tap the press me button.'

        result = parse_lyrics(url)

        self.assertEqual(expected_text_exist, result)