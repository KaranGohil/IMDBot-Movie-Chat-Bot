from googletrans import Translator

#Varaible use to translate
translator = Translator()

#Dectects the language and translate it to english. So, code can understand
def detector(sen):
    translations = translator.translate(sen, dest='en')
    return translations.text

#Gets the source language from the input sentence and send into wiki.py
def getSrcLang(sen):
    translations = translator.translate(sen)
    return translations.src


