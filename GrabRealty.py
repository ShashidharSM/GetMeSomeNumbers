# Does NOT follow PEP8 Naming Conventions!
# Author: Shashidhar Murthy Sreedhara (c) 2018 for Citron Solutions (not-yet)Inc, Canada

import urllib2, sys, getopt
from bs4 import BeautifulSoup

#Globals
baseurl = "https://www.kijiji.ca/b-house-for-sale/gta-greater-toronto-area/3+bathrooms-2+bedrooms+den__3+bedrooms__4+bedrooms/page-2/c35l1700272a220a217r40.0?ad=offering"
constructedurl = "https://www.kijiji.ca/b-house-for-sale/gta-greater-toronto-area/3+bathrooms-2+bedrooms+den__3+bedrooms__4+bedrooms/page-2/c35l1700272a220a217r40.0?ad=offering"


def usage_information():
    print "Usage:\n"
    print '\tGrabRealty {-P or --provider} -r or --radius <20|30|50|100 in KM> -a or --area <GTA,Vancouver,etc>'
    print '\n\tExample: \n\t\tGrabRealty -P Kijiji -r 50 -a GTA'
    sys.exit(3)


def main(argv):
    # These parameters are hard coded, for now:
    urlRealtyProvider = "Kijiji"
    searchArea = "GTA"
    searchRadius = 30
    bedrooms = 3
    bathrooms = 2 #Possible values: 1,1.5,2,2.5,3,3.5,4,4.5,5,5.5; We aren't considering houses for people who need more than 5 bathrooms
    try:
        opts, args = getopt.getopt(argv, "hP:r:a:b:B:", ["provider=", "help=", "radius=", "area=", "bedrooms=", "bath="])
    except getopt.GetoptError:
        print "No Options Provided/Incorrect Input"
        usage_information()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage_information()
        elif opt in ("-p", "--provider"):
            urlRealtyProvider = arg
        elif opt in ("-r", "--radius"):
            searchRadius = arg
        elif opt in ("-a", "--area"):
            searchArea = arg
        elif opt in ("-B", "--bath"):
            searchArea = arg
        elif opt in ("-b", "--bedrooms"):
            searchArea = arg

    print 'Here is what you ordered! \nArea: {0}\nSearch Radius: {1}\nProvider: {2}\nTHANK YOU!'.format(searchArea, searchRadius, urlRealtyProvider)
    open_url()


def open_url():
    page = urllib2.urlopen(constructedurl)
    soup = BeautifulSoup(page, 'lxml')
    soup.prettify()
    all_titles = soup.find_all("div", class_="title")

    print all_titles

if __name__ == "__main__":
    main(sys.argv[1:])
