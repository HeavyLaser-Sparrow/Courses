//java code
import java.util.Scanner;
import java.util.Random;


public class MyProgram{
    public static void main(String[] args)throws InterruptedException{
        
        //battle damage = (yourStrength - enemyStrength)/2 + 1
        // variables: 
        // opponentName,opponentHealth, opponentStrength
        // yourHealth, yourStrength, animalName
        
        System.out.println("Welcome to the arena, where your animal will fight others for our crude entertainment.");    
        
        //sets up the battle
        //get your animal
        Scanner input = new Scanner(System.in);
        System.out.print("Name your animal: ");
        String animalName = input.nextLine();
        //getYourHealth
        int yourHealth = (int)(Math.random() * 200 + 100 );
        yourHealth += 0.0;
        //getYourStrength
        int yourStrength = (int)(Math.random()*100 + 20);
        yourStrength += 0.0;
        
        final double ogHealth = yourHealth;
        
        boolean battleActive = true;

        while (battleActive){
            System.out.println("Your animal's name is "+animalName);
            System.out.println("Its health is: "+yourHealth);
            System.out.println("Its strength is "+yourStrength);
            System.out.println();
            
            //get your opponent
            int randomOpponentIndex = (int)(Math.random() * 10);
            //String[][] grid = new String[10][3];
            
            String[][] grid = {
                // name, health, strength
                {"Galvex", "50", "300"},
                {"ASDF", "1000", "1000"},
                {"Mad Hatter", "500", "200"},
                {"Dark  Maister", "200", "400"},
                {"The Dark Empire", "200", "300"},
                {"StringMan", "2000", "50"},
                {"Tozy", "500", "30"},
                {"Unnamed Warrior", "50", "30"},
                {"The Broken One", "200", "200"},
                {"Doggy", "1", "1"}
            };
            
            String opponentName = grid[randomOpponentIndex][0];
            double opponentHealth = Double.parseDouble(grid[randomOpponentIndex][1]);
            int opponentStrength = Integer.parseInt(grid[randomOpponentIndex][2]);
            
            
            System.out.println("You will fight: "+opponentName);
            System.out.println("Its health is: "+opponentHealth);
            System.out.println("Its strength is: "+opponentStrength);
            
            Thread.sleep(5000);
            
            System.out.println("MAY YOUR NAME GO DOWN IN LEGEND");
            
            Thread.sleep(2000);
            
            //clears screen
            for (int i = 0; i < 50; i++) {
                System.out.println();
            }
            
            double damageDone;
            
            if (yourStrength>opponentStrength){
                damageDone = (yourStrength - opponentStrength)/2 + 1;
            }else{
                damageDone = (opponentStrength - yourStrength)/2 + 1;
            }
            
            boolean battleGoing = true;
            int counter = 0;
            // does the battle
            while (battleGoing){
                
                //your turn
                //check if hit
                Random random = new Random();
                int missHit1 = random.nextInt(2);
                if (missHit1 == 1){
                    System.out.println("You missed!");
                }else{
                    System.out.println("You made a hit!");
                    System.out.println(opponentName+" lost "+ damageDone+" health.");
                    opponentHealth -= damageDone;
                    if (opponentHealth <= 0){
                        System.out.println("YOU WIN!!!!");
                        yourHealth += ogHealth+(opponentHealth/2);
                        counter ++;
                        for (int i = 0; i < 50; i++) {
                            System.out.println();
                        }
                        battleGoing = false;
                        break;
                    }
                }
                
                Thread.sleep(3000);
                for (int i = 0; i < 50; i++) {
                System.out.println();
                } 
                System.out.println("Your Health: "+yourHealth);
                System.out.println("Opponent Health: "+opponentHealth);
                //opponent  turn
                //check if hit
                Random random2 = new Random();
                int missHit2 = random2.nextInt(2);
                if (missHit2 == 1){
                    System.out.println(opponentName+" missed!");
                }else{
                    System.out.println(opponentName+" hit you.");
                    System.out.println("You lost "+ damageDone+" health");
                    yourHealth -= damageDone;
                    if (yourHealth <= 0){
                        System.out.println("YOU LOST!!!"+opponentName+" has won!");
                        for (int i = 0; i < 50; i++) {
                            System.out.println();
                        }
                        battleActive = false;
                        battleGoing = false;
                        break;
                    }
                }
                
                Thread.sleep(3000);
                for (int i = 0; i < 50; i++) {
                System.out.println();
                }
                System.out.println("Your Health: "+yourHealth);
                System.out.println("Opponent Health: "+opponentHealth);
                
            }
            System.out.println("You Survived "+counter+" battles.");
            
        }
        
        
        
        
    }
}