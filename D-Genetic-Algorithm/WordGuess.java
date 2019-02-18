import java.util.*;
import java.lang.*;


public class WordGuess extends GA
{
 private String WG_target;

 public WordGuess(String fileName, String target)
    {
        super(fileName,target);
        WG_target = new String(target);
        GA_numGenes = WG_target.length();
            if (WG_target.length() != GA_numGenes)
            {
                System.out.println("Error: Target size differs from number of genes");
                DisplayParams();
                System.exit(1);
            }

        InitPop();
    }


 public void InitPop()
    {
        super.InitPop();
        ComputeCost();
        SortPop();
        TidyUp();
    }

 public void DisplayParams()
    {
        System.out.print("Target: ");
        System.out.println(WG_target);
        super.DisplayParams();
    }

 protected void ComputeCost()
    {
        for (int i = 0; i < GA_pop.size(); i++)
        {
            int cost = 0;
            Chromosome chrom = GA_pop.remove(i);
            for (int j = 0; j < GA_numGenes; j++)
                if (chrom.GetGene(j) != WG_target.charAt(j))
                    cost++;
            chrom.SetCost(cost);
            GA_pop.add(i,chrom);
        }
    }
 //in earlier versions (as on ada) Evolve() from GA is here
 }

