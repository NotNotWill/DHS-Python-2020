import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    String numString;
    double number;

    numString = JOptionPane.showInputDialog(null, "Enter a number");
    number = Double.parseDouble(numString);

    if (number < 0){
      JOptionPane.showMessageDialog(null,"Your number is a negative");
    }
    else if (number == 0){
      JOptionPane.showMessageDialog(null,"Your number is 0");
    }
    else{
      JOptionPane.showMessageDialog(null,"Your number is a positive");
    }
    
  }
}