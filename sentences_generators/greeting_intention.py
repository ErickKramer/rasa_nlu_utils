def generate_greeting_sentences(greets):
    '''
        Generate sentences for the greeting intention.

        Args:
        - greets: List of greetings

        Return:
        - list of sentences
    '''
    tasks_greeting_ = []
    tasks_greeting = []

    tasks_greeting_.append([greet for greet in greets])

    tasks_greeting = [item for sublist in tasks_greeting_ for item in sublist]
    print ("number of 'request_names' sentences", len(tasks_greeting))

    return tasks_greeting
