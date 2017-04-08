
import java.util.*;
import java.lang.*;

public class Pair
{
 private ArrayList<Chromosome> PR_pop;

 public Pair(ArrayList<Chromosome> population)
    {
        PR_pop = population;
    }

 public int SimplePair() 
    {
        return (PR_pop.size() / 4);//the number of mating pairs
    }
 }

