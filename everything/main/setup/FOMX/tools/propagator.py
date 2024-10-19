'''
This file is the propagator for the FOMX system.
Its job is to propagate the crash handlers and elevators where necessary. Simple!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''
def propagate_crash_handler(wDir: str):
    raw_crash_file_list = [
        r'everything\main\top\container\index_crash_handler.py',
        r'everything\main\top\container\game_data\src\conways-game\conway_crash_handler.py',
        r'everything\main\top\container\game_data\src\flappy\flappy_crash_handler.py',
        r'everything\main\top\container\game_data\src\rhythm\rhythm_crash_handler.py'
    ]

    compiled_crash_file_list = [
        r'everything\main\setup\setup_crash_handler.py'
    ]

    crash_source = r'everything\toolsource\devsource\crash_handler.py'

    f = open(wDir +  crash_source, 'r')
    crash_source_content = f.read()
    f.close()
    print('-> FOMX: Getting contents of source...')

    for file in raw_crash_file_list:
        f = open(wDir + file, 'w')
        f.write(crash_source_content)
        f.close()
        print('-> FOMX: Propogating to raw file:', file)

    for file in compiled_crash_file_list:
        f = open(wDir + file, 'w')
        f.write(crash_source_content)
        f.close()
        print('-> FOMX: Propogating to compiled file:', file)


def propagate_elevator(wDir: str):
    raw_elevator_file_list = [
        r'everything\main\top\container\index_elevator.py'
    ]

    elevator_source = r'everything\toolsource\devsource\elevator.py'

    f = open(wDir + elevator_source, 'r')
    elevator_source_content = f.read()
    f.close()
    print('-> FOMX: Getting contents of source...')

    for file in raw_elevator_file_list:
        f = open(wDir + file, 'w')
        f.write(elevator_source_content)
        f.close()
        print('-> FOMX: Propogating to raw file:', file)


def propagate_master(wDir: str, elevator: bool = False, crash: bool = False):
    wDir += '\\'
    if elevator: propagate_elevator(wDir)
    if crash: propagate_crash_handler(wDir)