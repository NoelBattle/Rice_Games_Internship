#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>

int main()
{
  std::string name; //initialize variable type string for the user's name
  std::cout<< "Weclome to the Right Road, Wrong Road Game!"<<"\n";
  std::cout << "What is your name? "; //ask the user for their name
  getline (std::cin, name);
  std::cout << "Hello, " << name << "\n"<<"There is a Monster attacking the towns in Hyrule. "<<"\n"<<"You must track it down and choose which direction he went. "<<"\n"<<"If you choose wrong, The monster will DEVOUR the entire town!!!"<<"\n";
  int lives=5;//number of lives
  int demon_num;//variable for random int
  int rounds=1;//Number of turns alive.
  while (lives>0)
  {
    std::cout<<"It is round "<<rounds<<"\n";
    std::string player_choice;//initialize string for the player's choice
    std::string demon_choice; 
    srand (time(NULL));//sets seed for rand() function
    demon_num=rand()%2;//chooses a random number from 0-1
    //std::cout<<demon_num; for testing
    //increases round after each loop
    if(demon_num==0){ //converts the random number into a string representing a road
        demon_choice="right"; 
    }else{
        demon_choice="left";
    }
    std::cout<<"You have "<< lives<< " lives!"<<"\n";
    std::cout<<"Which road you would like to choose: right or left?"<<"\n";
    std::cin>> player_choice;
    
    if (player_choice==demon_choice){
        std::cout<<"You chose the correct road and defeated the demon!"<<"\n";
        rounds++;
    }else{
        lives--;
        std::cout<<"You chose the wrong road! You now have "<<lives<<" lives\n";
        rounds++;
    }
  }
  if(lives==0)// condition for what happens when the player is out of lives
  {
      rounds--;
      std::string score;
       if(rounds<=5)
        {score="F";}
       if(5<rounds&& rounds<10)
        {score="D";}
        if(9<rounds&& rounds<12)
        {score="C";}
        if(11<rounds&& rounds<15)
        {score="B";}
         if(14<rounds&& rounds<20)
        {score="A";}
        if(rounds>19) //calculates player score baased on the number of rounds
        {score="S";}
    
      std::cout<<"You lose!"<<"\n"<<"You lasted "<<rounds<<" rounds. Your score is "<<score<<".\n";//end of game message
  }
    return 0;
}
