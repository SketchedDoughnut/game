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

# this propagates the crash handler template
# to all of its respective files (listed below)
def propagate_crash_handler():
    
    # all the raw files
    # this means that these files are not compiled,
    # they stay as python files
    raw_crash_file_list = [
        r'everything\main\top\container\index_crash_handler.py',
        r'everything\main\top\container\game_data\src\conways-game\conway_crash_handler.py',
        r'everything\main\top\container\game_data\src\flappy\flappy_crash_handler.py',
        r'everything\main\top\container\game_data\src\rhythm\rhythm_crash_handler.py'
    ]

    # all of the compiled files
    # this means that these get bundled into the final compiled product
    # this is why it is VERY important to run this BEFORE compiling
    compiled_crash_file_list = [
        r'everything\main\setup\setup_crash_handler.py'
    ]

    # this is the source template for the crash handler
    crash_source = r'everything\toolsource\dev\crash_handler.py'

    # getting the contents of the template
    print('Getting contents of source...')
    f = open(crash_source, 'r')
    crash_source_content = f.read()
    f.close()

    # propagating template to raw files
    for file in raw_crash_file_list:
        f = open(file, 'w')
        f.write(crash_source_content)
        f.close()
        print('Propogating to raw file:', file)

    # propagating template to compiled files
    for file in compiled_crash_file_list:
        f = open(file, 'w')
        f.write(crash_source_content)
        f.close()
        print('Propogating to compiled file:', file)

# this does the same as above, but propagates the elevator file
# to all of its respective files (listed below)
def propagate_elevator():
    
    # same meaning as the "raw" files above
    # these are just files that are never compiled
    raw_elevator_file_list = [
        r'everything\main\top\container\index_elevator.py'
    ]

    # this is the source template to be spread
    elevator_source = r'everything\toolsource\dev\elevator.py'

    # getting the contents of the tempalte
    print('Getting contents of source...')
    f = open(elevator_source, 'r')
    elevator_source_content = f.read()
    f.close()

    # propagating templates to raw files
    for file in raw_elevator_file_list:
        f = open(file, 'w')
        f.write(elevator_source_content)
        f.close()
        print('Propogating to raw file:', file)

# calling on both functions when this file is ran
propagate_crash_handler()
propagate_elevator()