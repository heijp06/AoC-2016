class Computer:
    def __init__(self, code: list[str]) -> None:
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.pc = 0
        self.code = code
    
    def run(self) -> None:
        while self.pc < len(self.code):
            instruction, *args = self.code[self.pc].split()
            self.pc += 1
            func = getattr(self, instruction)
            func(*args)

    def cpy(self, x: str, y: str) -> None:
        value = self.get_value(x)
        self.set_value(y, value)

    def inc(self, x: str) -> None:
        self.set_value(x, self.get_value(x) + 1)

    def dec(self, x: str) -> None:
        self.set_value(x, self.get_value(x) - 1)

    def jnz(self, x: str, y: str) -> None:
        if self.get_value(x):
            self.pc += self.get_value(y) - 1

    def get_value(self, x: str) -> int:
        return getattr(self, x) if x in "abcd" else int(x)
    
    def set_value(self, x: str, value: int) -> None:
        setattr(self, x, value)