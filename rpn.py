from tester import print_test


class RPN:
    def __init__(self):
        self.memory = None  # !!!! sostituisci None con la struttura di memoria più adatta

    def enter(self, number: float):
        pass

    def last(self) -> float:
        pass

    def sum(self) -> float:
        pass

    def diff(self) -> float:
        pass

    def mul(self) -> float:
        pass

    def div(self) -> float:
        pass

    def clear(self):
        pass


def run_test():
    rpn = RPN()
    rpn.enter(4.0)

    rpn.enter(4.0)
    rpn.enter(5.0)
    print_test(1, rpn.sum(), 9.0)

    rpn.enter(8.0)
    rpn.enter(10.0)
    print_test(2, rpn.diff(), -2.0)

    rpn.enter(4.0)
    rpn.enter(30.0)
    print_test(3, rpn.mul(), 120.0)

    rpn.enter(50.0)
    rpn.enter(10.0)
    print_test(4, rpn.div(), 5.0)

    print_test(5, rpn.last(), 5.0)

    rpn.clear()
    print_test(6, rpn.last(), 0.0)


def main():
    run_test()

    rpn = RPN()
    print("Calcolatrice RPN, digita il comanda dopo il simbolo \">\", \"E\" per uscire")
    s = input("> ")
    while s != "E":
        try:
            if s == "":
                print(rpn.last())
            elif s == "+":
                print(rpn.sum())
            elif s == "-":
                print(rpn.diff())
            elif s == "*":
                print(rpn.mul())
            elif s == "/":
                print(rpn.div())
            else:
                rpn.enter(float(s))

        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
            rpn = RPN()

        s = input("> ")


if __name__ == '__main__':
    main()
