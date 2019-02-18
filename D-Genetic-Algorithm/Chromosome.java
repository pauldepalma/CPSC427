import java.lang.*;
import java.util.*;

public class Chromosome
{
 private   int      CH_numGenes;
 protected int      CH_cost;
 private   char[]   CH_gene;

 public Chromosome(int genesIn)
    {
        CH_numGenes = genesIn;
        CH_gene     = new char[CH_numGenes];
    }

 public int GetNumGenes()
    {
        return CH_numGenes;
    }

 public void SetCost(int cost)
    {
        CH_cost = cost;
    }

 public int GetCost()
    {
        return CH_cost;
    }
 
 public void SetGene(int index, char value)
    {
        CH_gene[index] = value;
    }

 public char GetGene(int index)
    {
        return CH_gene[index];
    }

 public void DisplayGenes()
    {
        for (int i = 0; i < CH_numGenes; i++)
            System.out.print(GetGene(i));
    }

 public boolean Equals(String target)
    {
        for (int i = 0; i < CH_numGenes; i++)
            if (CH_gene[i] != target.charAt(i))
                return false;
        return true;
    }

}

