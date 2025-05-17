# %%
corpus = ["This is the first document." ,
          "This document is the second document.",
          "And this is the third one.",
          "Is this the first document?"]

print("Training Corpus: ")
for doc in corpus:
    print(doc)



# %%
unique_chars = set()
for doc in corpus:
    for char in doc:
        unique_chars.add(char)
        
print(unique_chars)

# %%
vocab = list(unique_chars)
vocab.sort()

end_word = "</w>"
vocab.append(end_word)

print("Initial Vocabulary: ")
print(vocab)
print(f"Vocab size is {len(vocab)}")

# %% 
# Pre-tokenise corpus
word_splits = {}
for doc in corpus:
    words = doc.split(' ')
    for word in words:
        if word:
            char_list = list(word) + [end_word]
            # use tuple for immutability
            word_tuple = tuple(char_list)
            if word_tuple not in word_splits:
                word_splits[word_tuple] = 0
            word_splits[word_tuple] += 1

print("\nPre-Tokenised Word Frequencies: ")
print(word_splits)

# %%
import collections

def get_pair_stats(splits):
    pair_counts = collections.defaultdict(int)
    for word_tuple, freq in splits.items():
        symbols = list(word_tuple)
        for i in range(len(symbols)-1):
            pair = (symbols[i], symbols[i+1])
            pair_counts[pair] += freq
    return pair_counts
# %%
