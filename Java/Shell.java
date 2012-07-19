import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import org.kohsuke.args4j.CmdLineException;
import org.kohsuke.args4j.CmdLineParser;

/**
 * This class manages I/O.
 * @author Martin Thoma
 */
public class Shell {
    static List<ArrayList<ArrayList<Integer>>> read(File filename) {
        ArrayList<ArrayList<Integer>> A =
            new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> B =
            new ArrayList<ArrayList<Integer>>();

        String thisLine;

        try {
            BufferedReader br = new BufferedReader(
                    new FileReader(filename));

            // Begin reading A
            while ((thisLine = br.readLine()) != null) {
                if (thisLine.trim().equals("")) {
                    break;
                } else {
                    ArrayList<Integer> line =
                        new ArrayList<Integer>();
                    String[] lineArray = thisLine.split("\t");
                    for (String number : lineArray) {
                        line.add(Integer.parseInt(number));
                    }
                    A.add(line);
                }
            }

            // Begin reading B
            while ((thisLine = br.readLine()) != null) {
                ArrayList<Integer> line = new ArrayList<Integer>();
                String[] lineArray = thisLine.split("\t");
                for (String number : lineArray) {
                    line.add(Integer.parseInt(number));
                }
                B.add(line);
            }
        } catch (IOException e) {
            System.err.println("Error: " + e);
        }

        List<ArrayList<ArrayList<Integer>>> res =
            new LinkedList<ArrayList<ArrayList<Integer>>>();
        res.add(A);
        res.add(B);
        return res;
    }

    static void printMatrix(int[][] matrix) {
        for (int[] line : matrix) {
            int i = 0;
            for (int number : line) {
                if (i != 0) {
                    System.out.print("\t");
                } else {
                    i++;
                }
                System.out.print(number);
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {
        CommandLineValues values = new CommandLineValues(args);
        CmdLineParser parser = new CmdLineParser(values);

        try {
            parser.parseArgument(args);
        } catch (CmdLineException e) {
            System.exit(1);
        }

        // Now you can use the command line values
        List<ArrayList<ArrayList<Integer>>> matrices =
            read(values.getSource());
        ArrayList<ArrayList<Integer>> A = matrices.get(0);
        ArrayList<ArrayList<Integer>> B = matrices.get(1);
        int[][] C = MatrixMultiplication.ijkAlgorithm(A, B);
        printMatrix(C);
    }

}
