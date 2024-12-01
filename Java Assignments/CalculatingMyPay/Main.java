import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    String hoursIn, wageIn; 
    double hours, wage, grosswage, afterfedtax, afterstatetax, netpay;

    hoursIn = JOptionPane.showInputDialog(null,"Enter hours worked:");
    wageIn = JOptionPane.showInputDialog(null,"Enter yor hourly wage");

    hours = Double.parseDouble(hoursIn);
    wage = Double.parseDouble(wageIn);

    grosswage = hours * wage;
    afterfedtax = grosswage * 0.2;
    afterstatetax = grosswage * 0.053;
    netpay = grosswage - (afterstatetax + afterfedtax); 

    JOptionPane.showMessageDialog(null,
    "GrossWage: $"+ grosswage+
    "\nState tax is $"+ afterstatetax+
    "\nFederal tax is $" + afterfedtax+
    "\nYour net pay is $"+ netpay);
  }
}