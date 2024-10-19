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

# these are the sources for template files
# where the the main code is pulled from, and duplicated to any templates
DEVSOURCE_STEM = r'everything\toolsource\devsource'
CRASH_SOURCE = DEVSOURCE_STEM + r'\crash_handler.py'
ELEVATOR_SOURCE = DEVSOURCE_STEM + r'\elevator.py'
COPY_SOURCE = DEVSOURCE_STEM + r'\copy.py'
DOWNLOAD_SOURCE = DEVSOURCE_STEM + r'\download.py'
EXTRACT_SOURCE = DEVSOURCE_STEM + r'\extract.py'
VERIFY_SOURCE = DEVSOURCE_STEM + r'\verify.py'

# for below,
# any file that is labeled "raw" means it stays as a Python file.
# any file that is labeled "compiled" means that that file gets bundled
# into the .exe that is made with pyinstaller
# this shows how it is imperative to run the propagation BEFORE compiling
# and not after, because then its useless :P

# this is the list of all the raw / compiled .py files to propagate the elevator to
ELEVATOR_FILES = [
    # raw
    r'everything\main\top\container\index_elevator.py'
    ]

# this is the list of all of the raw / compiled .py files to propagate the crash handler to
CRASH_FILES = [
    # raw
    r'everything\main\top\container\index_crash_handler.py',
    r'everything\main\top\container\game_data\src\conways-game\conway_crash_handler.py',
    r'everything\main\top\container\game_data\src\flappy\flappy_crash_handler.py',
    r'everything\main\top\container\game_data\src\rhythm\rhythm_crash_handler.py',

    # compiled
    r'everything\main\setup\setup_crash_handler.py'
    ]

# this is a dictionary of lists of all of the raw / compiled .py files to propagate the tools to
TOOL_FILES = {
    'copy': [
        # compiled
        r'everything\\full-redo\update\tools\copy.py',
        
        # raw
        r'everything\main\setup\update\tools\copy.py'
    ],
    'download': [
        # compiled
        r'everything\full-redo\update\tools\download.py',

        # raw
        r'everything\main\setup\update\tools\download.py'
    ],
    'extract': [
        # compiled
        r'everything\full-redo\update\tools\extract.py',

        # raw
        r'everything\main\setup\update\tools\extract.py'
    ],
    'verify': [
        # compiled
        r'everything\full-redo\update\tools\verify.py',

        # raw
        r'everything\main\setup\update\tools\verify.py'
    ]
}

# this propagates the crash handler template
# to all of its respective files (listed below)
def propagate_crash_handler():

    # getting the contents of the template
    print('Getting contents of crash handler source...')
    f = open(CRASH_SOURCE, 'r')
    crash_source_content = f.read()
    f.close()

    # propagating template to raw files
    for file in CRASH_FILES:
        f = open(file, 'w')
        f.write(crash_source_content)
        f.close()
        print('Propogating to file:', file)

# this does the same as above, but propagates the elevator file
# to all of its respective files (listed below)
def propagate_elevator():
    # getting the contents of the tempalte
    print('Getting contents of elevator source...')
    f = open(ELEVATOR_SOURCE, 'r')
    elevator_source_content = f.read()
    f.close()

    # propagating templates to raw files
    for file in ELEVATOR_FILES:
        f = open(file, 'w')
        f.write(elevator_source_content)
        f.close()
        print('Propogating to file:', file)

# this function does the same as above, except it propagates 
# all of the tool files
# which makes maintanence easier as well :D
def propagate_tools():
    # get all of the sources of the templates
    print('Getting contents of tool sources...')
    with open(COPY_SOURCE) as f: 
        copy_contents = f.read()
    with open(DOWNLOAD_SOURCE) as f: download_contents = f.read()
    with open(EXTRACT_SOURCE) as f: extract_contents = f.read()
    with open(VERIFY_SOURCE) as f: verify_contents = f.read()

    # iterate over all of the respective files and propagate
    for file in TOOL_FILES['copy']:
        print('Propogating to file:', file)
        with open(file, 'w') as f: f.write(copy_contents)
    for file in TOOL_FILES['download']:
        print('Propogating to file:', file)
        with open(file, 'w') as f: f.write(download_contents)
    for file in TOOL_FILES['extract']: 
        print('Propogating to file:', file)
        with open(file, 'w') as f: f.write(extract_contents)
    for file in TOOL_FILES['verify']:
        print('Propogating to file:', file)
        with open(file, 'w') as f: f.write(verify_contents)


# calling on both functions when this file is ran
propagate_crash_handler()
propagate_elevator()
propagate_tools()