#!/usr/bin/perl
#
#

while(<>){
    if(/...EOS../){
        <>;
        print "\n";
    }
    else{
        print @lines;
    }
}
