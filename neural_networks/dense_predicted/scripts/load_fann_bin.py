import numpy
import sys

#Takes as input a feature, dataType, input filename,
#output filename and info filename where
#info file is in the format:
#number_of_examples    input_dimensions output_dimensions
#dataType is TRAIN or TEST
#input and output files are binary fann files
#Saves numpy arrays to X_dataType_feat.npy
#and Y_dataType.npy
def loadBin(feat, dataType, info_filename, input_filename,
        output_filename):

    info = open(info_filename, "r")
    io = info.readline().strip("\n").split()
    info.close()
    nb_examples = int(io[0])


    in_array = numpy.fromfile(input_filename, dtype=numpy.uint8)
    out_array = numpy.fromfile(output_filename, dtype=numpy.uint8)

    #Reshape into an array for every example
    mod_in = numpy.reshape(in_array, (nb_examples, -1))
    mod_out = numpy.reshape(out_array, (nb_examples, -1))

    #Save files
    numpy.save("X_"+dataType.lower()+"_"+feat+".npy", mod_in)
    numpy.save("Y_"+dataType.lower()+".npy", mod_out)

if __name__=="__main__":
    if len(sys.argv)!=6:
        sys.stderr.write("Usage: <feature_type> <TRAIN or TEST>"+
                " <io_info_filename> <input_data_filename> " +
               "<output_data_filename>\n")
        sys.exit(1)
    feat = sys.argv[1]
    dataType = sys.argv[2]
    info_filename = sys.argv[3]
    input_filename = sys.argv[4]
    output_filename = sys.argv[5]
    loadBin(feat, dataType, info_filename, input_filename, output_filename)
