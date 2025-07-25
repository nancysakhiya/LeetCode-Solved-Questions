from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.gates = [Lock(), Lock(), Lock()]
        self.gates[0].acquire()
        self.gates[1].acquire()
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.gates[2].acquire()
            printNumber(0)
            self.ct += 1
            self.gates[self.ct % 2].release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.gates[0].acquire()
            printNumber(self.ct)
            self.gates[2].release()

        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n+1) // 2):
            self.gates[1].acquire()
            printNumber(self.ct)
            self.gates[2].release()
        