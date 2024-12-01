import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    
    String tacosIn;
    double tacos, cost, total, tax;
    cost = 3.79; // This is the cost per taco
    tax = 0.06; // tax is 6%

    tacosIn = JOptionPane.showInputDialog(null, "Welcome to Mr. Tocci's Taco shop, how many tacos would you like to buy today?");

    tacos = Double.parseDouble(tacosIn);

    total = cost * tax; 

    JOptionPane.showConfirmDialog(null, "Your total will be " + total);

  }
}