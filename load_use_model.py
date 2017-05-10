import gensim
model = gensim.models.Word2Vec.load_word2vec_format("wiki.en.text.vector", binary=False)

model.most_similar("China")
model.similarity("woman", "man")


#model = gensim.models.Word2Vec.load("wiki.en.text.model")
#model.most_similar("man")
