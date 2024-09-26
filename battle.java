import java.util.Scanner;
import java.io.File;
import java.io.FileWriter; 
import java.io.IOException;


public class battle{
	public static void main(String[] args){

		Tools.startScreen();
		int gold = 100;
		Scanner input = new Scanner(System.in);
		Infantry i = new Infantry();
		Archers a = new Archers();
		Cavalry c = new Cavalry();	
		Tools.pause(10000);
		
		boolean battleRunning = true;
		while(battleRunning){
			boolean fightGo = true;
			boolean stillChoosing = true;
			while(stillChoosing){
				System.out.println("-------------------------------------------------------------");
				System.out.println("Gold: "+gold);
				i.printOut();
				a.printOut();
				c.printOut();
				System.out.println("-------------------------------------------------------------");
				System.out.println("1. Get More Infantry");
				System.out.println("2. Get More Archers");
				System.out.println("3. Get More Cavalry");
				System.out.println("4. Go To Battle");
				System.out.println("5. Leave (Save)");
				int choice = input.nextInt();	
				if(choice == 1 && gold >= 3 ){
					gold = i.gainPeople(gold);
				} else if(choice == 2 && gold >= 4){
					gold = a.gainPeople(gold);
				} else if(choice == 3 && gold >= 5){
					gold = c.gainPeople(gold);
				} else if(choice == 4){			
					System.out.println("Oh no.");
					stillChoosing = false;
				} else if(choice == 5){
					try{
						File myFile = new File("battleSaver.txt");
						if(myFile.createNewFile()){
							System.out.println("Your progress is being saved.");
						} else {
							System.out.println();
						}
						FileWriter myWriter = new FileWriter("battleSaver.txt");
						myWriter.write("Hello World");// write stuff in here
						myWriter.close();
					
					} catch (IOException e){
						System.out.println("An error has occurred");
						System.out.println("We apologize for the inconvenience.");
						System.out.println("The problem will be solved shortly");
						System.out.println("Your progress has not been saved.");
						e.printStackTrace();
					
					}
					
					System.out.println("Your progress has been saved, probably");
					stillChoosing = false;
					fightGo = false;
					battleRunning = false;
				}
			}
		
			int oppHealth = (int)(Math.random() * 7000)+500;
			int ogOppHealth = oppHealth;
		       	int speed = (int)(Math.random() * 3) + 1;
			int range = 10;	
			while(fightGo){
				System.out.println("Opponent Health: "+oppHealth);
				System.out.println("Range: "+range);
				System.out.println("Speed: "+speed);
				System.out.println("Which unit do you want to send out?");
				System.out.println("1.Infantry");
				System.out.println("2.Archers");
				System.out.println("3.Cavalry");
				int coolChoice = input.nextInt();
				if(coolChoice == 1 && i.getNumSoldiers() > 0){
					oppHealth = i.doBattle(oppHealth, range);
					i.subPeople();
				} else if(coolChoice == 2 && a.getNumSoldiers() > 0){
					oppHealth = a.doBattle(oppHealth, range);
					if(range <= 3){
						a.subPeople();
					} 
				} else if(coolChoice == 3 && c.getNumSoldiers() > 0){
					oppHealth = c.doBattle(oppHealth, range);
					c.subPeople();
				} else{
					System.out.println("Not in opptions or not enough soldiers");
					range ++;
				}
				range -= speed;
				if(oppHealth <= 0){
					gold += ogOppHealth;
					a.ageUp();
					i.ageUp();
					c.ageUp();
					fightGo = false;	
				} else if(oppHealth > 0 && range < 3 && i.getNumSoldiers()  <= 0 && c.getNumSoldiers() <= 0){
					System.out.println("You have lost the battle.");
					fightGo = false;
					battleRunning = false;
					System.out.println("You have failed Lord Eldersworth, forever changing the course of ducky history");
				}

			}
		
		
		}

	}
}

