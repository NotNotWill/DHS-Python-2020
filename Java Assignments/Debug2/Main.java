import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    
    String magicEightBallIn;
    double magicEightBall;

    magicEightBallIn = JOptionPane.showInputDialog(null, "Enter a number 1 - 8");

    magicEightBall = Double.parseDouble(magicEightBallIn);

    if (magicEightBall == 1){
      System.out.println("Today is going to be a great day!");
    }
    else if (magicEightBall == 2){
      System.out.println("Today you are going to get a lot of homework");
    }
    else if (magicEightBall == 3){
      System.out.println("Today you will have a great meal");
    }
    else if (magicEightBall == 4){
      System.out.println("Today you went bald. Bad day.");
    }
    else if (magicEightBall == 5){
      System.out.println("Today you won free Kool-aid for LIFE!");
    }
    else if (magicEightBall == 6){
      System.out.println("Today your window painting lost... to the freshman");
    }
    else if(magicEightBall == 7){
      System.out.println("You won the lottery!");
    }
    else if(magicEightBall == 8){
      System.out.println("You got locked into the school and had to learn for an extra 8 hours.");
    }
    else{
      System.out.println("Try again");
    }



  }
}