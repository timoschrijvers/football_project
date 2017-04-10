package org.lejos.pcexample;

import lejos.nxt.Motor;

public class NXT2 {
	final static int turnTime = 22 ; // turnTime is the time needed to turn approximately 1 degree.
	final static int startTurnTime = 20 ; // The time needed to give the motors the right speed
	final static int driveTime = 24 ; // driveTime is the time needed to drive approximately 1 milimeter.
	final static int startDriveTime = 15; // The time needed to give the motors the right speed
	final static int catchTime = 1200; // catchTime is the time needed to lower or upper the catch bar in the right position.
	
	//The NXT robot will turn left for the amount of degrees that is given with the parameter degree. 
	public static void turnLeft(int degree){
		Motor.B.backward();
		Motor.C.forward();
		turn(degree);
	}
	//The NXT robot will turn right for the amount of degrees that is given with the parameter degree.
	public static void turnRight(int degree){
		Motor.B.forward();
		Motor.C.backward();
		turn(degree);
	}
	
	//The NXT robot will continue for the amount of degrees that is given in the parameter and stop after.
	public static void turn(int degree){
		try {
			Thread.sleep(turnTime*(degree + startTurnTime));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Motor.B.stop();
		Motor.C.stop();
	}
	
	// The robot will drive in a given direction for a particular distance.
	// distance is the distance the robot will drive in milimeters. 
	// If forward = true, then the robot will drive forwards, else it will drive backwards.
	public static void drive(int distance, boolean forward){
		if (forward){
			Motor.B.forward();
			Motor.C.forward();
		}
		else {
			Motor.B.backward();
			Motor.C.backward();
		}
		try {
			Thread.sleep(driveTime* (distance + startDriveTime));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Motor.B.stop();
		Motor.C.stop();
	}
	
	// turnup will turn the ballcatcher at the front of the robot up or down. 
	// If direction is true, then the catcher will go down, else it will go up. 
	// If the catcher is already down, or up it cannot go further in that direction. 
	public static void turnup(boolean direction)	{	
		if (direction){
			try {
				Motor.A.forward();
				Thread.sleep(catchTime);
				Motor.A.stop();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else{
			try {
				Motor.A.backward();
				Thread.sleep(catchTime);
				Motor.A.stop();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	public static void computerProgram(String[] args) throws InterruptedException{
		Motor.A.setSpeed(50);
		Motor.B.setSpeed(100);
		Motor.C.setSpeed(100);
		if (args[0].equals("forward")){
			int i = Integer.valueOf(args[1]);
			NXT2.drive(i, true);
		}
		else if (args[0].equals("backward")){
			int i = Integer.valueOf(args[1]);
			NXT2.drive(i, false);
		}
		else if (args[0].equals("left")){
			int i = Integer.valueOf(args[1]);
			NXT2.turnLeft(i);
		}
		else if (args[0].equals("right")){
			int i = Integer.valueOf(args[1]);
			NXT2.turnRight(i);
		}
		else if (args[0].equals("up")){
			NXT2.turnup(false);
		}
		else if (args[0].equals("down")){
			NXT2.turnup(true);
		}
		System.out.println("done");
	}
	
	public static void main(String[] args) throws InterruptedException {
		NXT2.computerProgram(args);
	}
}
