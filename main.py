import string

class TuringMachine:
    def __init__(self, program: list):
        self.program = program

    def run(self, tape: string):
        stop: bool = False
        symbol_num: int = 0
        command_num: int = 0
        while (not stop):
            #because we have two different variants of behavoir:
            if tape[symbol_num] == '1':
                command_num = command_num + 1
            current_command: list = self.program[command_num]
            self.__print_condition__(tape, symbol_num, command_num // 2)
            tape = tape[:symbol_num] + str(current_command[1]) + tape[symbol_num + 1:]

            if current_command[2] == 's':
                symbol_num = symbol_num + 1
                stop = True
                #just another iteration to show the last iteration
                command_num = current_command[0] * 2
                if tape[symbol_num] == '1':
                    command_num = command_num + 1
                current_command: list = self.program[command_num]
                self.__print_condition__(tape, symbol_num, command_num // 2)
            elif current_command[2] == 'r':
                symbol_num = symbol_num + 1
            elif current_command[2] == 'l':
                symbol_num = symbol_num - 1
            
            command_num = current_command[0] * 2

    def __print_condition__(
        self, 
        tape: string, 
        symbol_num: int, 
        command_num: int
        ):
        print(tape, command_num)
        point: string = ' ' * len(tape)
        point = point[:symbol_num] + '↑' + point[symbol_num + 1:] 
        print(point)
        print('-' * len(tape))

#simple program which adds 1 to a number
def test_UN_plus_1():
    prog_UN_plus_1 = [
        [0, 0, 'r'],
        [1, 1, 'r'],
        [0, 1, 's'],
        [1, 1, 'r']
    ]

    data_UN_plus_1 = '00111000'

    machine = TuringMachine(prog_UN_plus_1)
    machine.run(data_UN_plus_1)

#program which multiply number by 2
def test_UN_times_2():
    prog_UN_times_2 = [
        [0, 0, 'r'],
        [1, 0, 'r'],
        [2, 1, 'l'],
        [1, 1, 'r'],
        [3, 0, 'r'],
        [4, 0, 'r'],
        [0, 1, 's'],
        [3, 1, 'r'],
        [5, 1, 'l'],
        [4, 1, 'r'],
        [2, 1, 'l'],
        [5, 1, 'l']
    ]

    data_UN_times_2 = '001111000000000'

    machine = TuringMachine(prog_UN_times_2)
    machine.run(data_UN_times_2)

#program to complete euclidian algorithm
def test_EUC():
    prog_EUC = [
        [0, 0, 'r'],
        [1, 1, 'l'],
        [2, 1, 'r'],
        [1, 1, 'l'],
        [10, 0, 'r'],
        [3, 0, 'r'],
        [4, 0, 'r'],
        [3, 1, 'r'],
        [4, 0, 'r'],
        [5, 0, 'r'],
        [7, 0, 'l'],
        [6, 1, 'l'],
        [6, 0, 'l'],
        [1, 1, 'l'],
        [7, 0, 'l'],
        [8, 1, 'l'],
        [9, 0, 'l'],
        [8, 1, 'l'],
        [2, 0, 'r'],
        [1, 1, 'l'],
        [0, 0, 's'],
        [10, 1, 'r']
    ]

    data_EUC = '0000000000000000001111111111110111111111000000000000000000000000'

    machine = TuringMachine(prog_EUC)
    machine.run(data_EUC)

def main():
    #test_UN_plus_1()
    #test_UN_times_2()
    test_EUC()
    

main()
