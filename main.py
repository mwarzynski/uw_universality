from automata import Automata

def parse_input():
    def from_line():
        return input().split(" ")
    _, _, _, _, m = map(int, from_line())
    words = list(from_line())
    states = list(from_line())
    states_initial = list(from_line())
    states_finite = list(from_line())
    transitions = []
    for _ in range(0, m):
        transitions.append(list(from_line()))
    n = list(map(int, from_line()))[0]
    return words, states, states_initial, states_finite, transitions, n

def main():
    data = list(parse_input())
    description = data[:-1]
    n = data[-1]
    automata = Automata(*description)
    does_satisfy, counter_example = automata.universality(n)
    if does_satisfy:
        print("YES")
    else:
        print("NO\n")
        print(counter_example)

if __name__ == "__main__":
    main()
