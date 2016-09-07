/******************************************************************
 * This function takes as input a fann file, the feature model for 
 * that fann file, a filename for saving the input data, a filename
 * for saving the output data and a file name for io info which is
 * used by load_fann_bin.py to load the binary file to a numpy array
 *
 * Forrest Davis
 * August 29, 2016
 * 
 *****************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* TODO:
 * Write now I just have a fann to binary function for a fann file
 * with one feature with the exact order s0 s1 s2 s3 b0 b1 b2 b3.
 * Need to write a general fann to binary for multiple features
 * and for a different order of stack and buffer.
 */

void transformFANN_Optimized(char *feat, const char *fann_name, 
        const char *saved_input_filename, 
        const char *saved_output_filename,
        const char *io_info_filename);

struct feat{
    char *feat_type;
    int locations[8];
};

int main(int argc, char **argv){
                 
    const char *fann_name = "small_example.fann";
    const char *fm_name = "example.fm";
    const char *saved_input_filename = "example_input.bin";
    const char *saved_output_filename = "example_output.bin";
    const char *io_info_filename = "example_io.txt";

    const char comment = '#';
    //If this is the exact order of stack and buffer elements
    //used for the same feature then the transformFANN_Optimized 
    //function to create a binary file can be used
    char *s_b_order[] = {"s0","s1","s2",
        "s3","b0","b1","b2","b3"};
    char buffer[100];

    //Open feature model file 
    FILE *fm = fopen(fm_name, "r");
    if(fm == NULL){
        fprintf(stderr, "Unable to open %s file.\n", fm_name);
        exit(1);
    }

    int i = 0;
    int isOptimized = 1;
    char *feat = (char *) malloc(2*sizeof(char));
    //Read each line of the fm file
    while(fgets(buffer, sizeof(buffer), fm)!=NULL){
        //If first character is #, ignore
        if(buffer[0] != comment){
            //Get feature location information i.e s0
            //Get feature, Assumes feature is one character
            printf("%s\n", buffer);
            feat[0] = buffer[2];
            feat[1] = '\0';
            //If each of the optimized stack/buffer order 
            //is not in order in the fm file than the Optimized
            //function cannot be used
            char *tmp = s_b_order[i++];
            if(tmp[0]!=buffer[0] && tmp[1]!=buffer[1]){
                isOptimized = 0;
            }
        }
    }

    if(isOptimized){
        transformFANN_Optimized(feat, fann_name, 
                saved_input_filename, saved_output_filename,
                io_info_filename);
    }
    free(feat);
    fclose(fm);
    return 0;
}

