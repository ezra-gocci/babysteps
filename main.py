import pytest


def main():
    print("We run all the active tests here")
    pytest.main(["-v", "./tests"])


if __name__ == "__main__":
    main()

