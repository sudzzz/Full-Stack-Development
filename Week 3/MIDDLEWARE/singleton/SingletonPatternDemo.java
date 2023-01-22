public class SingletonPatternDemo {
 public static void main(String[] args) 
{
// SingleObject s=new SingleObject();\
SingleObject s =SingleObject.getInstance();
s.showMessage();

 }
}