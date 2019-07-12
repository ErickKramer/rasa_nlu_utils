import sys
sys.path.append('../../sentences_generators')
from find_intention import generate_find_sentences
from greeting_intention import generate_greeting_sentences
from request_name_intention import generate_request_name_sentences

def extract_words(file_path):
    '''
        Iterate over text files to store the words into lists.

        Args:
        - file_path: Path to the text file.

        return:
        - list of words contained in the text file 
    '''
    f = open(file_path)
    words = []
    for line in f.readlines():
        words.append(line.rstrip("\n"))

    return words

def generate_training_script(file_path, intentions):
    '''
        Generate a markdown file with the structure required to train a rasa nlu model.

        Args:
        - file_path: Path where to write the markdown file.
        - intentions: Dictionary with intentions as keys and lists of sentences as values.
    '''

    f = open(file_path, "w")

    for intention, sentences in intentions.items():

        f.write('## intent:{}\n'.format(intention))

        for sentence in sentences:
            f.write('- ' + sentence + '\n')

        f.write('\n')
    f.close()

if __name__ == '__main__':

    # ----- Vocabulary -----
    # Loading greetings
    greets_file_path = "../../words_collections/greets.txt"
    greets = extract_words(greets_file_path)

    # # Loading locations
    # locations_file_path = "../../words_collections/locations.txt"
    # locations = extract_words(locations_file_path)

    # Loading names
    names_file_path = "../../words_collections/names.txt"
    names = extract_words(names_file_path)

    # Loading intros
    intros_file_path = "../../words_collections/intros.txt"
    intros = extract_words(intros_file_path)

    # ----- Training sentences -----
    intentions = {}

    greeting_sentences = generate_greeting_sentences(greets)
    intentions['greeting'] = greeting_sentences

    find_sentences = generate_find_sentences(names, intros)
    intentions['find'] = find_sentences

    request_name_sentences = generate_request_name_sentences(names)
    intentions['request_names'] = request_name_sentences

    # ----- training file -----
    training_file = "find_my_mate_sentences.md"
    generate_training_script(training_file, intentions)
