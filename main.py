
from services.cataas import download_cats


def main():
    download_cats(5)

if __name__ == "__main__":
    main()
# when every we call the project in the terminal
# these code will turn first file name into __main__
# when we have several file.py we can see the main file which need to process first.
# place this set of code in the main.py