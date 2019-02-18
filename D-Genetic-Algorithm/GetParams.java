import java.io.*;

public class GetParams
{
 private    ObjectOutputStream GP_output;
 private    ObjectInputStream GP_input;
 private    Parameters GP_params;
 private    String GP_fileName;

 //Creates the parameter file--Used by SetParams.java
 public GetParams(String fName, int numChromesI, int numChromes, int numGenes, 
                    double mutFact, int numIterations)
    {
        GP_fileName = new String(fName);
        GP_params = new Parameters(numChromesI,numChromes,numGenes,mutFact,numIterations);
        OpenOutputFile();
        WriteParams();
        CloseOutputFile();
    }

 //Reads the parameter file--Used by GA.java
 public GetParams(String fName)
    {
        GP_fileName = new String(fName);
        OpenInputFile();
        ReadParams();
        CloseInputFile();
    }
 
 private void WriteParams()
    {
    try
        {
            GP_output.writeObject(GP_params);
            GP_output.flush();
        }
    catch (IOException ioException)
        {
            System.out.println("Error writing parameter file");
            System.exit(1);
        }
    }

 private void ReadParams()
    {
    try
        {
            GP_params = (Parameters) GP_input.readObject();
        }
    catch (IOException ioException)
        {
            System.out.println("Error reading parameter file");
            System.exit(1);
        }
    catch (ClassNotFoundException classNotFoundException)
        {
            System.out.println("Error with parameter class");
            System.exit(1);
        }
    }

 private void OpenOutputFile()
    {
    try
        {
            GP_output = new ObjectOutputStream(new FileOutputStream(GP_fileName));
        }
    catch(IOException ioException)
        {
            System.out.println("Error opening output file");
            System.exit(1);
        }
    }

 private void OpenInputFile()
    {
    try
        {
            GP_input = new ObjectInputStream(new FileInputStream(GP_fileName));
        }
    catch(IOException ioException)
        {
            System.out.println("Error opening input file");
            System.exit(1);
        }
    }

 private void CloseOutputFile()
    {
    try 
        {
            GP_output.close();
        }
    catch (IOException ioException)
        {
            System.out.println("Error closing ouput file");
            System.exit(1);
        }
    }

 private void CloseInputFile()
    {
    try 
        {
            GP_input.close();
        }
    catch (IOException ioException)
        {
            System.out.println("Error closing input file");
            System.exit(1);
        }
    }

 public Parameters GetParameters()
    {
        return GP_params;
    }

 }
