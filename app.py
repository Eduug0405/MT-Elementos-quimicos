from flask import Flask, render_template, request, jsonify
from elementos import TuringMachine

app = Flask(__name__)
states = {"q0", "q1", "q2", "q3", "q4", "qf"}
initial_state = "q0"
final_states = {"qf"}
transitions = {
    ("q0", "H"): ("q1", "H", "R"),
    ("q1", "+"): ("q2", "+", "R"),
    ("q2", "O"): ("qf", "H2O", "R"),

    ("q0", "Na"): ("q1", "Na", "R"),
    ("q1", "+"): ("q2", "+", "R"),
    ("q2", "Cl"): ("qf", "NaCl", "R"),
}

turing_machine = TuringMachine(states, initial_state, final_states, transitions)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_compound", methods=["POST"])
def get_compound():
    data = request.get_json()
    input_symbols = data.get("input_symbols").replace(" ", "")  
    result = turing_machine.process_input(input_symbols)
    return jsonify({"compound": result})

if __name__ == "__main__":
    app.run(debug=True)
