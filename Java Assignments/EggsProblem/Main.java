import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    int eggs, cartons, leftover;
    String eggsIn;

    eggsIn = JOptionPane.showInputDialog(null,"How many eggs do you have");
    eggs = Integer.parseInt(eggsIn);

    cartons = eggs / 12;
    leftover = eggs % 12;

    JOptionPane.showMessageDialog(null, cartons+" cartons\n"+leftover+" leftover");
  }
}