'''
This is a tool used during build, which propagates template files to other directories.
This was developed because I did not want to maintain a variety of different files individually,
when they all have the same code. Instead, this copies code from a single template file all of the other files!
This means that I only have ot maintain one, and all of the others get updated. This lets all of them recieve 
updates at the sane tune, the FOMX system has a variant of this.
Therefore, it is most important to call on this before releasing a build!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''


def propagate_crash_handler():
    raw_crash_file_list = [
        r'everything\main\top\container\index_crash_handler.py',
        r'everything\main\top\container\game_data\src\conways-game\conway_crash_handler.py',
        r'everything\main\top\container\game_data\src\flappy\flappy_crash_handler.py',
        r'everything\main\top\container\game_data\src\rhythm\rhythm_crash_handler.py'
    ]

    compiled_crash_file_list = [
        r'everything\main\setup\setup_crash_handler.py'
    ]

    crash_source = r'everything\gitignore\dev\crash_handler.py'

    f = open(crash_source, 'r')
    crash_source_content = f.read()
    f.close()
    print('Getting contents of source...')

    for file in raw_crash_file_list:
        f = open(file, 'w')
        f.write(crash_source_content)
        f.close()
        print('Propogating to raw file:', file)

    for file in compiled_crash_file_list:
        f = open(file, 'w')
        f.write(crash_source_content)
        f.close()
        print('Propogating to compiled file:', file)


def propagate_elevator():
    raw_elevator_file_list = [
        r'everything\main\top\container\index_elevator.py'
    ]

    elevator_source = r'everything\gitignore\dev\elevator.py'

    f = open(elevator_source, 'r')
    elevator_source_content = f.read()
    f.close()
    print('Getting contents of source...')

    for file in raw_elevator_file_list:
        f = open(file, 'w')
        f.write(elevator_source_content)
        f.close()
        print('Propogating to raw file:', file)

propagate_crash_handler()
propagate_elevator()