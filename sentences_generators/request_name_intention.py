def generate_request_name_sentences(names):
    '''
        Generate sentences for the request_name intention.

        Args:
        - names: List of names

        Return:
        - list of sentences
    '''
    tasks_request_name_ = []
    tasks_request_name = []

    tasks_request_name_.append(['my name is [' + name +'] (name)' for name in names])
    tasks_request_name_.append(['[' + name +'] (name)' for name in names])
    tasks_request_name_.append(['people know me as [' + name +'] (name)' for name in names])
    tasks_request_name_.append(['i was named [' + name +'] (name)' for name in names])
    tasks_request_name_.append(['i am [' + name +'] (name)' for name in names])
    tasks_request_name_.append(['i am referred to as [' + name +'] (name)' for name in names])
    tasks_request_name_.append(['people call me [' + name +'] (name)' for name in names])

    tasks_request_name = [item for sublist in tasks_request_name_ for item in sublist]
    print ("number of 'request_names' sentences", len(tasks_request_name))

    return tasks_request_name
