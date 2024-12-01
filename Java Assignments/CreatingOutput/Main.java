import javax.swing.JOptionPane;
class Main {

  public static void main(String[] args) {

    String name;

    System.out.println("Hello world!");
    name = JOptionPane.showInputDialog(null, "Give me your name");
    JOptionPane.showMessageDialog(null, "Welcome to this program, "+name);
  }
}