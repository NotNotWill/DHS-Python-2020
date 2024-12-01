import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    String monthIn;
    int month;

    monthIn = JOptionPane.showInputDialog(null,"Enter number of the month");
    month = Integer.parseInt(monthIn);

    if (month == 1) {
      JOptionPane.showMessageDialog(null,"Month entered: January\nDays: 31");
    }
    else if (month == 2) {
      JOptionPane.showMessageDialog(null,"Month entered: February\nDays: 28");
    }
    else if (month == 3) {
      JOptionPane.showMessageDialog(null,"Month entered: March\nDays: 31");
    }
    else if (month == 4) {
      JOptionPane.showMessageDialog(null,"Month entered: April\nDays: 30");
    }
    else if (month == 5) {
      JOptionPane.showMessageDialog(null,"Month entered: May\nDays: 31");
    }
    else if (month == 6) {
      JOptionPane.showMessageDialog(null,"Month entered: June\nDays: 30");
    }
    else if (month == 7) {
      JOptionPane.showMessageDialog(null,"Month entered: July\nDays: 31");
    }
    else if (month == 8) {
      JOptionPane.showMessageDialog(null,"Month entered: August\nDays: 31");
    }
    else if (month == 9) {
      JOptionPane.showMessageDialog(null,"Month entered: September\nDays: 30");
    }
    else if (month == 10) {
      JOptionPane.showMessageDialog(null,"Month entered: October\nDays: 31");
    }
    else if (month == 11) {
      JOptionPane.showMessageDialog(null,"Month entered: November\nDays: 30");
    }
    else if (month == 12) {
      JOptionPane.showMessageDialog(null,"Month entered: December\nDays: 31");
    }
    else {
      JOptionPane.showMessageDialog(null,"Not a valid month number");
    }
  }
}