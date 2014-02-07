A simple tool based on "secret" IMDB urls to get the IMDB ratings of a movie.

This tool currently can search with the exact/approx movie name and print it's
rating.

How to use:

    #prints the help menu \m/optparse!
    $ python heyimdb.py --help

    #returns the rating of the movie if movie found, 
    $ python heyimdb.py The Butler
    7.1

    #if unavailable/clashing, displays close results. As of now, find the id of the movie 
    #you need and run the command again. 
    $ python heyimdb.py Redemption 
    Popular Titles:
     tt1893256: Redemption (2013,     <a href='/name/nm1140275/'>Steven Knight</a>)
     tt0111161: The Shawshank Redemption (1994,     <a href='/name/nm0001104/'>Frank Darabont</a>)
     tt1899353: The Raid: Redemption (2011, )
     tt0239195: Survivor (2000 TV series,     <a href='/name/nm0663789/'>Charlie Parsons</a>)
     tt1156466: Undisputed 3: Redemption (2010,     <a href='/name/nm0282708/'>Isaac Florentine</a>)
    Exact Titles:
     tt0218378: The Claim (2000,     <a href='/name/nm0935863/'>Michael Winterbottom</a>)
     tt0065744: The Shiver of the Vampires (1971,     <a href='/name/nm0210811/'>Jean Rollin</a>)
     tt2201886: Redemption (2013/IV documentary short,     <a href='/name/nm0022412/'>Jon Alpert</a>...)
     tt0021292: Redemption (1930,     <a href='/name/nm0629243/'>Fred Niblo</a>...)
     tt0275624: Redemption (2003 video,     <a href='/name/nm0717424/'>Sean A. Reid</a>)
    ...
    #Snipped

    #search with id
    $ python heyimdb.py -i tt0111161
    [u'The Shawshank Redemption', 9.3] 
   


TODO:
 - to add options (currently added, but options dont work)
 - coprehensive suite (rating, cast, summary)
 - better URLs to get data from
