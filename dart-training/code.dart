import 'dart:io';
import 'dart:math';


// The Guessing Game
void main() {
  password_gen();
  }

password_gen(){
  stdout.write("Bienvenue dans votre générateur de mot de passe :");
  stdout.write('Veuillez choisir le nombres de caractères aléatoires à générer (6 min) :');
  String charr = stdin.readLineSync()!;
  int char = int.parse(charr);
  if(char > 6){
    List<String> alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    List<String> uppercase = [];
    List<String> digits = ['1','2','3','4','5','6','7','8','9','0'];
    List<String> password = [];
    for (int i = 0; i < alphabet.length; i++){
      uppercase.add(alphabet[i].toUpperCase());
    }
    for (int i = 0; i<=char; i++) {
      password.add(uppercase[Random().nextInt(25)]);
      password.add(digits[Random().nextInt(10)]);
      password.add(alphabet[Random().nextInt(25)]);
    }
    print("Your generated password ${password.join('')}");
    }
  else{
    print('Veuillez relancer le programme vous avez choisi une mauvaise valeur');
  }
}















//void main () {
  //List first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
  //List second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
  //List final_list = [];
  //for(var i = 0; i < second_list.length; i++){
    //if (i < first_list.length){
      //if (second_list.contains(first_list[i]) && first_list[i] < 5){
        //final_list.add(first_list[i]);
        //print("Done at i = ${i}");
        //print(final_list);
        //print(i);
      //}else{
        //print('Do nothing at i = ${i}');
        //print(i);
      //}
    //}
  //else if (i>first_list.length) {
    //if (first_list.contains(second_list[i]) && second_list[i] < 5) {
      //final_list.add(second_list[i]);
      //print(i);
    //}
  //}
    //}
  //print(final_list);
  //}