//This is the fastest way I could come up with to transform 
//the fann file into binary.
//It reads the one hot encodings from the fann file and if the 
//data are input it writes it to the saved_input file. If the data
//are output it writes it to the saved_output file. In the fann file
//format the first line is comprised of three numbers. The first
//is number of input/output pairs. The second is the dimensions of the 
//input. The third is the dimension of the output. This line is read first
//and saved to the io_info file for use by the python program that loads
//the binary file as a numpy array.
//Furthermore, I am using char for the data to decrease the numpy array
//size later on. Unless the data is form, then I have to use double to 
//keep float values
void transformFANN_Optimized(char *feat, const char *fann_name, 
        const char *saved_input_filename, 
        const char *saved_output_filename,
        const char *io_info_filename){
    FILE *fann = fopen(fann_name, "r");

    //Open files
    if(fann == NULL){
        fprintf(stderr, "Unable to open %s file.\n", fann_name);
        exit(1);
    }
    FILE *saved_output = fopen(saved_output_filename, "wb");
    if(saved_output == NULL){
        fprintf(stderr, "Unable to open %s file.\n", saved_output_filename);
        exit(1);
    }
    FILE *saved_input = fopen(saved_input_filename, "wb");
    if(saved_input == NULL){
        fprintf(stderr, "Unable to open %s file.\n", saved_input_filename);
        exit(1);
    }
    FILE *io_info_file = fopen(io_info_filename, "w");
    if(io_info_file == NULL){
        fprintf(stderr, "Unable to open %s file.\n", io_info_filename);
        exit(1);
    }
    
    char buffer[8000];
    int isOutput = 0;
    int numNew = 0;
    int i;
    int j;

    printf("Transforming fann file to binary...\n");
    
    //Get first line of fann file and append the feature
    //to the beginning of the line. Write line to io file
    //Follows fann file format that first line will be
    //three numbers: number of examples, input size, output size
    //the first char * in info is reserved for the feature to be
    //found in fm file
    //Only does this for any features that are not form. For form
    //I need the input dimensions
    fgets(buffer, sizeof(buffer), fann);
    char tmp[100];
    memset(tmp, '\0', sizeof(tmp));
    strcat(tmp, feat);
    strcat(tmp, "  ");
    strcat(tmp, buffer);

    fputs(tmp, io_info_file);

    int *input_dim; 
    input_dim = (int *) malloc(sizeof(input_dim));
    memset(input_dim, 0, sizeof(*input_dim));
    //Get input dimension information for form
    if(feat[0] == 'f'){
        int k = 0;
        char *token;
        token = strtok(buffer, " ");
        while(token != NULL){
            if(k==1)
                *input_dim = atoi(token);
            token = strtok(NULL, " ");
            k++;
        }
    }

    //Read the rest of the lines
    //The format of the fann file is one blank line between 
    //input and output and two between the output and the new 
    //input/output pair. Thus if only one blank line is found the 
    //following one hot encoding is written to the saved output
    //file. Then the next one hot encodings are input so they are
    //written to the saved input file
    //If the data is from the form feature, however you have to read
    //the data as float.
    while(fgets(buffer, sizeof(buffer), fann)!=NULL){
        if(buffer[0] == 10){
            numNew++;
        }
        else{
            if(numNew == 1)
                isOutput = 1;
            if(isOutput){
                j = 0;
                //Get size of line. Due to format of fann files
                //I know each int is seperated by a space so the 
                //actually length of the one hot encoding is half
                int len = strlen(buffer);
                char value[len/2];
                for(i=0; i<len; i++){
                    char tmp;
                    //First append all data from line to array
                    //this is faster than writing each value to file
                    if((tmp=(buffer[i++]-48))== 0 || tmp == 1)
                        value[j++] = tmp;
                    
                }
                fwrite(value, sizeof(value), 1, saved_output);
                isOutput = 0;
            }
            else{
                if(feat[0]!='f'){
                    j = 0;
                    //Get size of line. Due to format of fann files
                    //I know each int is seperated by a space so the 
                    //actually length of the one hot encoding is half
                    int len = strlen(buffer);
                    char value[len/2];
                    memset(value, 0, sizeof(value));
                    for(i=0; i<len; i++){
                        char tmp;
                        //First append all data from line to array
                        //this is faster than writing each value to file
                        //i++ skips over non-data elements
                        if((tmp=(buffer[i++]-48))== 0 || tmp == 1)
                            value[j++] = tmp;
                        
                    }
                    fwrite(value, sizeof(value), 1, saved_input);
                }
                //Cast data into double and write to files
                else if(feat[0]=='f'){
                    j = 0;
                    char *data;
                    //Each line is an 8th of the total input dim
                    double value[*input_dim/8];
                    memset(value, 0, sizeof(value));
                    data = strtok(buffer, " ");
                    while(data != NULL){
                        double tmp = atof(data);
                        data = strtok(NULL, " ");
                        value[j++] = tmp;
                    }
                    fwrite(value, sizeof(value), 1, saved_input);
                }
            }
            numNew = 0;
        }
    }

    //Close files
    fclose(fann);
    fclose(saved_output);
    fclose(saved_input);
    fclose(io_info_file);
}
