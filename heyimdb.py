import optparse
import urllib2
import json

parser = optparse.OptionParser()
#parser.add_option("-a", "--approx",
                  #dest="approx",
                  #action="store_true",
                  #default="false",
                  #help="Include approx results")
#parser.add_option("-p", "--print",
                  #dest="print",
                  #action="store_true",
                  #default="false",
                  #help="Print fetcher results")
#parser.add_option("-f", "--file",               #the long and short option
                    #dest="filename",            #name in the options dict
                    #help="write report to FILE",#help text for --help
                    #metavar="FILE")             #notice the help text.
#parser.add_option("-q", "--quiet",              #again, option names
                    #dest="verbose",             #name in options dict
                    #action="store_false",       #special way to say, store False
                    #default="true",             #default value
                    #help="dont print the status messages")
#(options, args) = parser.parse_args()           #notice, returned list is unpacked
#print options, args                             #refer the output in the next section
#
# ./<scriptname> -f filename -q other-arguments
# ./<scriptname> -qf filename other-arguments
# ./<scriptname> -q -ffilename other-arguments
# ./<scriptname> --quiet --file filename other-arguments
# all these will give an output 
# options                                  args
# {'verbose': False, 'filename': 'myfile'} [other-arguments, ]

(options, args) = parser.parse_args()

def get_data(id, field=None):
  """Gets IMDB data (field if field mentioned) by doing a simple HTTP query.
  A hack from http://ubuntuincident.wordpress.com/2012/02/12/get-imdb-ratings-without-any-scraping/
  """
  req = urllib2.Request("http://app.imdb.com/title/maindetails?tconst="+id)
  handler = urllib2.urlopen(req)
  result = json.loads(handler.read())
  if field:
    return result['data'][field]
  else:
    return result['data']
 
#q will store the query movie name
q = "+".join(args)

#right now, we will just pass the movie name to the query
request = urllib2.Request("http://imdb.com/xml/find?json=1&s=tt&q="+q)

#get the request
handler = urllib2.urlopen(request)

#parse the text as json
result = json.loads(handler.read())

#try to understand the results:
categories = [ ["title_popular", "Popular Titles"],
              ["title_exact", "Exact Titles"],
              ]
if False:
  categories.append(["title_approx", "Approx Titles"])


#Application:

if 'title_popular' in result.keys():
  print get_data(result['title_popular'][0]['id'], 'rating')

else:
  for k, n in categories:
    if k in result.keys():
      print n+":"
      for item in result[k]:
        print " Title:", item['title']
        print " Description:", item['description']
        print " Id:", item['id']


