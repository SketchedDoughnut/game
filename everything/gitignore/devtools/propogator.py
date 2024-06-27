# this file propogates the one template copy of the crash handler to every other crash handler
# it is built for use with VSCode because paths are wonky
########################################################################
def propogate_crash_handler():
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


def propogate_elevator():
    raw_elevator_file_list = [

    ]

    compiled_elevator_file_list = [

    ]

    elevator_source = ''

    f = open(elevator_source, 'r')
    elevator_source_content = f.read()
    f.close()
    print('Getting contents of source...')

    for file in raw_elevator_file_list:
        f = open(file, 'w')
        f.write(elevator_source_content)
        f.close()
        print('Propogating to raw file:', file)

    for file in compiled_elevator_file_list:
        f = open(file, 'w')
        f.write(elevator_source_content)
        f.close()
        print('Propogating to compiled file:', file)



running = input('-> ')
if running == '1':
    propogate_crash_handler()
elif running == '2':
    propogate_elevator()