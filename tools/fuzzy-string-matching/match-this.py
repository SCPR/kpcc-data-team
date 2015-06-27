# install requirements.txt dependencies

import logging
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

def compare_strings():
    test = fuzz.ratio("Canoga Park El", "Canoga Park")
    logging.debug(test)

if __name__ == "__main__":
    compare_strings()
