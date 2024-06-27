########################################################################
class Crash_Handler:
    def __init__(self, wDir, error, mode='run'):
        if mode == 'run':
            print('------------------')
            print('Crash Handler setting up...')
            con = self.convert_path(wDir, '/')
            con = self.split_path(con)
            con = self.assemble_path(con)
            con = self.promote_path(con)
            print('Path formatted...')
            dumps_path = self.assemble_dir(con)
            print('Directory assembled...')
            con = self.get_data(dumps_path)
            self.dump_data(con, error)
            print('Data acquired, dumped...')
            print('------------------')
            print('Crash documented to:', f'{con}')
            print('------------------')
            input('Enter anything to exit: ')
            exit()
        elif mode == 'setup':
            pass
        else:
            print('Invalid crash handler initialization.')
            import sys
            sys.exit()

    def convert_path(self, path, mode):
        n_string = ''
        for letter in path:
            if mode == '/':
                if letter == '\\':
                    n_string += '/'
                else:
                    n_string += letter
            elif mode == '\\':
                if letter == '/':
                    n_string += '\\'
                else:
                    n_string += letter
        return n_string
    
    def split_path(self, path):
        n_string = ''
        n_list = []
        for letter in path:
            if letter == '/':
                n_list.append(n_string)
                n_string = ''
            else:
                n_string += letter
        while n_list[0] == " ":
            n_list.pop(0)
        if n_string:
            n_list.append(n_string)
        return n_list
    
    def assemble_path(self, path_list):
        n_string = ''
        for word in path_list:
            n_string += word
            n_string += '/'
        return n_string
    
    def remove_n_path_index(self, path):
        path_list = self.split_path(path)
        path_list.pop(len(path_list) - 1)
        path = self.assemble_path(path_list)
        return path_list, path
    
    def promote_path(self, path):
        while True:
            path_list, path = self.remove_n_path_index(path)
            if path_list[len(path_list) - 1] == 'everything':
                break
        return path
########################################################################







import os
e = Crash_Handler(
    wDir=None,
    error=None,
    mode='setup'
)

wDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = e.convert_path(wDir, '/')
p = e.split_path(p)
p = e.assemble_path(p)
p = e.promote_path(p)
print(p)