#!/usr/bin/python2.7
""" mapper.py
    mapper code for the project in the DE1 course
"""

import sys
import math

# imports specific to the MSD
import hdf5_getters as GETTERS

def read_input(file):
    i=0 #Counts the number of rows in the file
    
    #Variables for calculating the mean of a feature:
    j=0
    feature=0
    mean_of_feature=0

    #Variables for calculating conditional probabilities for a given feature:
    k=0  #Count low hotness
    kk=0 #Count high hotness
    prob_low_feat_low_hot = 0  #Initialize probabilities as zero
    prob_high_feat_low_hot = 0  #Initialize probabilities as zero
    prob_low_feat_high_hot = 0  #Initialize probabilities as zero
    prob_high_feat_high_hot = 0  #Initialize probabilities as zero
    low_feat_low_hot = 0  #Initialize counts as zero 
    high_feat_low_hot = 0  #Initialize counts as zero 
    low_feat_high_hot = 0  #Initialize counts as zero 
    high_feat_high_hot = 0  #Initialize counts as zero 
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
                        hot_song = 2
                    else:
                        hot_song = 1
                else:
                    hot_song = 0 #Assign zero for NaN
            except AttributeError:
                song_hotttnesss = None
                hot_song = 0  #Assign zero for Null
            try:
                tempo = GETTERS.get_tempo(h5)
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
                year = GETTERS.get_year(h5)
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
                duration = GETTERS.get_duration(h5)
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
            #try:
            #    time_signature = GETTERS.get_time_signature(h5)
            #except AttributeError:
            #    time_signature = None
            #try:
            #    end_of_fade_in = GETTERS.get_end_of_fade_in(h5)
            #except AttributeError:
            #    end_of_fade_in = None
            try:
                danceability = GETTERS.danceability(h5)
                if (not math.isnan(danceability)):
                    Danceability = danceability
                else:
                    Danceability = 0
            except AttributeError:
                danceability = None
                Danceability = 0
            
            ##Calculate conditional probability:
            #feat_prob = Duration
            #if (feat_prob != None and not math.isnan(feat_prob) and feat_prob != 0):  #Only calculate for legitimate values
            #    if (hot_song == 1):
            #        k += 1  #Count how many you sum up for low hotness
            #        if (feat_prob == 1):
            #            low_feat_low_hot += 1
            #        elif (feat_prob == 2):
            #            high_feat_low_hot += 1
            #    elif (hot_song == 2):
            #        kk += 1  #Count how many you sum up for high hotness
            #        if (feat_prob == 1):
            #            low_feat_high_hot += 1
            #        elif (feat_prob == 2):
            #            high_feat_high_hot += 1                 
            #        prob_low_feat_low_hot = low_feat_low_hot / k  #Conditional probability of getting low feature value given low song hotness
            #        prob_high_feat_low_hot = high_feat_low_hot / k   #Conditional probability of getting high feature value given low song hotness
            #        prob_low_feat_high_hot = low_feat_high_hot / kk  #Conditional probability of getting low feature value given high song hotness
            #        prob_high_feat_high_hot = high_feat_high_hot / kk  #Conditional probability of getting high feature value given high song hotness

            feat = danceability  #Input feature that you want to calculate the mean value for!
            if (feat != None and not math.isnan(feat) and feat != 0):  #Only calculate for legitimate values
                feature += feat #Sum up the features
                j += 1.0  #Calculate count how many you sum up
                mean_of_feature = feature / j #Divide sum by number of items to get the mean
            # Return the gotten attributes
            #if (song_hotttnesss != None and not (math.isnan(song_hotttnesss))):   #Uncomment if you only want the values where song_hotttnesss is defined
            yield (hot_song, Tempo, Year, Duration, danceability, mean_of_feature) #, duration, time_signature, end_of_fade_in)

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
