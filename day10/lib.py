from bot import Bot
from math import prod


class BotsDict(dict):
    def __missing__(self, key: int) -> Bot:
        self[key] = Bot(key)
        return self[key]


def part1(rows: list[str], low: int = 17, high: int = 61) -> int | None:
    bots, _ = go(rows)
    for bot in bots.values():
        if bot.ready and bot.low == low and bot.high == high:
            return bot.number
    return None


def part2(rows: list[str]) -> int:
    _, outputs = go(rows)
    return prod(outputs[i] for i in range(3))


def go(rows: list[str]) -> tuple[BotsDict, dict[int, int]]:
    bots: dict[int, Bot] = BotsDict()
    outputs = {}
    while rows:
        new_rows = []
        for command in rows:
            match command.split():
                case ["value", value, "goes", "to", "bot", bot_number]:
                    bot = bots[int(bot_number)]
                    bot.set_value(int(value))
                case ["bot", bot_number, "gives", "low", "to", what1, number1, "and", "high", "to", what2, number2]:
                    source_bot = bots[int(bot_number)]
                    if not source_bot.ready:
                        new_rows.append(command)
                        continue
                    output_value(source_bot.low, what1,
                                 outputs, bots, int(number1))
                    output_value(source_bot.high, what2,
                                 outputs, bots, int(number2))
        rows = new_rows
    return bots, outputs


def output_value(value: int, what: str, outputs: dict[int, int], bots: BotsDict, number: int) -> None:
    if what == "output":
        outputs[number] = value
    else:
        bot = bots[number]
        bot.set_value(value)
