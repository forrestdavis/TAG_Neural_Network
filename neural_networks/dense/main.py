import argparse
import sys
import keras_model as km

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="%(prog)s [options]",
            description=("main function for working with a "
               +"keras model. You can list more than one mode in any order "
               +"i.e. TEST TRAIN GRAPH. The order of operatations under "
               +"the hood is TRAIN OPTIMIZE TEST PREDICT GRAPH. "
               +"TEST/PREDICT/GRAPH "
               +"without -L to load a pre-trained model, or adding TRAIN to "
               +"-M will still cause TRAIN to be called, so TRAIN specific "
               +"flags can be added to a TEST/PREDICT/GRAPH call")
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
            help="TRAIN|TEST|PREDICT|GRAPH|OPTIMIZE", required=True, 
            choices=["TRAIN", "TEST", "PREDICT", "GRAPH", "OPTIMIZE"])
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
    train.add_argument("-l", "--nb_layers", metavar='', type=int, 
            help="Set number of layers in keras model (default: TBD)")
    train.add_argument("-A", "--activation", metavar='', nargs='+',
            help="Set activation function for layers. If you desire "
            +"different activation functions per layer list activation "
            +"functions in order")
    train.add_argument("-N", "--nodes", metavar='', nargs='+', type=int,
            help="Set number of nodes for layers. If you desire "
            +"different node sizes per layer list node sizes in order.")
    train.add_argument("-mL", "--nb_merge_layers", metavar='', type=int, 
    help="Set number of layers in keras model after merge (default: TBD)")
    train.add_argument("-mA", "--merge_activation", metavar='', nargs='+',
        help="Set activation function for layers after merge. If you desire "
            +"different activation functions per layer list activation "
            +"functions in order")
    train.add_argument("-mN", "--merge_nodes", metavar='', nargs='+', type=int,
            help="Set number of nodes for layers after merge. If you desire "
            +"different node sizes per layer list node sizes in order.")
    train.add_argument("-nE", "--nb_epoch", metavar='', type=int, 
            help=("Set number of epochs for training the model"
                +"(default: 50)"))
    train.add_argument("-nS", "--no_stop", action="store_false", 
            help="Stop early stopping on the model")


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

    ############################################################
    #Flags for optimize
    ############################################################
    optimize = parser.add_argument_group("IN OPTIMIZE MODE",
            "This mode is for the automation of the training "
            +"process to produce an optimized model. Currently "
            +"only the number of nodes before the merge process"
            +" is optimized so the flags -l/--nb_layers and "
            +"-mL/--nb_merge_layers can be used to set those "
            +"parameters. As well as -F/--feats, "
            +"-T/--trained_model and -S/--save.")

    args = parser.parse_args()

    ############################################################
    # CREATE CLASS INSTANCE
    ############################################################
    model = km.KerasModel(args.data_path, args.no_verbose)
    trained=False

    ############################################################
    # TRAIN
    ############################################################
    if "TRAIN" in args.mode:
        if args.trained_model:
            if not args.save:
                sys.stderr.write(
                "To use -T/--train_model you must either specifiy "
                        +"-L/--load or -S/--save\n")
                sys.exit(1)

        model.train(args.feats, args.nb_layers, args.activation,
                args.nodes, args.nb_merge_layers, 
                args.merge_activation, args.merge_nodes, 
                args.nb_epoch, args.no_stop)
        if args.save:
            model.save(args.trained_model)
        trained=True

    ############################################################
    # OPTIMIZE
    ############################################################
    if "OPTIMIZE" in args.mode:
        if args.trained_model:
            if not args.save:
                sys.stderr.write(
                "To use -T/--train_model you must specifiy "
                        +"-S/--save\n")
                sys.exit(1)

        model.optimize(args.feats, args.nb_layers, 
                args.nb_merge_layers)
        if args.save:
            model.save(args.trained_model)
        trained=True

    ############################################################
    # TEST
    ############################################################
    if "TEST" in args.mode:
        if args.trained_model:
            if not args.save and not args.load:
                sys.stderr.write(
                "To use -T/--train_model you must either specifiy "
                        +"-L/--load or -S/--save\n")
                sys.exit(1)
        if args.load:
            model.load(args.trained_model)

        if not args.load and not trained:
            model.train(args.feats, args.nb_layers, args.activation,
                    args.nodes, args.nb_merge_layers, 
                    args.merge_activation, args.merge_nodes, 
                    args.nb_epoch, args.no_stop)
            trained=True
            if args.save:
                model.save(args.trained_model)
        model.evaluate()
    
    ############################################################
    # PREDICT
    ############################################################
    if "PREDICT" in args.mode:
        if not args.feat_model:
            sys.stderr.write(
                    "To PREDICT -FM/--feat_model must be specified\n")
            sys.exit(1) 
        if not args.fann:
            sys.stderr.write(
                    "To PREDICT -f/--fann must be specified\n")
            sys.exit(1)

        if args.trained_model:
            if not args.save and not args.load:
                sys.stderr.write(
                "To use -T/--train_model you must either specifiy "
                        +"-L/--load or -S/--save\n")
                sys.exit(1)
        if args.save:
            model.save(args.trained_model)
        if args.load:
            model.load(args.trained_model)

        if not args.load and not trained:
            model.train(args.feats, args.nb_layers, args.activation,
                    args.nodes, args.nb_merge_layers, 
                    args.merge_activation, args.merge_nodes, 
                    args.nb_epoch, args.no_stop)
            trained=True
        print model.predict(args.feat_model, args.fann)
    
    ############################################################
    # GRAPH
    ############################################################
    if "GRAPH" in args.mode:
        if args.trained_model:
            if not args.save and not args.load:
                sys.stderr.write(
                "To use -T/--train_model you must either specifiy "
                        +"-L/--load or -S/--save\n")
                sys.exit(1)
        if args.save:
            model.save(args.trained_model)
        if args.load:
            model.load(args.trained_model)

        if not args.load and not trained:
            model.train(args.feats, args.nb_layers, args.activation,
                    args.nodes, args.nb_merge_layers, 
                    args.merge_activation, args.merge_nodes, 
                    args.nb_epoch, args.no_stop)
        model.graph(args.graph)
