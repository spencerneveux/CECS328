import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Tester {
    public static void main(String[] args) {
        RedBlackTreeMap rb = new RedBlackTreeMap();
        List<String[]> values = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader("players_homeruns.csv"))) {
            String line = reader.readLine();

            // Insert first 5 elements into RedBlackTreeMap
            for (int i = 0; i < 5; i++) {
                String[] attr = line.split(",");
                System.out.println(attr[0] + " " + attr[1]);
                rb.add(attr[0], attr[1]);
                line = reader.readLine();
            }
            // Print first 5 elements in pre-order
            rb.printStructure();

            //Insert next 5 elements into Tree
            for (int i = 5; i < 10; i++) {
                String[] attr = line.split(",");
                System.out.println(attr[0] + " " + attr[1]);
                rb.add(attr[0], attr[1]);
                line = reader.readLine();
            }

            // Print Tree
            rb.printStructure();

            // Find a-d
            System.out.println(rb.find("Babe Ruth"));
            System.out.println(rb.find("Honus Wagner"));
            System.out.println(rb.find("Rogers Hornsby"));
            System.out.println(rb.find("Ted Williams"));

            // Insert remaining elements
            for (int i = 10; i < 3835; i++) {
                String[] attr = line.split(",");
                rb.add(attr[0], attr[1]);
                line = reader.readLine();
            }

            // Print the tree
            rb.printStructure();

            // Find a-d
            System.out.println(rb.find("Zeb Terry"));
            System.out.println(rb.find("Honus Wagner"));
            System.out.println(rb.find("A.J. Ellis"));
            System.out.println(rb.find("A.J. Hinch"));


        }catch(FileNotFoundException e) {
            System.out.println(e.getMessage());
        }catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
