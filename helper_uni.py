import os
import pickle
import codecs

def load_data(path):
    """
    Load Dataset from File
    """
    input_file = os.path.join(path)
    with codecs.open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()

    return data


def preprocess_and_save_data(dataset_path, token_lookup, create_lookup_tables):
    """
    Preprocess Text Data
    """
    text = load_data(dataset_path)
    
    # Ignore notice, since we don't use it for analysing the data
    #text = text[81:]

    token_dict = token_lookup()
    print ("hello")
    for key, token in token_dict.items():
        t=' {'+ token + ' }'
        text = text.replace(key, t)

    text = text.lower()
    text = text.split()

    vocab_to_int, int_to_vocab = create_lookup_tables(text)
    int_text = [vocab_to_int[word] for word in text]
    pickle.dump((int_text, vocab_to_int, int_to_vocab, token_dict), open('preprocess.all.p', 'wb'))


def load_preprocess():
    """
    Load the Preprocessed Training data and return them in batches of <batch_size> or less
    """
    return pickle.load(open('preprocess.all.p', mode='rb'))


def save_params(params):
    """
    Save parameters to file
    """
    pickle.dump(params, open('params.all.p', 'wb'))


def load_params():
    """
    Load parameters from file
    """
    return pickle.load(open('params.all.p', mode='rb'))
