import java.util.*;
public class stringLet{
    public static void main(String[]args){
        Scanner a=new Scanner(System.in);
        System.out.println("Enter a String=");
        String s=a.nextLine();
        int spa=0;
        int let=0;
        int digi=0;
        for(int i=0;i< s.length();i++){
            char ch=s.charAt(i);
            if(Character.isLetter(ch)){
                let++;
            }
            else if(Character.isDigit(ch)){
                digi++;
            }
            else if(Character.isSpace(ch)){
                spa++;
            }
        }
        System.out.println("Entered String=" + a);
        System.out.println("Number of Letters=" + let);
        System.out.println("Number of Digits=" + digi);
        System.out.println("Number of Spaces=" + spa);
    }
}