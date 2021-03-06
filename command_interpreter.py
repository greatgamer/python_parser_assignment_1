import sys
import command_line
import interactive_shell


class Interpreter:

    def __init__(self, args):
        self.command = command_line.CommandLine()
        self.comm = None  # command given by user
        self.input_file = None
        self.output_file = 'output.csv'
        self.check_command_line(args)
        self.run_command()

    def check_command_line(self, args):
        '''
        command_line [command] -i [input] -o [output]
        '''
        # print(args)
        self.comm = args[1]
        # print('command', self.comm)
        index = 0
        for arg in args:
            if arg == '-i':
                self.input_file = args[index + 1]
            elif arg == '-o':
                self.output_file = args[index + 1]
            index += 1

    def run_command(self):
        '''
        Commands:
        help, file-uml, to-csv, csv-uml, pickle, pickle-uml, validate
        '''
        if self.comm == 'file-uml':
            self.command.create_class_diagram(self.input_file)
        elif self.comm == 'to-csv':
            params = self.input_file + ' ' + self.output_file
            self.command.create_csv(params)
        elif self.comm == 'csv-uml':
            self.command.load_csv_for_uml(self.input_file)
        elif self.comm == 'pickle':
            self.command.pickle_module(self.input_file)
        elif self.comm == 'pickle-uml':
            self.command.pickle_to_uml()
        elif self.comm == 'validate':
            self.command.validate_code(self.input_file)
        elif self.comm == '-help' or self.comm == 'help' or self.comm == '-h':
            self.help()

    def help(self, filename='help.txt'):
        try:
            with open(filename) as helpfile:
                for line in helpfile:
                    print(line.replace('\n', ''))
            return True
        except FileNotFoundError:
            print('Requested helpfile could not be found')
            return False
        except:
            print('Could not find any help.')
            return False


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('For help using the command line write: '
              'command_interpreter.py -help')
        interactive_shell.InteractiveShell()
    else:
        # print(sys.argv)
        interpret = Interpreter(sys.argv)
