import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
t1='i am a girl and boy'
t2='i am a boy'
vectorizer=CountVectorizer()
t1_vector=vectorizer.fit_transform([t1])
t2_vector=vectorizer.transform([t2])
print((t1_vector-t2_vector).toarray())
#证明了coo-matrix之间是可以进行四则运算的，但是当需要用正常形式的时候比如scipy.linagl.norm(coo-matrix.toarray())