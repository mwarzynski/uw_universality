from automata import universality

def parse_input():
    def from_line():
        return input().split()
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
    args = list(parse_input())
    does_satisfy, counter_example = universality(*args)
    if does_satisfy:
        print("YES")
    else:
        print(f"NO\n\n{counter_example}")

if __name__ == "__main__":
    main()
