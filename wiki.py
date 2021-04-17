import wikipediaapi
import googletrans as gt

wiki = wikipediaapi.Wikipedia('en')

#Verify if the page exists and send back summary?URL 
def findPageAndUrl(search):
    pageSearch = wiki.page(search) #Might have to add single quotes
    if(pageSearch.exists()):
        print(f"IMDBot: Would you like to know about {search} from wikipedia?")
        reply = input('You: ')
        if('YES' in reply.upper()):
           print("Summary: %s" % pageSearch.summary[0:350])
        else:
            print("IMDBot: Is there is anything else I can help with?")
        
        print("IMDBot: Do you want the wikipedia link for this page for more info?")
        reply = input('You: ')
        if('YES' in reply.upper()):
            print("Here is the link: %s" % pageSearch.fullurl)
        else:
            print("IMDBot: Is there is anything else I can help with?")
    else:
        print("page can not be found")


#find the link/URL of wikipedia in different language and
def findLinkDifLang(search, destLang):
    lang = gt.LANGUAGES  #dict of googletrans libararies provided by the API
    exLang = dict((v,k) for k,v in lang.items()) #exchange the key and value's position

    if(destLang.lower() in exLang):
        langCode = exLang[destLang.lower()] #gets the language code 
        pageSearch = wiki.page(search)
        langlinks = pageSearch.langlinks
        l = langlinks[langCode]
        print(destLang + " - " + l.title + ": "+l.fullurl)

   
    #srcLang = 