public class Infantry{
	private int damage; 
	private int numGreen;
	private int numVet;	
	public Infantry(){
		numGreen = 50;
		numVet = 50;
		damage = 0;
	}
	public int getNumGreen(){return numGreen;}
	public int getNumVet(){return numVet;}
	public int getNumSoldiers(){return numVet + numGreen;}
	public void setNumGreen(int t){numGreen = t;}
	public void setNumVet(int y){numVet = y;}	
	public int gainPeople(int gold){
		gold -= 3;
		numGreen ++;
		return gold;
	}
	public void ageUp(){
		numVet += numGreen;
		numGreen = 0;
	}
	public void printOut(){
		System.out.println("Infantry: ");
		System.out.println("	Greens: "+numGreen);
		System.out.println("	Veterans: "+numVet);
	}	
	public void subPeople(){
		if(numGreen >= 20){
			numGreen -= 20;
		} else {
			numGreen = 0;
		} 

		if(numVet >= 10){
			numVet -= 10;
		} else {
			numVet = 0;
		}
	}
	public int doBattle(int oppHealth, int range){
		if(range > 7){
			damage = 0;
		} else if(range > 3){
			damage = (3*numGreen + 4*numVet); 
		} else {
			damage = (5*numGreen + 4*numVet);
		}
		oppHealth -= damage;
		return oppHealth;
	}

}


public class Archers{
	private int damage; 
	private int numGreen;
	private int numVet;
	
	public Archers(){
		numGreen = 50;
		numVet = 50;
		damage = 0;
	}
		
	public int getNumGreen(){return numGreen;}
	public int getNumVet(){return numVet;}	
	public void setNumGreen(int t){numGreen = t;}
	public void setNumVet(int y){numVet = y;}	
	public int getNumSoldiers(){return numVet + numGreen;}

	public int gainPeople(int gold){
		gold -= 4;
		numGreen += 1;
		return gold;
	}
	public void ageUp(){
		numVet += numGreen;
		numGreen = 0;
	}
	public void printOut(){
		System.out.println("Archers: ");
		System.out.println("	Greens: "+numGreen);
		System.out.println("	Veterans: "+numVet);
	}
	public void subPeople(){
		if(numGreen >= 20){
			numGreen -= 20;
		} else {
			numGreen = 0;
		} 

		if(numVet >= 10){
			numVet -= 10;
		} else {
			numVet = 0;
		}
	}
	public int doBattle(int oppHealth, int range){
		if(range > 7){
			damage = (5*numGreen + 6*numVet);
		} else if(range > 3){
			damage = (3*numGreen + 4*numVet); 
		} else {
			damage = 0;
		}
		oppHealth -= damage;
		return oppHealth;
	}
}

public class Cavalry{
	private int damage; 
	private int numGreen;
	private int numVet;

	public Cavalry(){
		numGreen = 50;
		numVet = 50;
	}

	public void ageUp(){
		numVet += numGreen;
		numGreen = 0;
	}

	public int NumGreen(){return numGreen;}
	public int getNumVet(){return numVet;}	
	public void setNumGreen(int t){numGreen = t;}
	public void setNumVet(int y){numVet = y;}	
	public int getNumSoldiers(){return numVet + numGreen;}

	public int gainPeople(int gold){
		gold -= 5;
		numGreen += 1;
		return gold;
	}


	public void printOut(){
		System.out.println("Cavalry:");
		System.out.println("	Greens: "+numGreen);
		System.out.println("	Veterans: "+numVet);
	}
	public void subPeople(){
		if(numGreen >= 20){
			numGreen -= 20;
		} else {
			numGreen = 0;
		} 

		if(numVet >= 10){
			numVet -= 10;
		} else {
			numVet = 0;
		}
	}
	public int doBattle(int oppHealth, int range){
		if(range > 7){
			damage = 0;
		} else if(range > 3){
			damage = (5*numGreen + 6*numVet); 
		} else {
			damage = (3*numGreen + 4*numVet);
		}
		oppHealth -= damage;
		return oppHealth;
	}


}

public class Tools{
	public static void startScreen(){
		System.out.println("You are a warlord hired by Lord Eldersworth to serve as his mercenary army.");
		System.out.println("You have 4 things to consider: gold, infantry, archers, and cavalry.");
		System.out.println("You have 100 of each at the start.");
		System.out.println("Gold is used to buy more units, 3 for infantry, 4 for archers, and 5 for cavalry.");
		System.out.println("Infantry does 3 damage at medium range, 5 at short range, and 0 at far range.");
		System.out.println("Archers do 5 damage at long range, 3 at medium range, and 0 at short range."); 	
		System.out.println("Cavalry does 5 damage at medium range, 3 at short range, and 0 at long range.");		
		System.out.println("Veterans do 1 more damage than greens");
	}

	public static void pause(int time){
		try{
			Thread.sleep(time);
			for(int z = 0 ; z < 30 ; z++){
				System.out.println();
			}
		} catch (InterruptedException e){
			for(int x = 0 ; x < 20 ; x++){
				System.out.println();
			}	
		}
	}


}
