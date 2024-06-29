#imports
import os
import shutil

def read_commands(above_everything_dir, cmd_dir) -> tuple[bool, bool]:
    propogate = (False, False)
    f = open(cmd_dir, 'r')
    cmds = f.readlines()
    f.close()
    print('---------------')
    for cmdd in cmds:
        line = cmdd.split()
        cmd = line[0]
        dir = line[1]
        print('cmd:', cmd)
        print('dir:', dir)
        try:
            if cmd == 'mkdir':
                os.mkdir(os.path.join(above_everything_dir, dir))
            elif cmd == 'rmdir':
                shutil.rmtree(os.path.join(above_everything_dir, dir))
            elif cmd == 'mkfile':
                f = open(os.path.join(above_everything_dir, dir), 'w')
                f.close()
            elif cmd == 'rmfile':
                os.remove(os.path.join(above_everything_dir, dir))
            elif cmd == 'propogate':
                elevator = propogate[0]
                crash = propogate[1]
                if dir == 'crash':
                    crash = True
                elif dir == 'elevator':
                    elevator = True
                propogate = (elevator, crash)
        except Exception as e:
            print('cmd error:', e)
        print('----- endline -----')