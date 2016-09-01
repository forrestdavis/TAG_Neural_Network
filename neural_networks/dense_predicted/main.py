import argparse
import sys
import keras_model as km

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="%(prog)s [options]",
            description=("main function for working with a "
               +"keras model. You can list more than one mode in any order "
               +"i.e. TEST TRAIN GRAPH. The order of operatations under "
               +"the hood is TRAIN TEST PREDICT GRAPH. TEST/PREDICT without "
               +"-L to load a pre-trained model, or adding TRAIN to -M "
               +"will still cause TRAIN to be called, so TRAIN specific "
               +"flags can be added to a TEST/PREDICT call")
                ,add_help=False)

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
    req.add_argument("-M", "--mode", metavar='', nargs='+',
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
    train.add_argument("-F", "--feats", metavar='', nargs='+',
            help=("List features for training (default: all features "
                +"available in data directory)"))

    ############################################################
    #Flags for test
    ############################################################
    test = parser.add_argument_group("IN TEST MODE",
            "Optional arguments are -L/--load and -T/--trained_model, "
            +"listed in Options."
            +" If a model is not loaded, a model will be trained and "
            +" the flags for TRAIN mode can also be specified")

    ############################################################
    #Flags for predict
    ############################################################
    predict = parser.add_argument_group("IN PREDICT MODE", 
            "Argument -L/--load, listed above is an option as well")
    predict.add_argument("-f", "--fann", metavar='', help="fann file")
    predict.add_argument("-FM", "--feat_model", metavar='',
            help="feature model file name")

    ############################################################
    #Flags for graph
    ############################################################
    graph = parser.add_argument_group("IN GRAPH MODE", 
            "Argument -L/--load, listed above is an option as well."
            +" If a model is not loaded, a model will be trained and "
            +" the flags for TRAIN mode can also be specified")
    graph.add_argument("-g", "--graph", metavar='', help="graph file name")

    args = parser.parse_args()

    model = km.KerasModel(args.data_path)
    trained=False
    #TRAIN
    if "TRAIN" in args.mode:
        model.train(args.feats)
        trained=True
    
    #SAVE/LOAD
    if args.trained_model:
        if not args.save and not args.load:
            sys.stderr.write("To use -T/--train_model you must either specifiy "
                    +"-L/--load or -S/--save\n")
            sys.exit(1)
    if args.save:
        model.save(args.trained_model)
    if args.load:
        model.load(args.trained_model)

    #TEST
    if "TEST" in args.mode:
        if not args.load and not trained:
            model.train(args.feats)
            trained=True
        model.evaluate()
    
    #Predict
    if "PREDICT" in args.mode:
        if not args.load and not trained:
            model.train(args.feats)
            trained=True
        if not args.feat_model:
            sys.stderr.write(
                    "To PREDICT -FM/--feat_model must be specified\n")
            sys.exit(1)
        if not args.fann:
            sys.stderr.write(
                    "To PREDICT -f/--fann must be specified\n")
            sys.exit(1)
        print model.predict(args.feat_model, args.fann)
    
    #Graph
    if "GRAPH" in args.mode:
        if not args.load and not trained:
            model.train(args.feats)
            trained=True
        model.graph(args.graph)
