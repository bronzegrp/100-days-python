import json
import time

file_path = r'/home/gryphon_/python_code/100-days-python/letter/states/states.json'

with open(file_path,'r') as states_file:
    states_data = json.load(states_file)
    


list_states = states_data['states']

def show_states ():
    for state in list_states:
        print('Name:',state['name'])
        print('\n')


def state_info(state_name : str):

    u_input = state_name.capitalize()

    for state in list_states:
        if u_input == state['name']:
            return state
        
show_states()
#print(state_info('alabama'))






