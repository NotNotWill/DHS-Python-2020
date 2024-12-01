import javax.swing.JOptionPane;
class Main {
  public static void main(String[] args) {
    String totalMinutesIn;
    int totalMinutes, numDays, minutesRemaining, numHours;

    totalMinutesIn = JOptionPane.showInputDialog(null,"Enter total minutes");

    totalMinutes = Integer.parseInt(totalMinutesIn);

    numDays = totalMinutes / 1440;
    minutesRemaining = totalMinutes % 1440;
    numHours = minutesRemaining / 60;
    minutesRemaining = minutesRemaining % 60;


    JOptionPane.showMessageDialog(null,
    "Days: "+numDays+
    "\nHours: "+ numHours+
    "\nMinutes: "+ minutesRemaining);
  }
}