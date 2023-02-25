

states = ('Healthy', 'Fever')

observations = ('normal', 'cold', 'dizzy')

start_probability = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever': {'Healthy': 0.4, 'Fever': 0.6},
}

emission_probability = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
}


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize
    for st in states:
        V[0][st] = start_p[st] * emit_p[st][obs[0]]
        path[st] = [st]
    # Run Viterbi when t > 0
    for t in range(1,len(obs)):
        V.append({})
        newpath = {}

        for curr_st in states:
            paths_to_curr_st = []
            for prev_st in states:
                paths_to_curr_st.append((V[t-1][prev_st] * trans_p[prev_st][curr_st] * emit_p[curr_st][obs[t]], prev_st))
            curr_prob, prev_state = max(paths_to_curr_st)
            V[t][curr_st] = curr_prob
            newpath[curr_st] = path[prev_state] + [curr_st]

        # No need to keep the old paths
        path = newpath
    print(V)
    for line in dptable(V):
        print(line)
    prob, end_state = max([(V[-1][st], st) for st in states])
    return prob, path[end_state]

def dptable(V):
    # Print a table of steps from dictionary
    yield ' ' * 4 + '    '.join(states)
    for t in range(len(V)):
        yield '{}   '.format(t) + '    '.join(['{:.4f}'.format(V[t][state]) for state in V[0]])


def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
print(example())