import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;

public class Shell {
    static List<Vector<Vector<Integer>>> read() {
        Vector<Vector<Integer>> A = new Vector<Vector<Integer>>();
        Vector<Vector<Integer>> B = new Vector<Vector<Integer>>();

        String thisLine;

        try {
            BufferedReader br = new BufferedReader(
                    new FileReader(
                            "/home/moose/Desktop/matrix-multiplication/bigMatrix.txt"));

            // Begin reading A
            while ((thisLine = br.readLine()) != null) {
                if (thisLine.trim().equals("")) {
                    break;
                } else {
                    Vector<Integer> line = new Vector<Integer>();
                    String[] lineArray = thisLine.split("\t");
                    for (String number : lineArray) {
                        line.add(Integer.parseInt(number));
                    }
                    A.add(line);
                }
            }

            // Begin reading B
            while ((thisLine = br.readLine()) != null) {
                Vector<Integer> line = new Vector<Integer>();
                String[] lineArray = thisLine.split("\t");
                for (String number : lineArray) {
                    line.add(Integer.parseInt(number));
                }
                B.add(line);
            }
        } catch (IOException e) {
            System.err.println("Error: " + e);
        }

        List<Vector<Vector<Integer>>> res = new LinkedList<Vector<Vector<Integer>>>();
        res.add(A);
        res.add(B);
        return res;
    }

    static int[][] ijkAlgorithm(Vector<Vector<Integer>> A,
            Vector<Vector<Integer>> B) {
        int n = A.size();

        // initialise C
        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A.get(i).get(k) * B.get(k).get(j);
                }
            }
        }
        return C;
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
        List<Vector<Vector<Integer>>> matrices = read();
        Vector<Vector<Integer>> A = matrices.get(0);
        Vector<Vector<Integer>> B = matrices.get(1);
        int[][] C = ijkAlgorithm(A, B);
        printMatrix(C);
    }

}
