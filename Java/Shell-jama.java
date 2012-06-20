import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import Jama.Matrix;

public class Shell {
    static List<ArrayList<ArrayList<Double>>> read(String filename) {
        ArrayList<ArrayList<Double>> A = new ArrayList<ArrayList<Double>>();
        ArrayList<ArrayList<Double>> B = new ArrayList<ArrayList<Double>>();

        String thisLine;

        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));

            // Begin reading A
            while ((thisLine = br.readLine()) != null) {
                if (thisLine.trim().equals("")) {
                    break;
                } else {
                    ArrayList<Double> line = new ArrayList<Double>();
                    String[] lineArray = thisLine.split("\t");
                    for (String number : lineArray) {
                        line.add((double) Integer.parseInt(number));
                    }
                    A.add(line);
                }
            }

            // Begin reading B
            while ((thisLine = br.readLine()) != null) {
                ArrayList<Double> line = new ArrayList<Double>();
                String[] lineArray = thisLine.split("\t");
                for (String number : lineArray) {
                    line.add((double) Integer.parseInt(number));
                }
                B.add(line);
            }
        } catch (IOException e) {
            System.err.println("Error: " + e);
        }

        List<ArrayList<ArrayList<Double>>> res = new LinkedList<ArrayList<ArrayList<Double>>>();
        res.add(A);
        res.add(B);
        return res;
    }

    static int[][] ijkAlgorithm(ArrayList<ArrayList<Integer>> A,
            ArrayList<ArrayList<Integer>> B) {
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

    static void printMatrix(Matrix matrix, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j != 0) {
                    System.out.print("\t");
                }
                System.out.printf("%.0f", matrix.get(i, j));
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {
        String filename;
        if (args.length < 2) {
            filename = "bigMatrix.txt";
        } else {
            filename = args[1];
        }
        List<ArrayList<ArrayList<Double>>> matrices = read(filename);
        ArrayList<ArrayList<Double>> A = matrices.get(0);
        ArrayList<ArrayList<Double>> B = matrices.get(1);
        int n = A.size();
        double[][] Aarray = new double[n][n];
        double[][] Barray = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Aarray[i][j] = A.get(i).get(j);
                Barray[i][j] = B.get(i).get(j);
            }
        }
        Matrix AM = new Matrix(Aarray);
        Matrix BM = new Matrix(Aarray);
        Matrix CM = AM.times(BM);

        printMatrix(CM, n);
    }

}
