import nltk
print '--------start--------'

def unusual_words(text):
	text_vocab = set(w.lower() for w in text if w.isalpha())
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)

print unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))[:10]