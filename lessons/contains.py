"""Example of a function that processes a lsit."""


def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return true if needle is found in haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False


# Python Idiom for starting the main function
if __name__ == "__main__":
    main()