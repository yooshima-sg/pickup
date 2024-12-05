import sys
import random
import logging

from collections.abc import Sequence


def input_data() -> Sequence[str]:
    data = sys.stdin.read()
    lines = filter(lambda y: y and y != "", map(lambda x: x.strip(), data.split("\n")))
    return list(lines)


def main() -> int:
    source_datas = input_data()
    if len(source_datas) < 2:
        logging.error("This program is required input data that is more than 2 lines.")
        return 1

    print("------------ PICKUP ------------")
    print(random.choice(source_datas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
