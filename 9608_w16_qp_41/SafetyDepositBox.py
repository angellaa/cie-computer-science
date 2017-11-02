class SafetyDepositBox:

    # (b) (i)
    def __init__(self):
        self._code = ''
        self._state = 'Open-NoCode'

    # (b) (ii)
    def reset(self):
        self._code = ''

    # (b) (iii)
    def setState(self, state):
        self._state = state
        print(state)

    # (b) (iv)
    def setNewCode(self, code):
        self._code = code
        print("Current code is: {0}".format(code))

    # (b) (v)
    def _valid(self, s):
        return s.isdigit() & (len(s) == 4)

    # (b) (vi)
    def stateChange(self):
        Chars = input("Enter code: ")

        if Chars == "R":
            if self._state == "Open-CodeSet":
                self.reset()
                self.setState("Open-NoCode")

        elif Chars == self._code:
            if self._state == "Locked":
                self.setState("Open-CodeSet")
            elif self._state == "Closed":
                self.setState("Locked")

        elif (Chars == "") & (self._state == "Open-CodeSet"):
            self.setState("Closed")

        elif self._valid(Chars):
            if self._state == "Open-NoCode":
                self.setNewCode(Chars)
                self.setState("Open-CodeSet")
            else:
                print("Error - does not match set code")
        else:
            print("Error - Code format incorrect")

    def __str__(self):
        return 'Code: {0}, State: {1}'.format(self._code, self._state)

# (b) (vii)
def main():
    ThisSafe = SafetyDepositBox()

    while True:
        ThisSafe.stateChange()

if __name__ == '__main__':
    main()

