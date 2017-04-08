import java.util.*;
import java.lang.*;
import java.io.*;


public class WritePop
{
 private String  P_file;
 private String  P_tokens[];
 private int     P_numbers[];
 private File    P_outFile;
 private File    p_file;
 private FileOutputStream P_outFileStream;
 private DataOutputStream P_outDataStream;
 private int P_numFreq, P_numInFreq, P_numHiCost;

 public WritePop(String file_in, String tokens_in[],int numbers_in[])
    {
        P_file = file_in;
        P_tokens = tokens_in;
        P_numbers = numbers_in;
        
        OpenPopFile();
        WritePopFile();
        ClosePopFile();
    }

 private void OpenPopFile()
    {
        try
        {
            P_outFile = new File(P_file);
            P_outFileStream = new FileOutputStream(P_outFile);
            P_outDataStream = new DataOutputStream(P_outFileStream);
        }
        catch(IOException ioException)
        {
            System.out.println("Error opening population file");
            System.exit(1);
        }
    }
    
 private void ClosePopFile()
    {
        try 
        {
            P_outDataStream.close();
        }
        catch (IOException ioException)
        {
            System.out.println("Error closing population file");
            System.exit(1);
        }
    }
    
 private void WritePopFile()
    {
        for (int i = 0; i < P_tokens.length; i++)
        try
        {
        for (int j = 0; j < P_numbers[i]; j++)
            {
                P_outDataStream.writeBytes(P_tokens[i]);
                P_outDataStream.write('\n');
            }
        }
        catch(IOException ioException)
        {
            System.out.println("error writing population file");
        }
    }
}

