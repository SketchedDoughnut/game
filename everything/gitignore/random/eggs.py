all_releases = 'https://api.github.com/repos/SketchedDoughnut/development/releases?page=1&per_page=10000'

import requests

# get requests json
all_response = requests.get(all_releases).json()

# setup var(s)
release_data = []

# current data(s)
current = '3432805'
current_mode = 'game_data'

# parse response_data
for response in all_response:
    label = response['body'].split()[0]
    mode = response['body'].split()[1]
    release_data.append([label, mode])
print('---------------------------')
print('Loaded releases parsed')

# display
print(f"""---------------------------
Release data:
- Amount of releases detected: {len(all_response)}/10000
- current label: {current}
- current mode: {current_mode}
- Succession chart: game_data > top > full
---------------------------""")

# eval
print('Evaluating...')
print('---------------------------')
def eval_modes():
    # vars
    local_mode = current_mode
    valid_promote = ['top', 'full']

    # measure
    ran_true = False

    for rd in release_data:
        if rd[0] == current:
            print('Scan has returned to previous, finishing.')
            break
        else:
            if local_mode != valid_promote[0]:
                print(f'- promoting {local_mode} to {rd[1]}')
                local_mode = rd[1]
                valid_promote.pop(0)
                ran_true = True

    print('---------------------------')
    return local_mode, ran_true

current_mode, m_detect = eval_modes()
print('Mode promoted to:', current_mode)