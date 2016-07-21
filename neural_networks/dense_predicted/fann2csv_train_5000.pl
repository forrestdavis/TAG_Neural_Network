#!/usr/bin/perl
#
#
my $number = 0;
my $lenInput;
my $lenOutput;
my $x_tmp;
my @X = qw();
my @Y = qw();

#open new files to write
open(INPUT, ">X_train_5000.csv");
open(OUTPUT, ">Y_train_5000.csv");

while(<>){
    if(/...EOS../){
        <>;
        print "\n";
    }
    else{
        @tab = split;
        $lineLength = scalar(@tab);
        if($number == 0){
            $lenInput = @tab[1];
            $lenOutput = @tab[2];
            print "$lenInput $lenOutput \n";
        } 
        else{
            if(($lineLength!=$lenOutput) && ($lineLength!=0)){
                foreach $elt (@tab){
                    if(length $x_tmp == 0){
                        $x_tmp = "$elt";
                    }
                    else{
                        $x_tmp = "$x_tmp, $elt";
                    }
                }
            }
            if($lineLength == $lenOutput){
                $y_tmp;
                foreach $elt (@tab){
                    if(length $y_tmp == 0){
                        $y_tmp = "$elt";
                    }
                    else{
                        $y_tmp = "$y_tmp, $elt";
                    }
                }
                #print INPUT "$x_tmp\n";
                #print OUTPUT "$y_tmp\n";
                push (@X, "$x_tmp\n");
                push (@Y, "$y_tmp\n");
                $x_tmp = "";
                $y_tmp = "";
            }
        }
        $number++;

    }
}
print INPUT "@X";
print OUTPUT "@Y";
close(INPUT);
close(OUTPUT);
