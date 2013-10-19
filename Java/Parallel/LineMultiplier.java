import java.util.ArrayList;
import java.util.concurrent.Callable;

public class LineMultiplier implements Callable<int[]> {
	ArrayList<Integer> A;
	ArrayList<ArrayList<Integer>> B;
	public int[] CLine;
	
	public LineMultiplier(ArrayList<Integer> a, ArrayList<ArrayList<Integer>> b) {
		A = a;
		B = b;
		CLine = new int[b.get(0).size()];
	}

	@Override
	public int[] call() {
		for (int j=0; j<B.get(0).size(); j++){
			for (int k=0; k<B.size(); k++) {
				ArrayList<Integer> line = B.get(k);
				Integer value = line.get(j);
				CLine[j] += A.get(k)*value;
			}
		}
		return CLine;
	}
}
