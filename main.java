// Online Java Compiler
// Use this editor to write, compile and run your Java code online
// import java.util.Scanner;


// class Main {
    
//     public static void main(String[] args) {
//         Scanner reader = new Scanner(System.in); // Reading from System.in

//         System.out.println("Try programiz.pro");
//     // ans the next token of the input as an int
//         System.out.println("Enter a number: ");
//         int n = reader.nextInt();
//         int totalPair = 0;
//         int totalInPair = 0;
        
//         while(n != 100) {
//             // for(int i = 0)
//             if(n % 2 == 0) {
//                 System.out.println("Even");
//                 System.out.println(Math.pow(n, 2));
//                 System.out.println(Math.sqrt(n));
//                 totalPair += n;
//             } else {
//                 System.out.println("Odd");
//                 totalInPair += n;
//             }
//             System.out.println("Enter a number: ");
//             n = reader.nextInt();
//         }
        
//         // Once finished
//         reader.close();
//     }
// }


//diagonal Start
//     *
//    ***
//   *****
//  *******

// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int n = 10;
        // int nbrStars = 1;
        // int middle = (int)Math.ceil(n / 2);
        
        for(int i = 1; i <= n; i++) {
            for(int j = n - i; j > 0; j--) {
                System.out.print(" ");
            }
            // for(int k = 0; k < nbrStars; k++) {
            //     System.out.print("*");
            // }
            if(i == 1) {
                System.out.println("*");
            }
            
            // if( i >  1) {
                for(int l = 0; l < i * 2; l++) {
                    System.out.print("*");
                }
            // }
            // nbrStars++;
            System.out.println();
        }
        
    }
}

// schema of the Zarabiya like this * * * * * * 
				    * +       *
				    *  +      *
				    *   +     *
				    *     +   *
				    *       + *
				    * * * * * * 


// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        // System.out.println("Try programiz.pro");
        // System.nextInt()
        int n = 18;
        int cpt = 0;
        int mdN = (int)Math.floor(n / 2);
        
        for(int i = 0; i <= n; i++) {
            for(int j = 0; j <= n; j++) {
                if(i == 0) {
                    System.out.print("* ");
                } else if(i != 0 && (j == 0 || j == n)) {
                    System.out.print("* ");
                } else if(i == n) {
                    System.out.print("* ");
                } else if(i == mdN && !(i == mdN && j == mdN)) {
                    System.out.print("- ");
                } else if(j == mdN && !(i == mdN && j == mdN)) {
                    System.out.print("| ");
                } else if(i == mdN && j == mdN) {
                    System.out.print("+ ");
                } else if(i == j) {
                    System.out.print("* ");
                } else if((n - cpt) == j) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");   
                }
            }
            cpt++;
            System.out.println("");
        }
    }
}