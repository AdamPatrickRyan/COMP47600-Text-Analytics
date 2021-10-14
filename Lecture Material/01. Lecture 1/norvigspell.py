# Norvig Spelling Corrector

import re, collections, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(),os.path.dirname(__file__)))
print(__location__)

file_name = os.path.join(__location__, 'big.txt')
print(file_name)

def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(open(file_name).read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

i','me’,'my’,'myself’,'we’,'our’,'ours’,'ourselves’,'you’,'your’,'yours’,\
         'yourself’,'yourselves’,'he’,'him’,'his’,'himself’,'she’,'her’,'hers’,\
         'herself’,'it’,'its’,'itself’,'they’,'them’,'their’,'theirs’,'themselves’,\
         'what’,'which’,'who’,'whom’,'this’,'that’,'these’,'those’,'am’,'is’,'are’,\
         'was’,'were’,'be’,'been’,'being’,'have’,'has’,'had’,'having’,'do’,'does’,\
         'did’,'doing’,'a’,'an’,'the’,'and’,'but’,'if’,'or’,'because’,'as’,'until’,\
         'while’,'of’,'at’,'by’,'for’,'with’,'about’,'against’,'between’,'into’,\
         'through’,'during’,'before’,'after’,'above’,'below’,'to’,'from’,'up’,\
         'down’,'in’,'out’,'on’,'off’,'over’,'under’,'again’,'further’,'then’,\
         'once’,'here’,'there’,'when’,'where’,'why’,'how’,'all’,'any’,'both’,\
         'each’,'few’,'more’,'most’,'other’,'some’,'such’,'no’,'nor’,'not’,'only’,\
         'own’,'same’,'so’,'than’,'too’,'very’,'s’,'t’,'can’,'will’,'just’,'don’,\
         'should’,'now’,'d’,'ll’,'m’,'o’,'re’,'ve’,'y’,'ain’,'aren’,'couldn’,'didn’,\
         'doesn’,'hadn’,'hasn’,'haven’,'isn’,'ma’,'mightn’,'mustn’,'needn’,'shan’,\
         'shouldn’,'wasn’,'weren’,'won’,'wouldn’