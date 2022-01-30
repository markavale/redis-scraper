# Main script for executing python code
from helpers import Converter
import time, datetime
from base import DatabaseOperations, AUTHOR

def main():
    time.sleep(2.0)
    print("Hello from Python Redis :)")



if __name__ == "__main__":
    print("Executed at", datetime.datetime.now().strftime("%Y-%m-%d at %M:%S%p"))
    print("*", "-----"*10,"*")
    t1 = time.perf_counter()

    main()

    t2 = time.perf_counter()
    print("*", "-----"*10, "*")
    print("Finished in", Converter.convert_sec_to_hr_min_sec(round(t2 - t1, 2)))