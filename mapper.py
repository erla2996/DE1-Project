#!/usr/bin/python2.7
""" mapper.py
    mapper code for the project in the DE1 course
"""

import tables

# Code from hdf5_getters.py

def open_h5_file_read(h5filename):
    """
    Open an existing H5 in read mode.
    Same function as in hdf5_utils, here so we avoid one import
    """
    return tables.open_file(h5filename, mode='r')

def get_release(h5,songidx=0):
    """
    Get release from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.release[songidx]

def get_song_hotttnesss(h5,songidx=0):
    """
    Get song hotttnesss from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.song_hotttnesss[songidx]

def get_duration(h5,songidx=0):
    """
    Get duration from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.duration[songidx]

def get_tempo(h5,songidx=0):
    """
    Get tempo from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.tempo[songidx]

def get_year(h5,songidx=0):
    """
    Get release year from a HDF5 song file, by default the first song in it
    """
    return h5.root.musicbrainz.songs.cols.year[songidx]

import sys
import math

def read_input(file):
    i=0 #Counts the number of rows in the file

    for line in file:
        line = str(line.strip("\n"))
        line = line[1:]
        line = "/home/ubuntu/" + line
        if line != '\n' and line != '':
            i += 1
            # Open input as an h5 file
            h5 = open_h5_file_read(line)
            # Get the needed attributes from the file
            # Some values doesn't exist for all songs, and hdf5_getters doesn't check for existence
            try:
                song_hotttnesss = get_song_hotttnesss(h5)
                if (not math.isnan(song_hotttnesss)):
                    if (song_hotttnesss >0.6):
                        hot_song = 2
                    else:
                        hot_song = 1
                else:
                    hot_song = 0 #Assign zero for NaN
            except AttributeError:
                song_hotttnesss = None
                hot_song = 0  #Assign zero for Null
            try:
                tempo = get_tempo(h5)
                if (not math.isnan(tempo)):
                    if tempo > 100:
                        Tempo = 2
                    else:
                        Tempo = 1
                else:
                    Tempo = 0  #Assign zero if NaN
            except AttributeError:
                tempo = None
                Tempo = 0  #Assign zero if null
            try:
                year = get_year(h5)
                if (not math.isnan(year)):
                    if (year>2005):
                        Year = 3  #new
                    elif year >=1990:
                        Year = 2  #somewhat new
                    elif (year < 1990 and year > 0):
                        Year = 1  #old songs
                    else:
                        Year = 0  #Assign zero if year is zero or negative number
                else:
                    Year = 0  #Assign zero if NaN
            except AttributeError:
                year = None
                Year = 0  #Assign zero if null
            try:
                duration = get_duration(h5)
                if (not math.isnan(duration)):
                    if (duration > 202):
                        Duration = 2
                    elif (duration > 0):
                        Duration = 1
                    else:
                        Duration = 0 #Assign zero if erroneus or missing input
                else:
                    Duration = 0 #Assign zero if NaN
            except AttributeError:
                duration = None
                Duration = 0 #Assign zero if Null
            # Return the gotten attributes
            if (song_hotttnesss != None and not (math.isnan(song_hotttnesss))):   #Uncomment if you only want the values where song_hotttnesss is defined
                yield (hot_song, Tempo, Year, Duration)

def main(separator='\t'):
    # Read attributes from STDIN
    data = read_input(sys.stdin)
    for attributes in data:
        # Process attributes, e.g. containerize
        out_data = attributes
        # Print to STDOUT
        print('%s%s%d' % (out_data, separator, 1));

if __name__ == "__main__":
    main();
