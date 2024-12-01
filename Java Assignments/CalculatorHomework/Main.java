import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    double val1, val2, sum, diff, product, avg;
    String val1In, val2In;

    val1In = JOptionPane.showInputDialog(null,"Enter first value");
    val2In = JOptionPane.showInputDialog(null,"Enter second value");
    
    val1 = Double.parseDouble(val1In);
    val2 = Double.parseDouble(val2In);

    sum = val1 + val2;
    diff = val1 - val2;
    product = val1 * val2;
    avg = (val1 + val2) /2;

    JOptionPane.showMessageDialog(null, "Calculation Results:\n"+
    "First Value Entered = "+ val1+"\n"+
    "Second Value Entered = "+ val2+"\n"+
    val1+" + "+val2+ " = "+sum+"\n"+
    val1+" - "+val2+ " = "+diff+"\n"+
    val1+" * "+val2+ " = "+product+"\n"+
    val1+" = "+val2+ " / 2 = "+avg);

  }
}