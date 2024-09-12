import pandas

my_data = pandas.read_csv("50_states.csv")

states = my_data.state.to_list()

state_dict = {}

for i in range(len(states)):
    state = my_data[my_data.state == states[i]]
    position = (state.x.item(), state.y.item())
    state_dict[states[i]] = position


