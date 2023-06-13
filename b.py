import time
import re
from nltk.stem import WordNetLemmatizer
import nltk
import multiprocessing

#nltk.download('wordnet')

class TextPreprocessor:
    def __init__(self, text):
        self.text = text

    def preprocess(self):
        start_time = time.time()

        self.lemmatize()
        self.upper_lower_case()
        self.sentence_segmentation()

        end_time = time.time()

        #print("Parallel Preprocessing time: {} seconds".format(end_time - start_time))

        return self.text

    def lemmatize(self):
        lemmatizer = WordNetLemmatizer()
        self.text = " ".join([lemmatizer.lemmatize(word) for word in self.text.split()])

    def upper_lower_case(self):
        self.text = self.text.lower()

    def sentence_segmentation(self):
        self.text = re.split("(?<=[.!?]) +", self.text)

if __name__ == '__main__':
    with open('New Text Document 3.txt', 'r') as file:
        # Read the content of the file and store it in a variable
        text = file.read()

    #text = "This is an example sentence. Another example sentence is coming up next! Finally, here is the last example sentence."
    preprocessor = TextPreprocessor(text)

    num_cores = 3
    print("Number of cores: {}".format(num_cores))

    pool = multiprocessing.Pool(num_cores)

    start_time = time.time()
    parallel_preprocessed_text = pool.apply(preprocessor.preprocess)
    end_time = time.time()

    pool.close()
    pool.join()

    print("Parallel Total time: {} seconds".format(end_time - start_time))

    print("Parallel Preprocessing Text : ")
    print(parallel_preprocessed_text)