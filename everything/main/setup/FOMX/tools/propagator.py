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
# builtin modules
import os

# external modules
from rich import print

# file imports
import elevator

# these are the sources for template files
# where the the main code is pulled from, and duplicated to any templates
ABS_ROOT_STEM = elevator.Elevator.elevated + '\\'
ABS_EVERYTHING_STEM = elevator.Elevator.elevated_everything
DEVSOURCE_STEM = ABS_EVERYTHING_STEM + r'\toolsource\devsource'
CRASH_SOURCE = DEVSOURCE_STEM + r'\crash_handler.py'
ELEVATOR_SOURCE = DEVSOURCE_STEM + r'\elevator.py'
COPY_SOURCE = DEVSOURCE_STEM + r'\copy.py'
DOWNLOAD_SOURCE = DEVSOURCE_STEM + r'\download.py'
EXTRACT_SOURCE = DEVSOURCE_STEM + r'\extract.py'
VERIFY_SOURCE = DEVSOURCE_STEM + r'\verify.py'
SELF_SOURCE = os.path.join(os.path.dirname(DEVSOURCE_STEM), 'devtools\propagator.py')

# for below,
# any file that is labeled "raw" means it stays as a Python file.
# any file that is labeled "compiled" means that that file gets bundled
# into the .exe that is made with pyinstaller
# this shows how it is imperative to run the propagation BEFORE compiling
# and not after, because then its useless :P

# this is the list of all the raw / compiled .py files to propagate the elevator to
ELEVATOR_FILES = [
    # raw
    r'everything\main\top\container\index_elevator.py',
    r'everything\main\setup\FOMX\tools\elevator.py',
    r'everything\toolsource\devtools\elevator.py'
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
        r'everything\full-redo\update\tools\copy.py',
        
        # raw
        r'everything\main\setup\update\tools\copy.py'
    ],
    'download': [
        # compiled
        r'everything\full-redo\update\tools\download.py',

        # raw
        r'everything\main\setup\update\tools\download.py',
        r'everything\main\setup\FOMX\tools\download.py'
    ],
    'extract': [
        # compiled
        r'everything\full-redo\update\tools\extract.py',

        # raw
        r'everything\main\setup\update\tools\extract.py',
        r'everything\main\setup\FOMX\tools\extracter.py'
    ],
    'verify': [
        # compiled
        r'everything\full-redo\update\tools\verify.py',

        # raw
        r'everything\main\setup\update\tools\verify.py'
    ]
}

# this is a list containing all of the raw / compiled .py files to propagate the propagator to :P
PROPAGATE_FILES = [
    # raw 
    r'everything\main/setup/FOMX/tools/propagator.py'
]

# this propagates the crash handler template
# to all of its respective files (listed below)
def propagate_crash_handler():

    # getting the contents of the template
    print('[blue]Getting contents of crash handler source...')
    f = open(CRASH_SOURCE, 'r')
    crash_source_content = f.read()
    f.close()

    # propagating template to raw files
    for file in CRASH_FILES:
        f = open(ABS_ROOT_STEM + file, 'w')
        f.write(crash_source_content)
        f.close()
        print('- Propogating to file:', ABS_ROOT_STEM + file)

# this does the same as above, but propagates the elevator file
# to all of its respective files (listed below)
def propagate_elevator():
    # getting the contents of the tempalte
    print('[blue]Getting contents of elevator source...')
    f = open(ELEVATOR_SOURCE, 'r')
    elevator_source_content = f.read()
    f.close()

    # propagating templates to raw files
    for file in ELEVATOR_FILES:
        f = open(ABS_ROOT_STEM + file, 'w')
        f.write(elevator_source_content)
        f.close()
        print('- Propogating to file:', ABS_ROOT_STEM + file)

# this function does the same as above, except it propagates 
# all of the tool files
# which makes maintanence easier as well :D
def propagate_tools():
    # get all of the sources of the templates
    print('[blue]Getting contents of tool sources...')
    with open(COPY_SOURCE) as f: copy_contents = f.read()
    with open(DOWNLOAD_SOURCE) as f: download_contents = f.read()
    with open(EXTRACT_SOURCE) as f: extract_contents = f.read()
    with open(VERIFY_SOURCE) as f: verify_contents = f.read()

    # iterate over all of the respective files and propagate
    for file in TOOL_FILES['copy']:
        print('- Propogating to file:', ABS_ROOT_STEM + file)
        with open(ABS_ROOT_STEM + file, 'w') as f: f.write(copy_contents)
    for file in TOOL_FILES['download']:
        print('- Propogating to file:', ABS_ROOT_STEM + file)
        with open(ABS_ROOT_STEM + file, 'w') as f: f.write(download_contents)
    for file in TOOL_FILES['extract']: 
        print('- Propogating to file:', ABS_ROOT_STEM + file)
        with open(ABS_ROOT_STEM + file, 'w') as f: f.write(extract_contents)
    for file in TOOL_FILES['verify']:
        print('- Propogating to file:', ABS_ROOT_STEM + file)
        with open(ABS_ROOT_STEM + file, 'w') as f: f.write(verify_contents)

def propagate_self():
    # get the source from the template
    print('[blue]Getting contents of propagator sources...')
    with open(SELF_SOURCE) as f: source_contents = f.read()

    # iterate over all of the respective files and propagate
    for file in PROPAGATE_FILES:
        print('- Propagating to file:', ABS_ROOT_STEM + file)
        with open(ABS_ROOT_STEM + file, 'w') as f: f.write(source_contents)

# calling on all functions when this file is ran
# this will only run if the file is being ran
# if it is being imported or otherwise used, 
# the following won't run
if __name__ == '__main__':
    propagate_crash_handler()
    propagate_elevator()
    propagate_tools()
    propagate_self()