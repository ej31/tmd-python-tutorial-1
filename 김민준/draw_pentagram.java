public class draw_pentagram {
    public static void main(String[] args){
        int i = 0;
        int j = 0;
        int k = 0;

        // Step 1
        for(i = 1; i <= 20; i++){
            for(j = 1; j <= (70 - i); j++){
                System.out.print(" ");
            }
            for(k = 1; k <= (2 * i); k++){
                System.out.print("*");
            }
            System.out.println();
        }

        //Step 2
        int NumOfSpaces = (--j);
        int NumOfLetters = (--k);
        int MaxEndLettersCount;

        for(MaxEndLettersCount = NumOfLetters+10, NumOfLetters = 2*NumOfSpaces+NumOfLetters, NumOfSpaces=0;
            NumOfLetters > MaxEndLettersCount; NumOfLetters -= 10, NumOfSpaces += 5){
            for(j = 1; j <= NumOfSpaces; j++){
                System.out.print(" ");
            }
            for(k = 1; k <= NumOfLetters; k++){
                System.out.print("*");
            }
            System.out.println();
        }

        // Step 3
        for(MaxEndLettersCount = NumOfLetters + 10; NumOfLetters <= MaxEndLettersCount; NumOfLetters += 2, NumOfSpaces -= 1){
            for(j = 1; j <= NumOfSpaces; j++){
                System.out.print(" ");
            }
            for(k = 1; k < NumOfLetters; k++){
                System.out.print("*");
            }
            System.out.println();
        }

        // Step 4
        for(int internalSpace = 0, scount = NumOfLetters; scount > 0; NumOfLetters += 2, NumOfSpaces -= 1, internalSpace += 6){
            for(j = 1; j < NumOfSpaces; j++){
                System.out.print(" ");
            }
            scount = NumOfLetters - internalSpace;
            for(k = 1; k <= (scount/2); k++){
                System.out.print("*");
            }
            for(k = 1; k <= internalSpace; k++){
                System.out.print(" ");
            }
            for(k = 1; k <= (scount/2); k ++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
