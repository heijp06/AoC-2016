class Bot:
    def __init__(self, number: int) -> None:
        self.number = number
        self.values = []
    
    def __repr__(self) -> str:
        return f"BOT{self.number:03}-{self.low}-{self.high}"

    def set_value(self, value: int) -> None:
        self.values.append(value)

    @property
    def low(self) -> int | None:
        return min(self.values) if self.ready else None

    @property
    def high(self) -> int | None:
        return max(self.values) if self.ready else None

    @property
    def ready(self) -> bool:
        return len(self.values) == 2
