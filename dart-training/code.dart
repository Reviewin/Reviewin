import 'dart:io';
import 'dart:math';

// The Guessing Game
void main() {
  int random_digit = Random().nextInt(9999);
  List<int> random_digit_found = [];
  int cows = 0;
  int bulls = 0;
  print(random_digit);
  do {
    stdout.write('Choose an index and a number');
    int? digit = int.tryParse(stdin.readLineSync()!);
    int? index = int.tryParse(stdin.readLineSync()!);
    if (digit != null && index != null && random_digit.toString().contains(digit.toString()) && random_digit.toString().indexOf(digit.toString()) == index) {
      random_digit_found.add(digit);
      cows += 1;
      continue;
    } else if (digit != null && index != null && random_digit.toString().contains(digit.toString()) && random_digit.toString().indexOf(digit.toString()) != index) {
      print('False index, try again');
      bulls += 1;
      continue;
    } else {
      bulls += 1;
      print('Totally false');
      continue;
    }
  } while (new Set<int>.from(random_digit_found).length != 10);
  print(bulls);
  print(cows);
  print(random_digit);
}