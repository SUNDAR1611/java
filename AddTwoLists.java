import java.util.*;

public class AddTwoLists {
    public static void main(String[] args) {
        List<Integer> list1 = Arrays.asList(3, 3, 4);
        List<Integer> list2 = Arrays.asList(4, 2, 2);

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < list1.size(); i++) {
            result.add(list1.get(i) + list2.get(i));
        }

        System.out.println("Result: " + result);
    }
}