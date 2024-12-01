import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    double width, length, area, cost, total;
    String lengthIn, widthIn, costIn;
    
    lengthIn = JOptionPane.showInputDialog(null,"Enter your length: ");
    length = Double.parseDouble(lengthIn);

    widthIn = JOptionPane.showInputDialog(null,"Enter your width: ");
    width = Double.parseDouble(widthIn);

    costIn = JOptionPane.showInputDialog(null,"Enter your cost per square foot: ");
    cost = Double.parseDouble(costIn);

    area = length * width;
    total = area * cost;
    JOptionPane.showMessageDialog(null,"The total cost is $"+total);
  }
}