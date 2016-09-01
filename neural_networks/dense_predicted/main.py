import argparse
import sys
import keras_model as km

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="%(prog)s [options]",
            add_help=False)

    ############################################################
    #Flags for options
    ############################################################
    req = parser.add_argument_group("Options", 
            "Arguments -D and -M are required")
    req.add_argument("-nv", "--no-verbose", 
            help="deactivate verbose mode", action="store_false")
    req.add_argument("-h", "--help", action="help",
            help="display this message")
    req.add_argument("-D", "--data_path", metavar='', 
            help="path to data directory", required=True)
    req.add_argument("-M", "--mode", metavar='', 
            help="TRAIN|TEST|PREDICT|GRAPH", required=True, 
            choices=["TRAIN", "TEST", "PREDICT", "GRAPH"])
    req.add_argument("-T", "--trained_model", metavar='',
    help=("Specifiy the file name for saving/loading the train model, "
          +"no extension. The files are "
          +"located in saved_models "
          +"{for all modes} (default: trained_model)"))
    req.add_argument("-L", "--load", action="store_true",
            help=("Load trained model {for TEST, PREDICT, and GRAPH} "
    +"(default: False, will train model"))

    ############################################################
    #Flags for train
    ############################################################
    train = parser.add_argument_group("IN TRAIN MODE",
            "Argument -T, listed above, is an option as well")
    train.add_argument("-S", "--save", action="store_true", 
            help="Save trained model (default: False)")
    train.add_argument("-F", "--feats", metavar='',
            help=("List features for training (default: all features "
                +"available in data directory)"))

    ############################################################
    #Flags for test
    ############################################################
    test = parser.add_argument_group("IN TEST MODE",
            "Optional arguments are -L and -T, listed in Options."
            +" If a model is not loaded, a model will be trained and "
            +" the flags for TRAIN mode can also be specified")

    ############################################################
    #Flags for predict
    ############################################################
    predict = parser.add_argument_group("IN PREDICT MODE", 
            "Argument -L, listed above is an option as well")
    predict.add_argument("-f", "--fann", metavar='', help="fann file")
    predict.add_argument("-FM", "--feat_model", metavar='',
            help="feature model file name")

    ############################################################
    #Flags for graph
    ############################################################
    graph = parser.add_argument_group("IN GRAPH MODE", 
            "Argument -L, listed above is an option as well."
            +" If a model is not loaded, a model will be trained and "
            +" the flags for TRAIN mode can also be specified")
    graph.add_argument("-g", "--graph", metavar='', help="graph file name")

    args = parser.parse_args()

    #model = KerasModel("data_1000")
    #model.train()
    #model.save()
    #model.load()
    #model.evaluate()
    #print model.predict()
    #model.graph()
