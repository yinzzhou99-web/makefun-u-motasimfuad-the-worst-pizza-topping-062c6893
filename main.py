"""Entry point for the worst-pizza-topping bounty.

Writes the single winning one-liner to $OUTPUT_DIR/entry.txt.
Stdlib only, deterministic, no network access.
"""

import os
import stat


def _compose_line() -> str:
    """Assemble the final one-liner from its four beats.

    The topping name leads, the pizza's confidence is the setup,
    and the noise complaint is the punchline.
    """
    opener = "Introducing the"
    topping = "Pickle-Brussels-Sprout Surprise"
    boast = "a pizza so confident in its own crunch"
    punchline = "it filed a noise complaint against itself"
    return f"{opener} {topping}, {boast}, {punchline}."


def _write_entry() -> None:
    """Create the output directory if needed and write entry.txt.

    Only entry.txt itself is ever touched: anything else already
    sitting in the output directory is left exactly as it is.
    """
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    payload = _compose_line().encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(payload)
    os.chmod(
        target,
        stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH,
    )


if __name__ == "__main__":
    _write_entry()
