"""EchoPlot - Plot loudness of a song using the EchoNest API."""

# Author: Alexandre Passant - apassant.net
# Licensed: MIT - see LICENSE.txt


import numpy as np
import matplotlib.pyplot as plt

from pyechonest import config
from pyechonest import song as echosong
from pyechonest import track as echotrack
from pyechonest.util import EchoNestAPIError 

# Default interval
START = 0
END = 10000

# Available catalogs
CATALOGS = [
    "spotify-WW", 
    "7digital-US", 
    "7digital-AU", 
    "7digital-UK", 
    "rdio-US", 
    "rdio-AT", 
    "rdio-AU", 
    "rdio-BR", 
    "rdio-CA", 
    "rdio-CH", 
    "rdio-DE", 
    "rdio-DK", 
    "rdio-ES", 
    "rdio-FI", 
    "rdio-FR", 
    "rdio-IE", 
    "rdio-IT", 
    "rdio-NL", 
    "rdio-NO", 
    "rdio-NZ",
    "rdio-PT",
    "rdio-SE", 
    "rdio-WW", 
    "rdio-EE", 
    "rdio-LT", 
    "rdio-LV", 
    "rdio-IS", 
    "rdio-BE", 
    "rdio-MX", 
    "rdio-GB", 
    "rdio-CZ", 
    "rdio-CO", 
    "rdio-PL", 
    "rdio-MY", 
    "rdio-HK", 
    "rdio-CL", 
    "7digital-ES"
]

class EchoPlot(object):
    """Plot loudness of a song using the Echonest API."""

    def __init__(self, artist, title, start, end):
        self.artist = artist
        self.title = title
        self.start = start and float(start) or START
        self.end = end and float(end) or END

    def _inrange(self, segment):
        """Check if a segment is in the song's analysis range"""
        start = segment.get('start', 0)
        end = start + segment.get('duration')
        return start > self.start and end < self.end

    def plot(self):
        """Plot song data"""
        songs = echosong.search(title=self.title, artist=self.artist, results=1)
        if songs:
            # Search for the track through all catalogues
            for catalog in CATALOGS:
                # Fails when the API Key can't access a catalogue
                try:
                    tracks = songs[0].get_tracks(catalog)
                except EchoNestAPIError:
                    continue
                # Get track or go to next catalogue
                if not tracks:
                    continue
                track = echotrack.track_from_id(tracks[0]['id'])
                # Adjust start and end
                self.start = self.start < track.duration and self.start or 0
                self.end = self.end < track.duration and self.end or track.duration
                # Get full aoustic analysis
                track.get_analysis()
                # Loudness (from segments)
                x = np.array([segment.get('start') for segment in track.segments if self._inrange(segment)])
                y = np.array([segment.get('loudness_max') for segment in track.segments if self._inrange(segment)])
                plt.plot(x, y)
                plt.xlabel('Duration')
                plt.ylabel('Loudness')
                # Use sections as a grid
                [plt.axvline(section.get('start')+section.get('duration'), color='k', linestyle='--') for section in track.sections]
                # Add caption and show plot
                plt.suptitle('%s - %s' %(self.artist, self.title))
                plt.show()
                return

