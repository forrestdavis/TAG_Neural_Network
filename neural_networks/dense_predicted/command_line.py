import argparse

parser = argparse.ArgumentParser(usage="%(prog)s [options]",
        add_help=False)
req = parser.add_argument_group("Options", 
        "Besides -v and -h these arguments are required")
req.add_argument("-v", "--verbose", 
        help="activate verbose mode", action="store_true")
req.add_argument("-h", "--help", action="help",
        help="display this message")
req.add_argument("-D", "--data_path", metavar='', 
        help="path to data directory")
req.add_argument("-M", "--mode", metavar='', 
        help="TRAIN|TEST|PREDICT")



args = parser.parse_args()

