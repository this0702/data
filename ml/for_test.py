import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
t1='i am a boy'
t2='i am a girl'
t1_vector=CountVectorizer.transform([t1])
t2_vector=CountVectorizer.transform([t2])
print((t1_vector-t2_vector).toarray())
