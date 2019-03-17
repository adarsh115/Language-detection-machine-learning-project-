


import sys
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from gtts import gTTS
import os
import speech_recognition as s
r = s.Recognizer()


def text():
	text = '''
    There's a passage I got memorized. Ezekiel 25:17. "The path of the righteous man is beset on all sides\
    by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity\
    and good will, shepherds the weak through the valley of the darkness, for he is truly his brother's keeper\
    and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger\
    those who attempt to poison and destroy My brothers. And you will know I am the Lord when I lay My vengeance\
    upon you." Now... I been sayin' that shit for years. And if you ever heard it, that meant your ass. You'd\
    be dead right now. I never gave much thought to what it meant. I just thought it was a cold-blooded thing\
    to say to a motherfucker before I popped a cap in his ass. But I saw some shit this mornin' made me think\
    twice. See, now I'm thinking: maybe it means you're the evil man. And I'm the righteous man. And Mr.\
    9mm here... he's the shepherd protecting my righteous ass in the valley of darkness. Or it could mean\
    you're the righteous man and I'm the shepherd and it's the world that's evil and selfish. And I'd like\
    that. But that shit ain't the truth. The truth is you're the weak. And I'm the tyranny of evil men.\
    But I'm tryin', Ringo. I'm tryin' real hard to be the shepherd.
    '''
	return text

def ratio(text):
	languages_ratio = {}
	tokens = wordpunct_tokenize(text)
	words = [word.lower() for word in tokens]

	for l in stopwords.fileids():
		stopwords_set = set(stopwords.words(l))
		words_set = set(words)
		common_words = words_set.intersection(stopwords_set)
		languages_ratio[l] = len(common_words)
	print(languages_ratio)
	return languages_ratio

def detect_language(text):
    ratios = ratio(text)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language

if __name__=='__main__':
	print("THIS IS PROGRAM TO DETECT LANGUAGE")
	print("PRESS 1 TO DETECT LANGUAGE OF PREDEFINED DATA")
	print("PRESS 2 TO ENTER DATA OF YOUR OWN CHOICE")
	print("PRESS 3 TO SPEAK IN LANGUAGE OF YOUR CHOICE")
	print("GIVE THE INPUT........1 or 2 or 3")
	choice = int(input())
	if choice == 1:
		data = text()
	elif choice == 2:
		print("enter data in language of your choice!!!!")
		data = str(input())
	elif choice ==3:
		with s.Microphone() as source:
			print("SPEAK IN YOUR LANGUAGE")
			audio = r.listen(source)
			print("SPEECH RECORDED")
		data = r.recognize_google(audio)
		print("YOUR SPEECH :-" + data)
	else:
		print("WRONG INPUT!!!!!!!!!!!!!!!...TRY AGAIN")
	
	lnguage = detect_language(data)
	
	language = 'en'
	myobj = gTTS(text=lnguage, lang=language, slow=False)
	myobj.save("five.mp3")
	os.system("five.mp3")
	print(lnguage)
