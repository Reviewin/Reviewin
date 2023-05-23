import 'dart:io';

void main() {
  function([[1, 2, 0],[2, 1, 0],[2, 1, 1]]);
}
bool function(List<List<int>> list_game) {
  bool won = false;
    // cas colomne 1er 
    if(list_game[0][0] == list_game[1][0] && list_game[0][0] == list_game[2][0]) {
      won = true;
      stdout.write("Player ${list_game[0][0]} won the game");
    }
    else {
      won = false;
    }
    // cas diagonal 1er
    if(list_game[0][0] == list_game[1][1] && list_game[2][2] ==  list_game[0][0]) {
      won = true;
      stdout.write("Player number ${list_game[0][0]} won the game");
    }
    else {
      won = false;
    }
    // cas row 1
    if(list_game[0][0] ==  list_game[0][1] && list_game[0][0] == list_game[0][2]) {
      won = true;  
      stdout.write('Player number ${list_game[0][0]} won the game');
    }
    else{
      won = false;
    }
    // cas row 2
    if(list_game[1][0] == list_game[1][1] && list_game[1][0] == list_game[1][2]){
      won = true;
      stdout.write("Player number ${list_game[1][0]} won the game");
    }
    else {
      won = false;
    }
    // cas row 3
    if(list_game[2][0] == list_game[2][1] && list_game[2][0] == list_game[2][2]) {
      won = true;
      stdout.write('Player number ${list_game[2][0]} won the game');
    }
    else {
      won = false;
    }
    // cas colomne 2
    if(list_game[0][1] == list_game[1][1] && list_game[0][1] == list_game[2][1]) {
      won = true;
      stdout.write('Player number ${list_game[0][1]} won the game');
    }
    else {
      won = false;
    }
    // cas colomne 3
    if(list_game[0][2] == list_game[1][2] && list_game[0][2] == list_game[2][2]) {
      won = true;
      stdout.write('Player number ${list_game[0][2]} won the game');
    }
    else {
      won = false; 
    }
    // cas diagonale 2
    if(list_game[0][2] == list_game[1][1] && list_game[0][2] == [2][0]) {
      won = true;
      stdout.write('Player number ${list_game[0][2]} won the game');
    }
    else {
      won = false;
    }
  return won;
}
