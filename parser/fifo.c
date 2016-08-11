#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main(){


    int arr[] = {2,4,6,8};
    int len = 4;

    char *filename = "fifo.tmp";

    int s_fifo = mkfifo(filename, S_IRWXU);
    if(s_fifo != 0){
        printf("mkfifo() error: %d\n", s_fifo);
        exit(1);
    }

    FILE *wfd = fopen(filename, "w");
    if(wfd<0){
        printf("failed to open fifo\n");
        exit(1);
    }

    int i, s_write;
    for(i=0; i<len; i++){
        if(s_write=fprintf(wfd, "%d ", arr[i]) < 0){
            printf("fprintf() error\n");
            break;
        }
    }
    fprintf(wfd, "\n");

    for(i=0; i<len; i++){
        if(s_write=fprintf(wfd, "%d ", arr[i]) < 0){
            printf("fprintf() error\n");
            break;
        }
    }

    fclose(wfd);
    unlink(filename);

    return 0;
}        

