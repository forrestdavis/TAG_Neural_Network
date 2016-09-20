#!/usr/bin/perl

my $ref = pop;
my $hyp = pop;

my $TAGGING_ACCURACY_PER_CATEGORY = 0;
my $TAGGING_CONFUSION_MATRIX = 0;
my $TAGGING_ERRORS_PER_CATEGORY = 0;

my $PARSING_ACCURACY_PER_FUNCTION = 0;
my $LABELING_CONFUSION_MATRIX = 0;
my $ATTACHEMENT_CONFUSION_MATRIX = 0;

sub is_punctuation_ptb{
    my $pos = shift(@_);

    if($pos eq "``"){return 1;}
    if($pos eq ","){return 1;}
    if($pos eq ":"){return 1;}
    if($pos eq "."){return 1;}
    if($pos eq "''"){return 1;}
    if($pos eq "-LRB-"){return 1;}
    if($pos eq "-RRB-"){return 1;}
    return 0;
}
sub is_punctuation_ftb{
    my $pos = shift(@_);

    if($pos eq "PONCT"){return 1;}
    return 0;
}


$arg = shift;
while($arg){
    if($arg eq "-g"){$ref = shift;}
    elsif($arg eq "-s"){$hyp = shift;}
    elsif($arg eq "-tac"){$TAGGING_ACCURACY_PER_CATEGORY = 1;}
    elsif($arg eq "-tcm"){$TAGGING_CONFUSION_MATRIX = 1;}
    elsif($arg eq "-tec"){$TAGGING_ERRORS_PER_CATEGORY = 1;}
    elsif($arg eq "-paf"){$PARSING_ACCURACY_PER_FUNCTION = 1;}
    elsif($arg eq "-lcm"){$LABELING_CONFUSION_MATRIX = 1;}
    elsif($arg eq "-acm"){$ATTACHEMENT_CONFUSION_MATRIX = 1;}
    elsif($arg eq "-all"){
	$TAGGING_ACCURACY_PER_CATEGORY = 1;
	$TAGGING_CONFUSION_MATRIX = 1;
	$TAGGING_ERRORS_PER_CATEGORY = 1;
	$PARSING_ACCURACY_PER_FUNCTION = 1;
	$LABELING_CONFUSION_MATRIX = 1;
	$ATTACHEMENT_CONFUSION_MATRIX = 1;
    }
    elsif($arg eq "-h"){
	print "usage eval07.pl OPTIONS -g <gold file> -s <system output>\n";
	print "OPTIONS :\n";
	print "\t-tac tagging accuracy per category\n";
	print "\t-tcm tagging confusion matrix\n";
	print "\t-tec tagging errors per category\n";
	print "\t-paf parsing accuracy per function\n";
	print "\t-lcm labeling confusion matrix\n";
	print "\t-acm attachment confusion matrix\n";
	print "\t-all all options\n";
	exit;
}
$arg = shift;
}

#print "ref = $ref hyp = $hyp\n";

open REF, $ref or die "cannot open file $ref";
open HYP, $hyp or die "cannot open file $hyp";


my $line_nb;
my $word_nb;
my $correct_pos_nb;
my $correct_gov_nb;
my $correct_gov_fct_nb;

while(<REF>){
    $line_nb++;
    $seg_ref = 0;
    $seg_hyp = 0;
    if($_ eq "\n"){$_ = <REF>; $seg_ref = 1;}
#    print;
    ($ref_index, $ref_form, $ref_lemma, $ref_cpos, $ref_pos, $ref_morpho, $ref_gov, $ref_fct) = split;
    $_ = <HYP>;
    if($_ eq "\n"){$_ = <HYP>; $seg_hyp = 1;}
#    print;
    if($seg_ref && $seg_hyp){$r1h1++;}
    if($seg_ref && !$seg_hyp){
	$r1h0++;
#	print ">> r1h0\n";
    }
    if(!$seg_ref && $seg_hyp){
	$r0h1++; 
#	print ">> r0h1\n";
    }
    if(!$seg_ref && !$seg_hyp){$r0h0++;}
    ($hyp_index, $hyp_form, $hyp_lemma, $hyp_cpos, $hyp_pos, $hyp_morpho, $hyp_gov, $hyp_fct) = split;
#    if(($ref_index) && (!is_punctuation_ptb($ref_cpos))){
    if(($ref_index) && (!is_punctuation_ftb($ref_cpos))){
#    if($ref_index){

#	print "ref = $ref_form hyp = $hyp_form\n";

	if($ref_form ne $hyp_form){die "mismatch line $line_nb\n";}
	$word_nb++;
	$pos_nb{$ref_pos}++;
	$fct_nb{$ref_fct}++;
	if($ref_pos eq $hyp_pos){
	    $correct_pos_total_nb++; 
	    $correct_pos_nb{$ref_pos}++;
	}
	else{
	    $false_pos_form{$ref_pos}{$ref_form}++;
	    $pos_confusion_matrix{$ref_pos}{$hyp_pos}++;
	}
	
	if($ref_gov == 0){$ref_dep_length = 0;}
	else{$ref_dep_length = $ref_index - $ref_gov;}

	if($hyp_gov == 0){$hyp_dep_length = 0;}
	else{$hyp_dep_length = $hyp_index - $hyp_gov;}


#	if($ref_gov eq $hyp_gov){
	if($ref_dep_length eq $hyp_dep_length){
	    $correct_gov_nb++;
	    if($ref_fct eq $hyp_fct){
		$correct_gov_fct_total_nb++; 
		$correct_gov_fct_nb{$ref_fct}++;
	    }
	    else{
		$labeling_confusion_matrix{$ref_fct}{$hyp_fct}++;
	    }
	}
	else{
	    $attachement_confusion_matrix{$ref_fct}{$hyp_fct}++;
	}
	$ref_index = "";
    }
}

