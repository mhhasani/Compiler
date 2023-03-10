class DFA:
    def __init__(self):
        self.alphabet = ['a', 'b']
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
        self.transitions = {('q0', 'a'): 'q1', ('q0', 'b'): 'q2', ('q1', 'a'): 'q0', ('q1', 'b'): 'q5', ('q2', 'b'): 'q3', ('q3', 'b'): 'q4', ('q4', 'b'): 'q3', ('q5', 'b'): 'q6', ('q6', 'b'): 'q5'}
        self.start_state = 'q0'
        self.accepting_states = ['q0', 'q3', 'q5']

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