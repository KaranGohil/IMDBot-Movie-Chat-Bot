from googletrans import Translator

#Varaible use to translate
translator = Translator()

#Dectects the language and translate it to english. So, code can understand
def detector(sen):
    translations = translator.translate(sen, dest='en')
    return translations.text

#This function translate english sentences into desire language
def translateInto(sen):
    pass


