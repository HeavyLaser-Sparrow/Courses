
import java.util.Scanner;

public class Ship{
	public static void main(String[] args){
		
		Scanner input = new Scanner(System.in);
		System.out.println("Do you want a [t]orpedo boat or a [d]readnought?: ");
		String whichShip = input.nextLine();
		if(whichShip.equals("t")){	
			TorpedoBoat myBoat = new TorpedoBoat();
			System.out.println("You own a torpedo-boat");
			boolean keepGoing = true;
			while(keepGoing){
				System.out.println();
				myBoat.willPrint();
				System.out.println("Do you want to [d]ock [s]etSail [lo]adTorpedo [f]ireTorpedo [le]ave");
				String choice = input.nextLine();
				if(choice.equals("le")){
					System.out.println("Ok, Bye");
					keepGoing = false;
				} else if(choice.equals("d")){
					myBoat.dock();
				} else if(choice.equals("s")){
					myBoat.setSail();
				} else if(choice.equals("lo")){
					myBoat.load();
				} else if(choice.equals("f")){
					myBoat.fire();
				}
				System.out.println();
				if(myBoat.getHealth() <= 0){
					System.out.println("You have been sunk");
					keepGoing = false;
				}
			}
		} else {
			System.out.println("You have yourself a dreadnought");
			Dreadnought myDread = new Dreadnought();
			boolean keepGoings = true;
			while(keepGoings){
				System.out.println();
				myDread.willPrint();
				System.out.println("Do you want to [d]ock [s]etSail [lo]adTorpedo [f]ireTorpedo [le]ave");
				String choice = input.nextLine();
				if(choice.equals("le")){
					System.out.println("Ok, Bye");
					keepGoings = false;
				} else if(choice.equals("d")){
					myDread.dock();
				} else if(choice.equals("s")){
					myDread.setSail();
				} else if(choice.equals("lo")){
					myDread.load();
				} else if(choice.equals("f")){
					myDread.fire();
				}
				System.out.println();
				if(myDread.getHealth() <= 0){
					System.out.println("You have been sunk");
					keepGoings = false;
				}
			}
	
		}

	}
}

public class Navy{
	private boolean atSea;
	private int health;
	private boolean enemy;
	
	public Navy(int asdf){
		atSea = false;
		health = asdf;
		enemy = false;
	}
	

	public void setSail(){
		atSea = true;
		System.out.println("Setting Sail Now");
	}
	public void dock(int max){
		if(atSea){
			System.out.println("Docking Now");
			atSea = false;
			health = max;
			enemy = false;
		} else {
			System.out.println("You are already at a dock");
		}
		
		int prb = (int)(Math.random() * 10) + 1; // 1-10
		if(prb > 0){
			enemy = true;
			System.out.println("Oh no! An enemy approaches.");
			System.out.println("SHOOT THEM!!!!");
		} 
	
	}	
	public boolean getSea(){return atSea;}
	public int getHealth(){return health;}
	public boolean getEnemy(){return enemy;}
	public void subHealth(int x){
		health -= x;
	}
	public void ridEnemy(){enemy = false;}

}


public class Dreadnought extends Navy{
	private int numShells;
	private boolean loaded;
	public Dreadnought(){
		super(1000);
		loaded = false;
		numShells = 50;
	}
	
	public void dock(){
		if(getSea()){
			super.dock(1000);
			numShells = 50;
			System.out.println("You have docked and loaded up on supplies");
		} else {
			System.out.println("You are already docked");
		}
	}

	public void load(){
		numShells -= 5;
		System.out.println("5 shells loaded");
		loaded = true;
	}
	
	public void fire(){
		if(getSea()){
			if(loaded){ 
				System.out.println("You have fired your salvo");
				if(getEnemy()){
					int aPrb = (int)(Math.random() * 10) + 1;
					int bPrb = (int)(Math.random() * 10) + 1;
					int cPrb = (int)(Math.random() * 10) + 1;
					int dPrb = (int)(Math.random() * 10) + 1;
					int ePrb = (int)(Math.random() * 10) + 1;
					if(aPrb > 7 || bPrb > 7 || cPrb > 7 || dPrb > 7 || ePrb > 7){
						ridEnemy();
						System.out.println("You have taken out the enemy!");
					} else {
						System.out.println("You missed...");
						subHealth(30);
						System.out.println("They shot at you!");
					}
				}
			}
		} else {
			System.out.println("You are not allowed to fire shells while docked");
		}
	}

	public void willPrint(){
		System.out.println("Health: "+getHealth());
		System.out.println("AtSea Status: "+getSea());
		System.out.println("NumShells: "+numShells);
		System.out.println("Loaded: "+loaded);
		System.out.println("Ship Nearby: "+getEnemy());
	}

	

}







public class TorpedoBoat extends Navy{
	private int numTorpedo;
	private boolean loaded;
	public TorpedoBoat(){
		super(100);
		numTorpedo = 10;
		loaded = false;
	}
	
	public void dock(){
		if(getSea()){
			super.dock(100);
			numTorpedo = 10;
			System.out.println("You have docked and loaded up on supplies");
		} else {
			System.out.println("You are already docked");
		}	
	}

	public void load(){
		if(numTorpedo >= 2){
			numTorpedo -= 2;
			System.out.println("2 torpedo's loaded");
			loaded = true;
		} else {
			System.out.println("Sorry, but you do not have any torpedos left");
		}
	}
	
	public void fire(){
		if(getSea()){
			if(loaded){
				System.out.println("Shooting Torpedo Now");
				loaded = false;
				if(getEnemy()){
					int xPrb = (int)(Math.random() * 10) + 1;
					int yPrb = (int)(Math.random() * 10) + 1;
					if(xPrb > 5 || yPrb > 5){
						System.out.println("You have taken down the enemy!");
						ridEnemy();
					} else {
						System.out.println("You missed...");
						subHealth(30);
						System.out.println("They shot at you!");
					}
				}
			} else {
				System.out.println("Sorry, but you do not have any torpedos loaded");
			}
		} else {
			System.out.println("You are not allowed to shoot torpedos when you are docked");
		}
	}

	public void willPrint(){
		System.out.println("Health: "+getHealth());
		System.out.println("AtSea Status: "+getSea());
		System.out.println("NumTorpedos: "+numTorpedo);
		System.out.println("Loaded: "+loaded);
		System.out.println("Ship Nearby: "+getEnemy());
	}


}

