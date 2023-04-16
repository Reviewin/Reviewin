import 'dart:io';
import 'dart:math';


// The Guessing Game
void main() {
  fibonacci(50);
  }
fibonacci(int number_terms) {
  int first_fibonnaci = 1;
  int second_fibonnaci = 1;
  List<int> fibonnaci_list = [];
  for (int i = 0; i<= number_terms; i++) {
    int next_term = first_fibonnaci + second_fibonnaci;
    first_fibonnaci = second_fibonnaci;
    second_fibonnaci = next_term;
    fibonnaci_list.add(next_term);
  }
  print(fibonnaci_list);
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
