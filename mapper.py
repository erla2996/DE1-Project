#!/usr/bin/python2.7
""" mapper.py
    mapper code for the project in the DE1 course
"""

import sys
import math

# imports specific to the MSD
import hdf5_getters as GETTERS

def read_input(file):
    i=0
    for line in file:
        line = line.strip()
        if line != '\n' and line != '':
            i += 1
            # Open input as an h5 file
            h5 = GETTERS.open_h5_file_read(line)
            # Get the needed attributes from the file
            # Some values doesn't exist for all songs, and hdf5_getters doesn't check for existence
            try:
                song_hotttnesss = GETTERS.get_song_hotttnesss(h5)
                if (not math.isnan(song_hotttnesss)):
                    if (song_hotttnesss >0.6):
                        hot_song = 1
                    else:
                        hot_song = 0
            except AttributeError:
                song_hotttnesss = None
            try:
                tempo = GETTERS.get_tempo(h5)
                if tempo > 100:
                    Tempo=1
                else:
                    Tempo=0
            except AttributeError:
                tempo = None
            try:
                year = GETTERS.get_year(h5)
                if year>2005:
                    Year=3
                elif year >=1990:
                    Year = 2
                elif (year < 1990 and year > 0):
                    Year=1
                else:
                    Year = 0
            except AttributeError:
                year = None
            #try:
            #    duration = GETTERS.get_duration(h5)
            #except AttributeError:
            #    duration = None
            #try:
            #    time_signature = GETTERS.get_time_signature(h5)
            #except AttributeError:
            #    time_signature = None
            #try:
            #    end_of_fade_in = GETTERS.get_end_of_fade_in(h5)
            #except AttributeError:
            #    end_of_fade_in = None
            #try:
            #    danceability = GETTERS.danceability(h5)
            #except AttributeError:
            #    danceability = None
            # Return the gotten attributes
            if (song_hotttnesss != None and not (math.isnan(song_hotttnesss))):
                yield (i, song_hotttnesss, hot_song, Tempo, year, Year) #, duration, time_signature, end_of_fade_in)

def main(separator='\t'):
    # Read attributes from STDIN
    data = read_input(sys.stdin)
    for attributes in data:
        # Process attributes, e.g. containerize
        out_data = attributes[2:3]
        # Print to STDOUT
        print('%s%s%d' % (out_data, separator, 1));

if __name__ == "__main__":
    main();
