def generate_find_sentences(names, intros):
    '''
        Generate sentences for the find intention.

        Args:
        - names: List of names
        - intros: List of intros 

        Return:
        - list of sentences
    '''

    tasks_find = []
    tasks_find_ = []

    tasks_find_.append(['find [' + name + '](name)' for name in names])
    tasks_find_.append(['look for [' + name + '](name)' for name in names])
    tasks_find_.append(['locate [' + name + '](name)' for name in names])
    tasks_find_.append(['spot [' + name + '](name)' for name in names])

    tasks_find_.append([ intro + ' find [' + name + '](name)' for intro in intros for name in names])
    tasks_find_.append([ intro  +  ' look for [' + name + '](name)' for intro in intros  for name in names])
    tasks_find_.append([ intro  +  ' locate [' + name + '](name)' for intro in intros  for name in names])
    tasks_find_.append([ intro  +  ' spot [' + name + '](name)' for intro in intros  for name in names])

    tasks_find_.append(['find [' + name + '](name)' + ' [' + name + '](name)' for name in names])
    tasks_find_.append(['look for [' + name + '](name)' + ' [' + name + '](name)' for name in names])
    tasks_find_.append(['locate [' + name + '](name)' + ' [' + name + '](name)' for name in names])
    tasks_find_.append(['spot [' + name + '](name)' + ' [' + name + '](name)' for name in names])

    tasks_find_.append(['find [' + name + '](name)' + ' [' + name + '](name)' + ' [' + name + '](name)' for name in names])
    tasks_find_.append(['look for [' + name + '](name)' + ' [' + name + '](name)' + ' [' + name + '](name)' for name in names])
    tasks_find_.append(['locate [' + name + '](name)' + ' [' + name + '](name)' + ' [' + name + '](name)' for name in names])
    tasks_find_.append(['spot [' + name + '](name)' + ' [' + name + '](name)' + ' [' + name + '](name)'  for name in names])

    tasks_find = [item for sublist in tasks_find_ for item in sublist]
    print ("number of 'find' sentences", len(tasks_find))

    return tasks_find
