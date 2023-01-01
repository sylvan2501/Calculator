class Calculator:
    def __init__(self):
        self.operator = None
        self.first_num = None
        self.second_num = None
        self.result = None

    def __del__(self):
        print('The object is deconstructed.')

    def set_operator(self, operator):
        self.operator = operator

    def set_first_num(self, first_num):
        self.first_num = first_num

    def set_second_num(self, second_num):
        self.second_num = second_num

    def set_result(self, result):
        self.result = result

    def interface_prompt(self):
        self.set_first_num(float(input('Please enter the first number: \n')))
        self.set_second_num(float(input('Please enter the second number: \n')))
        self.set_operator(input('Please enter the operator: \n'))
        if self.operator == '+':
            self.set_result(self.first_num + self.second_num)
        elif self.operator == '-':
            self.set_result(self.first_num - self.second_num)
        elif self.operator == '*':
            self.set_result(self.first_num * self.second_num)
        elif self.operator == '/':
            if self.second_num == 0:
                print('Invalid result !!')
                return
            else:
                self.set_result(self.first_num / self.second_num)
        else:
            print('invalid operator!!')
            return
        print(f'Your result is {self.result}')



