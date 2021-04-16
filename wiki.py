import wikipediaapi

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