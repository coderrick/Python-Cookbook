# first
'''
 Java example

 public class Person {
  private String firstName;
  private String lastName;
  private String address;
  private String username;
  //The constructor method
  public Person(String firstName, String lastName, String address, String username)
  {
    this.firstName = firstName;
    this.lastName = lastName;
    this.address = address;
    this.username = username;
  }
  // A method to display the state of the object to the screen
  public void displayPersonDetails()
  {
    System.out.println("Name: " + firstName + " " + lastName);
    System.out.println("Address: " + address);
    System.out.println("Username: " + username);
  }
 }

 '''

 class Person:
   def __init__(self, first_name, last_name, address, username):
     self.first_name = first_name
     self.last_name = last_name
     self.address = address
     self.username = username

     

