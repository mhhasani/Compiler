class DFA:
    def __init__(self):
        self.alphabet = ['a']
        self.states = ['q0']
        self.transitions = {('q0', 'a'): 'q0'}
        self.start_state = 'q0'
        self.accepting_states = ['q0']

    def run(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.accepting_states

if __name__ == '__main__':
    dfa = DFA()
    print(dfa.run(input('Enter a string: ')))