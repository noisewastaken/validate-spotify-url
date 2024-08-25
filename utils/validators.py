import re

def extract_and_validate_spotify_uri(url):
    """
    Extract Spotify URI from a URL or validate the given Spotify URI.
    """

    match = re.match(r"^https://open\.spotify\.com/(track|playlist)/([a-zA-Z0-9]+)", url)
    
    if match:
        uri_type, uri_id = match.groups()
        spotify_uri = f"spotify:{uri_type}:{uri_id}"
    else:
        spotify_uri = url

    playlist_pattern = r"^spotify:playlist:[a-zA-Z0-9]{22}$"
    song_pattern = r"^spotify:track:[a-zA-Z0-9]{22}$"

    if not re.match(playlist_pattern, spotify_uri) and not re.match(song_pattern, spotify_uri):
        raise ValueError("Invalid Spotify URI")

    return spotify_uri