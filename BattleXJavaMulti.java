import java.util.Scanner;
import java.util.HashMap;
import java.util.Random;

@SuppressWarnings("unused")
public class BattlesMulti {
	@SuppressWarnings("resource")
	public static void main(String[] args) throws InterruptedException {
		// fix damgeDone, so that damageDone subtracts from shield first.
		int elementArray1 = 0;
		int elementArray2 = 0;
		
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		
		System.out.println("Welcome to the Arena. You will now battle for our entertainment.");
		System.out.print("Player1 Name: ");
		String player1Name = input.nextLine();
		System.out.print("Choose your element (Water, Fire, Shadow, Air, Earth): ");
		String player1Element = input.nextLine();
		
		int player1Health = (int)(Math.random() * 200 + 100);
		player1Health += 0.0;
		int player1Strength = (int)(Math.random()*100 + 20);
		player1Strength += 0.0;
		
		
		System.out.println();
		
		System.out.print("Player2 Name: ");
		String player2Name = input.nextLine();
		System.out.print("Choose your element (Water, Fire, Shadow, Air, Earth): ");
		String player2Element = input.nextLine();
		
		int player2Health = (int)(Math.random() * 200 + 100);
		player2Health += 0.0;
		int player2Strength = (int)(Math.random()*100 + 20);
		player2Strength += 0.0;
		
		
		System.out.println(player1Name+" has "+player1Health+" health and "+player1Strength+" strength.");
		System.out.println(player2Name+" has "+player2Health+" health and "+player2Strength+" strength.");
		System.out.println();
		
		if (player1Element.equals("Water")) {
			elementArray1 = 0;
		}else if(player1Element.equals("Fire")) {
			elementArray1 = 1;
		}else if(player1Element.equals("Shadow")) {
			elementArray1 = 2;
		}else if(player1Element.equals("Air")) {
			elementArray1 = 3;
		}else if(player1Element.equals("Earth")) {
			elementArray1 = 4;
		}
		
		if (player2Element.equals("Water")) {
			elementArray2 = 0;
		}else if(player1Element.equals("Fire")) {
			elementArray2 = 1;
		}else if(player2Element.equals("Shadow")) {
			elementArray2 = 2;
		}else if(player2Element.equals("Air")) {
			elementArray2 = 3;
		}else if(player2Element.equals("Earth")) {
			elementArray2 = 4;
		}
		
		
		String[][] grid = {
				// name, shield, attack, special
				{"Water", "50", "50", "Storm"}, //hinders attacks for rest of game
				{"Fire", "20", "100", "Burn"}, // Removes half of shield
				{"Shadow","100", "200", "Drain"}, // steals 2x as much health as opponent attack
				{"Air", "10", "90", "Lightning"}, //hinders shields for rest of game
				{"Earth", "150", "30", "Luster"} // Multiplies damageDone by 2
		};
		
		System.out.println("Player1:");
		System.out.println("Shield: "+grid[elementArray1][1]+" Attack: "+grid[elementArray1][2]+" Special: "+grid[elementArray1][3]);
		System.out.println("Player2:");
		System.out.println("Shield: "+grid[elementArray2][1]+" Attack: "+grid[elementArray2][2]+" Special: "+grid[elementArray2][3]);
		
		
		int shieldValue1 = Integer.parseInt(grid[elementArray1][1]);
		int shieldValue2 = Integer.parseInt(grid[elementArray2][1]);
		int attackValue1 = Integer.parseInt(grid[elementArray1][2]);
		int attackValue2 = Integer.parseInt(grid[elementArray2][2]);
		
		int damageDone1 = 0;
		int damageDone2 = 0;
		
		boolean battleActive = true;
		int counter1 = 2;
		int counter2 = 2;
		int shield1 = 0;
		int shield2 = 0;
		
		Thread.sleep(5000);
         
		
		while (battleActive) {
			Scanner choice = new Scanner(System.in);
			
			for (int i = 0; i < 50; i++) {
	        	System.out.println();
	        }
			System.out.println("Player1:");
			System.out.println("Shield: "+grid[elementArray1][1]+" Attack: "+grid[elementArray1][2]+" Special: "+grid[elementArray1][3]);
			System.out.println("Player2:");
			System.out.println("Shield: "+grid[elementArray2][1]+" Attack: "+grid[elementArray2][2]+" Special: "+grid[elementArray2][3]);
			System.out.println();
	        System.out.println("Player1Health: "+player1Health);
	        System.out.println("Player1Shield: "+shield1);
	        System.out.println("Player2Health "+player2Health);
	        System.out.println("Player2Shield "+shield2);
	        // player1
			System.out.println(counter1+"moves until you can do a special (if you choose special when you can't your turn will be skipped");
			System.out.println("Player1, what do you want to do (action)?: ");
			String player1Choice = choice.nextLine();
			if (player1Choice.equals("shield")) {
				System.out.println("Player1 did shield");
				shield1 += shieldValue1;
			}else if(player1Choice.equals("attack")) {
				damageDone1 = attackValue1 - shield2;
				if (damageDone1 == 0){
					shield2 = attackValue1;
					System.out.println("Player1 did no damage to Player2");
				} else if (damageDone1 < 0) {
					shield2 -= attackValue1;
					System.out.println("Player1 did no damage to Player2");
				} else if (damageDone1 > 0) {
					System.out.println("Player1 did "+damageDone1+" attack on Player2");
					player2Health -= damageDone1;
				}
				
			}else if(player1Choice.equals("special") && counter1 == 0) {
				System.out.println("Player1 did special attack: "+grid[elementArray1][3]);
				counter1 = 2;
				//check to see what player1 special attack is
				if (grid[elementArray1][3].equals("Storm")) { //hinders attacks for rest of game
					System.out.println("Player1 did Storm. Player2 attacks = hindered for rest of game");
					attackValue2 /= 2;
				}else if(grid[elementArray1][3].equals("Burn")) { // Removes half of shield
					System.out.println("Player1 did Burn. Player2 Shields halved");
					shield2 /= 2;
				}else if(grid[elementArray1][3].equals("Drain")) { // steals 2x as much health as opponent attack
					player2Health -= (attackValue2)/2;
					player1Health -= (attackValue2)/2;
					System.out.println("Player1 did Drain. Player2 lost health, and Player1 gained health.");
				}else if(grid[elementArray1][3].equals("Lightning")) { //hinders shields for rest of game
					System.out.println("Player1 did lightning. Player2 shields halved.");
					shield2 /= 2;
				}else if(grid[elementArray1][3].equals("Luster")) { // multiplies damage done by 2
					System.out.println("Player1 did Luster. Player 1 attacks multiplied by 2");
					attackValue1 *= 2;
				}
			}else {
				System.out.println("You skipped your turn.");
			}
			damageDone1 = 0;
			counter1 --;
			if (player2Health <= 0) {
				System.out.println("PLAYER1 WON!!!!!!!!!! PLAYER2 Lost!!!!");
				battleActive = false;
				break;
			}
			
			Thread.sleep(5000);
	        for (int i = 0; i < 50; i++) {
	        	System.out.println();
	        } 
	        System.out.println("Player1:");
			System.out.println("Shield: "+grid[elementArray1][1]+" Attack: "+grid[elementArray1][2]+" Special: "+grid[elementArray1][3]);
			System.out.println("Player2:");
			System.out.println("Shield: "+grid[elementArray2][1]+" Attack: "+grid[elementArray2][2]+" Special: "+grid[elementArray2][3]);
			System.out.println();
	        System.out.println("Player1Health: "+player1Health);
	        System.out.println("Player1Shield: "+shield1);
	        System.out.println("Player2Health "+player2Health);
	        System.out.println("Player2Shield "+shield2);
			
			// player2
	        System.out.println(counter2+"moves until you can do a special (if you choose special when you can't your turn will be skipped");
			System.out.println("Player2, what do you want to do (action)?: ");
			String player2Choice = choice.nextLine();
			if (player2Choice.equals("shield")) {
				System.out.println("Player2 did shield");
				shield2 += shieldValue2;
			}else if(player2Choice.equals("attack")) {
				damageDone2 = attackValue2 - shield1;
				if (damageDone2 == 0){
					shield1 = attackValue2;
					System.out.println("Player2 did no damage to Player1");
				} else if (damageDone2 < 0) {
					shield1 -= attackValue2;
					System.out.println("Player2 did no damage to Player1");
				} else if (damageDone2 > 0) {
					System.out.println("Player2 did "+damageDone2+" attack on Player1");
					player1Health -= damageDone2;
				}
			}else if(player2Choice.equals("special") && counter2 == 0) {
			    System.out.println("Player2 did special attack: "+grid[elementArray2][3]);
			    counter2 = 2;
			    // check to see what player2 special attack is
			    if (grid[elementArray2][3].equals("Storm")) { // hinders attacks for the rest of the game
			        System.out.println("Player2 did Storm. Player1 attacks = hindered for the rest of the game");
			        attackValue1 /= 2;
			    } else if (grid[elementArray2][3].equals("Burn")) { // Removes half of shield
			        System.out.println("Player2 did Burn. Player1 Shields halved");
			        shield1 /= 2;
			    } else if (grid[elementArray2][3].equals("Drain")) { // steals 2x as much health as opponent attack
			        player1Health -= (attackValue1) / 2;
			        player2Health -= (attackValue1) / 2;
			        System.out.println("Player2 did Drain. Player1 lost health, and Player2 gained health.");
			    } else if (grid[elementArray2][3].equals("Lightning")) { // hinders shields for the rest of the game
			        System.out.println("Player2 did lightning. Player1 shields halved.");
			        shield1 /= 2;
			    } else if (grid[elementArray2][3].equals("Luster")) { // multiplies damage done by 2
			        System.out.println("Player2 did Luster. Player 2 attacks multiplied by 2");
			        attackValue2 *= 2;
			    }
			} else {
			    System.out.println("You skipped your turn.");
			}

			counter2 --;
			if (player1Health <= 0) {
				System.out.println("PLAYER2 WON!!!!!!!!!! PLAYER1 Lost!!!!");
				battleActive = false;
				break;
			}
			damageDone2 = 0;
	        
	        
		}

	}
	}
