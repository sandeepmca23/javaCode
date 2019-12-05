
public class MissingNumber2 {

	public static void main(String[] args) {
		int[] intarray = new int[] { 7, 6, 10, 5, 9, 2, 1, 15, 7 };
		bubbleSortAscendingOrder(intarray);
		for (int i = 0; i < intarray.length; i++) {
			if (i != 0 && (i + 1) < intarray.length && (intarray[i + 1] - intarray[i]) != 1) {
				boolean flag = true;
				int val = intarray[i];
				while (flag) {
					if (val == intarray[i + 1]) {
						flag = false;
					} else {
						if (val != intarray[i])
							System.out.println(val);
						val++;
					}

				}
			}

		}

	}

	public static void bubbleSortAscendingOrder(int[] intarray) {
		int length = intarray.length;
		int j = 0;
		while (j < length) {
			for (int i = 0; i < length; i++) {
				if ((i + 1) < length) {
					if (intarray[i] > intarray[i + 1]) {
						int t2 = intarray[i];
						intarray[i] = intarray[i + 1];
						intarray[i + 1] = t2;

					}

				}
			}
			j++;
		}
	}

}
