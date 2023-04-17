import 'dart:io';
import 'dart:math';


// The Guessing Game
void main() {
  int random_digit = Random().nextInt(9999);
  List<int> random_digit_found = [];
  int cows = 0;
  int bulls = 0;
  do {
    stdout.write('Choose an index and a number');
    int digit = int.parse(stdin.readLineSync()!);
    int index = int.parse(stdin.readLineSync()!);
    if (random_digit.toString().contains(digit.toString()) && random_digit.toString().indexOf(digit.toString()) == index) {
      random_digit_found.add(digit);
      cows+=1;
    }else if (random_digit.toString().contains(digit.toString()) && random_digit.toString().indexOf(digit.toString()) != index){
      print("False index, try again");
      bulls+=1;
      continue;
    }
    else{
      bulls+=1;
      print('Totally false');
      continue;
    }
  } while(int.parse(random_digit_found.toString()) != random_digit);
  print("${bulls}");
  print('${cows}');
  print(random_digit);
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
