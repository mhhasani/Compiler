from graphviz import Digraph

    
class DFA:
    def __init__(self, alphabet, states, transitions, start_state, accepting_states):
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.dfa_code = self.generate_dfa_code()
        self.dfa_graph = self.generate_dfa_graph()
        
    def generate_dfa_code(self):
        code = [
            f"class DFA:",
            f"    def __init__(self):",
            f"        self.alphabet = {self.alphabet}",
            f"        self.states = {self.states}",
            f"        self.transitions = {self.transitions}",
            f"        self.start_state = '{self.start_state}'",
            f"        self.accepting_states = {self.accepting_states}",
            f"",
            f"    def run(self, input_string):",
            f"        current_state = self.start_state",
            f"        for symbol in input_string:",
            f"            current_state = self.transitions.get((current_state, symbol))",
            f"            if current_state is None:",
            f"                return False",
            f"        return current_state in self.accepting_states",
            f"",
            f"if __name__ == '__main__':",
            f"    dfa = DFA()",
            f"    print(dfa.run(input('Enter a string: ')))"
        ]
        
        code = "\n".join(code)

        with open("dfa.py", "w") as f:
            f.write(code)
        
        return code
    
    
    def generate_dfa_graph(self):
        dot = Digraph(comment='DFA')
        
        for state in self.states:
            if state in self.accepting_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state, shape='circle')
        
        for (state, symbol), next_state in self.transitions.items():
            dot.edge(state, next_state, label=symbol)
        
        dot.attr('node', shape='none')
        dot.edge('', self.start_state)
        
        file = dot.render('dfa.gv', format='png')
        return file


if __name__ == '__main__':
    states = input("Enter the states, separated by a space: ").split()
    initial = input("Enter the initial state: ")
    accepting = input("Enter the accepting states, separated by a space: ").split()
    alphabet = input("Enter the alphabet, separated by a space: ").split()
    transitions = {}
    while True:
        transition = input("Enter a transition with the format {state}:{symbol}>{next_state} (or press enter to finish): ")
        if transition == "":
            break
        state, symbol, next_state = transition.split(":")[0], transition.split(":")[1].split(">")[0], transition.split(":")[1].split(">")[1]
        transitions[(state, symbol)] = next_state
        
    dfa = DFA(alphabet, states, transitions, initial, accepting)



    


        

