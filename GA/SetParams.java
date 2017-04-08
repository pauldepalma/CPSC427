/*  SetParams creates the parameter file. args[0] is its name.
    Here is a reasonable set of command line arguments:
    java SetParams params.dat 128 64 5 .1 1000
    where   128  = the size of the initial population
            64   = the size of the working population
            5    = the number of genes.  In this case, the number of letters in the word to be guessed
            .1   = the mutation factor
            1000 = the number of generations; stop after this number of generations if the word has 
                    not been guessed.
*/

import java.lang.*;

public class SetParams
{
public static void main(String args[])
    {
        int     numChromesI = Integer.parseInt(args[1]);
        int     numChromes   = Integer.parseInt(args[2]);
        int     numGenes    = Integer.parseInt(args[3]);
        double  mutFact     = Double.parseDouble(args[4]);
        int     numIters    = Integer.parseInt(args[5]);
        GetParams GP        = new GetParams(args[0],numChromesI,numChromes,numGenes,mutFact,numIters);
        //args[0] is the name of the parameter file
    }
}

