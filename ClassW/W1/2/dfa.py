class DFA:
    def __init__(self):
        self.alphabet = ['0', '1', '2']
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']
        self.transitions = {('q0', '0'): 'q0', ('q0', '1'): 'q1', ('q0', '2'): 'q2', ('q1', '0'): 'q1', ('q1', '1'): 'q4', ('q1', '2'): 'q3', ('q2', '0'): 'q2', ('q2', '1'): 'q3', ('q2', '2'): 'q5', ('q3', '0'): 'q3', ('q3', '1'): 'q5', ('q3', '2'): 'q7', ('q4', '0'): 'q4', ('q4', '1'): 'q6', ('q4', '2'): 'q5', ('q5', '0'): 'q5', ('q5', '1'): 'q7', ('q6', '0'): 'q6', ('q6', '1'): 'q5', ('q6', '2'): 'q7', ('q7', '0'): 'q7'}
        self.start_state = 'q0'
        self.accepting_states = ['q7']

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