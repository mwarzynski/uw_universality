from z3 import Not, And, Or, Implies, Bool, Solver, unsat
from itertools import combinations

def var_symbol(position, symbol):
    return Bool(f"symbol_{position}_{symbol}")

def var_state(position, state):
    return Bool(f"state_{position}_{state}")

def ensure_only_one_true_of(variables):
    if len(variables) == 1:
        return variables[0] == True
    all_pairs_false = Not(Or([And(list(c)) for c in combinations(variables, 2)]))
    or_all_items_true = Or(list(variables))
    return And(all_pairs_false, or_all_items_true)

def universality(symbols, states, states_initial, states_final, transitions, n):
    constraints = []
    # Generate variables space.
    var_symbols = [{s:var_symbol(i, s) for s in symbols} for i in range(0, n)]
    var_states = [{s:var_state(i, s) for s in states} for i in range(0, n+1)]
    # At each position only one symbol might be true.
    for symbols in var_symbols:
        constraints.append(
            ensure_only_one_true_of(symbols.values())
        )
    # At the beginning automata in every initial state.
    for si in states_initial:
        constraints.append(var_states[0][si] == True)
    # Use transitions to span paths made by the word.
    for i in range(0, n):
        for t in transitions:
            constraints.append(
                # state_i_x and symbol_i_a => state_(i+1)_y
                Implies(And(var_states[i][t[0]], var_symbols[i][t[1]]),
                        var_states[i+1][t[2]]
                )
            )
    # We don't want to accept the word, so all final states should be false.
    for sf in states_final:
        constraints.append(var_states[n][sf] == False)

    solver = Solver()
    solver.add(constraints)
    if n <= 0 or solver.check() == unsat:
        return True, ""
    model = solver.model()

    solution = ['']*n
    for i, symbols in enumerate(var_symbols):
        for s, v in symbols.items():
            if model[v]:
                solution[i] = s
    return False, " ".join(solution)

