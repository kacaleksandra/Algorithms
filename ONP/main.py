import os


class Stack:
    stack = []

    def on_top(self, value):
        self.stack.append(value)
        return

    def pop(self):
        return self.stack.pop()

    def return_last(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


def what_priority(char):
    if char == "^":
        return 3
    elif char in "*/":
        return 2
    elif char in "+-":
        return 1
    return 0


def to_or_from(onp_str):
    if onp_str[-1] in "*/+-^":
        return True  # convert from onp
    else:
        return False  # convert to onp


def clear_and_decide(onp_str):
    # clear string
    onp_str = onp_str.replace("\n", "")
    onp_str.strip()
    # decision
    onp_str_r = ""
    if to_or_from(onp_str):
        onp_str_r = from_onp(onp_str)
    else:
        onp_str_r = to_onp(onp_str)
    return onp_str_r


def from_onp(str):
    onp_stack = Stack()
    for char in str:
        if char == " ":
            continue
        if char in '+-*/^':
            temp_a = onp_stack.pop()
            temp_b = onp_stack.pop()
            onp_stack.on_top('(' + temp_b + char + temp_a + ')')
        else:
            onp_stack.on_top(char)
    return onp_stack.return_last()

def to_onp(onp_str):
    onp_stack = Stack()
    output = ""
    for char in onp_str:
        if char == ' ':
            continue
        elif char in "()*/+-^":
            if onp_stack.is_empty() or char == "(":
                onp_stack.on_top(char)
            elif char == ")":
                while onp_stack.return_last() != "(":
                    output += onp_stack.pop()
                onp_stack.pop()
            elif what_priority(char) > what_priority(onp_stack.return_last()):
                onp_stack.on_top(char)
            elif what_priority(char) <= what_priority(onp_stack.return_last()):
                while what_priority(char) <= what_priority(onp_stack.return_last()):
                    output += onp_stack.pop()
                onp_stack.on_top(char)
        else:
            output += char
    while not onp_stack.is_empty():
        output += onp_stack.pop()

    return output

def main():
    if os.path.isfile('./onp.txt'):
        with open('./onp.txt') as file:
            print(clear_and_decide(file.readline()))
    else:
        print("Plik z danymi wejściowymi nie istnieje.")


if __name__ == '__main__':
    main()
