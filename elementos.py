class TuringMachine:
    def __init__(self, states, initial_state, final_states, transitions):
        self.states = states
        self.current_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.tape = []
        self.head_position = 0

    def process_input(self, input_symbols):
        self.tape = list(input_symbols)
        self.head_position = 0

        while self.current_state not in self.final_states:
            symbol = self.tape[self.head_position] if self.head_position < len(self.tape) else " "
            if (self.current_state, symbol) in self.transitions:
                next_state, write_symbol, move = self.transitions[(self.current_state, symbol)]
                self.tape[self.head_position] = write_symbol
                self.current_state = next_state
                if move == "R":
                    self.head_position += 1
                elif move == "L":
                    self.head_position -= 1
            else:
                break

       
        compound_map = {
            "H+O": "H2O",
            "Na+Cl": "NaCl",
            "C+O": "CO2",
            "Fe+O": "FeO",
            "Ca+C+O": "CaCO3",
            "C+H": "CH4",
            "N+H": "NH3",
            "C+H+O": "C2H5OH",
            "H+Cl": "HCl",
            "C+N+H": "HCN",
            "Ca+O": "CaO",
            "C+O+H": "COH",
            "Fe+C": "FeC",
            "Pb+O": "PbO",
            "Mg+C+O": "MgCO3",
            "Al+O": "Al2O3",
            "Cu+Cl": "CuCl2",
            "C+H+N+O": "CHNO",
            "Fe+S": "FeS",
            "C+H+N": "CHN",
            "Pb+S": "PbS",
            "Fe+Cl": "FeCl3",
            "B+O": "B2O3",
            "K+C+O": "K2CO3",
            "Cr+O": "CrO3",
            "B+H": "BH3",
            "Na+S+O": "Na2SO4",
            "B+C": "BC",
            "P+H": "PH3",
            "Hg+O": "HgO"
        }
        
        input_string = "".join(self.tape)
        return compound_map.get(input_string, "Compuesto no encontrado")
