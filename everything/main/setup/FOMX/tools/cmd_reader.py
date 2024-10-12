'''
This is the command reader used by FOMX.
it reads commands from a file, and does certain actions based on those commands.
Pretty simple!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import shutil

# function for reading commands from a text file
# and executing them (besides propagation)
def read_commands(above_everything_dir: str, cmd_dir: str) -> tuple[bool, bool]:
    # establish the variable representing what to propagate
    # this is returned once the function is done
    propagate = (False, False)

    # access all of the commands, into a list of each line
    f = open(cmd_dir, 'r')
    cmds = f.readlines()
    f.close()
    print('---------------')

    # iterate over each line / command
    for cmd in cmds:
        line = cmd.split()
        cmd = line[0]
        dir = line[1]
        print('cmd:', cmd)
        print('dir:', dir)

        # try each command. if it fails, error then continue
        # this was the best way to handle any errors with the commands
        # or code
        try:

            # if the command is mkdir, make directory
            if cmd == 'mkdir':
                os.mkdir(os.path.join(above_everything_dir, dir))

            # if the command is rmdir, remove directory
            elif cmd == 'rmdir':
                shutil.rmtree(os.path.join(above_everything_dir, dir))

            # if the command is mkfile, make file
            elif cmd == 'mkfile':
                f = open(os.path.join(above_everything_dir, dir), 'w')
                f.close()

            # if the command is rmfile, remove file
            elif cmd == 'rmfile':
                os.remove(os.path.join(above_everything_dir, dir))

            # if the command is propogate, do not propogate. 
            # instead, assign what to do to a variable that is returned later
            elif cmd == 'propagate':
                elevator = propagate[0]
                crash = propagate[1]
                if dir == 'crash':
                    crash = True
                elif dir == 'elevator':
                    elevator = True
                propagate = (elevator, crash)

        except Exception as e:
            print('cmd error:', e)
        print('----- endline -----')

    # once done, return propagation info
    # so FOMX knows what to do later on
    return propagate