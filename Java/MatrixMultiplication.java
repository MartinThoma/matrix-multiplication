import java.util.ArrayList;
import java.util.Vector;

/**
 * This class offers different algorithms for matrix multiplication.
 * @author Martin Thoma
 */
public class MatrixMultiplication {
    static int[][] ijkAlgorithmVector(Vector<Vector<Integer>> A,
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

    static int[][] ijkAlgorithm(ArrayList<ArrayList<Integer>> A,
            ArrayList<ArrayList<Integer>> B) {
        int n = A.size();

        // initialise C
        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                for (int j = 0; j < n; j++) {
                    C[i][j] += A.get(i).get(k) * B.get(k).get(j);
                }
            }
        }
        return C;
    }

    static int[][] ikjAlgorithm(ArrayList<ArrayList<Integer>> A,
            ArrayList<ArrayList<Integer>> B) {
        int n = A.size();

        // initialise C
        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                for (int j = 0; j < n; j++) {
                    C[i][j] += A.get(i).get(k) * B.get(k).get(j);
                }
            }
        }
        return C;
    }
}

