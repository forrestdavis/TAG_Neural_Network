#include<stdio.h>
#include<string.h>

int main(){

    char command[100];
    //strcpy(command, "python model_predictor.py output.txt mvt.txt trained_model.json trained_model_weights.h5");
    //system(command);
    FILE *fp;
    int mvt;
    int mvt_code;
    char buf[10];
    fp = fopen("mvt.txt", "r");
    fgets(buf, sizeof(buf), fp);
    mvt_code = atoi(buf);
    printf("%s\n", buf);
    printf("%d\n", mvt_code);
    fclose(fp);

    return 0;
}
