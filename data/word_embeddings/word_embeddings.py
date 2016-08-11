from gensim import models

words = open("words.txt", "r")
output = open("form_300.we", "w")

fname = "GoogleNews-vectors-negative300.bin"
model = models.Word2Vec.load_word2vec_format(fname, binary=True)

for word in words:
    word = word.split()
    if word:
        word = word[0]
        if word in model.vocab:
            output.write(word + "  ")
            for element in model[word]:
                output.write(str(round(float(element),7)) + " ")
            output.write("\n")
