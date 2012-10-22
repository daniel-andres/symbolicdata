#!/usr/bin/perl

# replaces one or more URI with a namespace as listed in the hash below
# the ttl-file to work with is specified by command line
# the output is saved in the file with "refactor-" attached to the front

my %pairs = qw{
    sdps http://hgg.ontowiki.net/SymbolicData/CRef/INTPS/
};

if($#ARGV == -1) {
    print "Please specify file to work with."
}

open ARG, $ARGV[0] or die "File $ARGV[0] not found!";
open MYFILE, ">refactor-$ARGV[0]";

# get preamble and append new namespace definitions

while(<ARG>) {    
    if(not(substr($_, 0, 1) eq "@")) {
        while(my($namespace, $uri) = each(%pairs)) {
            print MYFILE "\@prefix $namespace: <$uri> . \n"
        }
        print MYFILE "\n";
        last;
    }
    print MYFILE $_;
}

# do a regex replace for each line

foreach $line (<ARG>) {
    while(my($namespace, $uri) = each(%pairs)) {
        $line =~ s/\<$uri([^\>\/]*)\>/$namespace:$1/g;
    }
    print MYFILE $line;
}

close MYFILE;
close ARG;
