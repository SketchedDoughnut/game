all_releases = 'https://api.github.com/repos/SketchedDoughnut/development/releases?page=1&per_page=10000'

import requests

# get requests json
all_response = requests.get(all_releases).json()

# setup var(s)
release_data = []

# parse response_data
for response in all_response:
    label = response['body'].split()[0]
    mode = response['body'].split()[1]
    release_data.append([label, mode])
print('----------------------------')
print('Loaded releases parsed')

# eval
print('Evaluating...')

def find_mode(current):
    for i in release_data:
        if i[0] == current:
            print('Mode found:', i[1])
            current_mode = i[1]
    for i in release_data

def eval_modes(current: str):
    # get mode based off of current
    print('----------------------------')
    print('Getting mode based off of label...')
    find_mode(current)

    # measure
    ran_true = False

    for rd in release_data:
        if rd[0] == current: # if labels equal
            print('Scan has returned to previous, finishing.')
            break
        else:
            if current_mode == 'game_data':
                if rd[1] == 'top':
                    print(f'Promoting {current_mode} to {rd[1]}')
                    current_mode = rd[1]
                elif rd[1] == 'full':
                    print(f'Promoting {current_mode} to {rd[1]}')
                    current_mode = rd[1]
            elif current_mode == 'top':
                if rd[1] == 'full':
                    print(f'Promoting {current_mode} to {rd[1]}')
                    current_mode = rd[1]

    print('----------------------------')
    print('Mode promoted to:', current_mode)
    return current_mode, state, ran_true

#current_mode, m_detect = eval_modes()
#print('Mode promoted to:', current_mode)