import java.io.*;

public class JobFileHandler {
    public static void main(String[] args) {
        String fileName = "job.txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            System.out.print("Reading file: " + fileName +"  "+ "content:"+ "\n");
            while ((line = reader.readLine()) != null) {
                System.out.println(line); 
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}