close REF;
close HYP;

my $seg_recall = $r1h1 / ($r1h1 + $r1h0) * 100;
my $seg_precision = $r1h1 / ($r0h1 + $r1h1) * 100;


my $pos_acc = $correct_pos_total_nb / $word_nb * 100;
my $las = $correct_gov_fct_total_nb / $word_nb * 100;
my $uas = $correct_gov_nb / $word_nb  * 100 ;

#printf("%.2f %.2f\n", $las, $uas);
printf("seg rec = %.2f seg prec = %.2f pos acc = %.2f las = %.2f uas = %.2f\n", $seg_recall, $seg_precision, $pos_acc, $las, $uas);

#printf("r1h1 = %d r1h0 = %d r0h1 = %d\n", $r1h1, $r1h0, $r0h1);


if($TAGGING_ACCURACY_PER_CATEGORY){
    print "\n\n--------------------------------------------------------------------------------------\n";
    printf "TAGGING ACCURACY PER CATEGORY\n";
    printf "CAT\tFREQ\tACC\tIMPACT\n";
    foreach $pos (keys %correct_pos_nb){
	$acc = $correct_pos_nb{$pos} / $pos_nb{$pos}; 
	$freq = $pos_nb{$pos} / $word_nb;
	$impact =  ($pos_nb{$pos} - $correct_pos_nb{$pos}) / ($word_nb - $correct_pos_total_nb);
	printf("%s\t%6.2f\t%6.2f\t%6.2f\n", $pos, $freq*100, $acc*100, $impact*100);
    } 
}

if($TAGGING_CONFUSION_MATRIX){
    print "\n\n--------------------------------------------------------------------------------------\n";
    print "TAGGING CONFUSION MATRIX\n";
    foreach $ref_pos (keys %pos_confusion_matrix){
	$pos_error_nb = $pos_nb{$ref_pos} - $correct_pos_nb{$ref_pos};
	print "$ref_pos ($pos_error_nb) :";
	    foreach $hyp_pos (keys %{$pos_confusion_matrix{$ref_pos}}){
	    print "\t$hyp_pos ($pos_confusion_matrix{$ref_pos}{$hyp_pos})";
	}
	print "\n";
    }
}


if($TAGGING_ERRORS_PER_CATEGORY){
    print "\n\n--------------------------------------------------------------------------------------\n";
    print "TAGGING ERRORS PER CATEGORY\n";
    foreach $pos (keys %false_pos_form){
	print "\n$pos\n";
	foreach $form (keys %{$false_pos_form{$pos}}){
	    print "\t$form $false_pos_form{$pos}{$form}\n";
	}
    }
}

if($PARSING_ACCURACY_PER_FUNCTION){
    print "\n\n--------------------------------------------------------------------------------------\n";
    printf "LABELED ATTACHMENT SCORE PER LABEL\n";
    printf "LABEL       FREQ           ACC   IMPACT\n";
    foreach $fct (keys %correct_gov_fct_nb){
	$acc = $correct_gov_fct_nb{$fct} / $fct_nb{$fct}; 
	$freq = $fct_nb{$fct}/$word_nb;
	$impact =  ($fct_nb{$fct} - $correct_gov_fct_nb{$fct}) / ($word_nb - $correct_gov_fct_total_nb++);
	printf("%-10s%6.2f\t%6.2f\t%6.2f\n", $fct, $freq*100, $acc*100, $impact*100);
    }
}


if($ATTACHEMENT_CONFUSION_MATRIX){
    print "\n\n--------------------------------------------------------------------------------------\n";
    printf "ATTACHEMENT CONFUSION MATRIX\n";
    foreach $ref_fct (keys %attachement_confusion_matrix){
	$attachement_error_nb = $fct_nb{$ref_fct} - $correct_gov_fct_nb{$ref_fct};
	print "$ref_fct ($attachement_error_nb) :";
	foreach $hyp_fct (keys %{$attachement_confusion_matrix{$ref_fct}}){
	    print "\t$hyp_fct ($attachement_confusion_matrix{$ref_fct}{$hyp_fct})";
	}
	print "\n";
    }

}

if($LABELING_CONFUSION_MATRIX){
    print "\n\n--------------------------------------------------------------------------------------\n";
    printf "LABELING CONFUSION MATRIX\n";
    foreach $ref_fct (keys %labeling_confusion_matrix){
	$fct_error_nb = $fct_nb{$ref_fct} - $correct_gov_fct_nb{$ref_fct};
	print "$ref_fct ($fct_error_nb) :";
	foreach $hyp_fct (keys %{$labeling_confusion_matrix{$ref_fct}}){
	    print "\t$hyp_fct ($labeling_confusion_matrix{$ref_fct}{$hyp_fct})";
	}
	print "\n";
    }

}
