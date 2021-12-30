# def get_hindi_sw(number):
#     return number + 1
# import os
import codecs
import os.path

stopwords=set()

def get_hindi_sw():
    # stopwords = ['लेकिन','अगर','या','क्यूंकि','जैसा','जब','तक','जबकि','की','पर','द्वारा','के','लिए','साथ']
    # module_path =os.path.dirname(os.path.realpath(__file__))
    # with open(os.path.join(module_path, 'stopwords.txt')) as f:
    # text_file_dir = str(os.path.dirname(__file__)) + '/stopwords.txt'
    # with open(text_file_dir) as f:
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, 'final_hindi_stopwords.txt'), 'r') as f:
        for line in f:
            stopwords.add(line[:-1])
    return stopwords

stopwords = get_hindi_sw()