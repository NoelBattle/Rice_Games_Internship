#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
using namespace std;
class Player
{
    public:
  string m_current;
    string name;
    int num_choice;
    int wins;
    double points=0.0;
    int streak=0;
    double score=0.0;
    void set_name(string);  //member function setting the player's name
    string show_name()      //function that displays the player's name
    {
        return name;
    }
     void set_weapon(string);//sets the player's weapon

};
class Game
{   
    int counter;
    Player a;
    Player b;
    string weapon;
    public:
      /* start_game
     * @param Player &one -> This is the player 1 object
     * @param Player &two -> This is the player 2 object
     * @param  &rounds ->this is the number of rounds selected
     * This function is used to start the game
     
     */
    string start_game( Player &one, Player &two, int &rounds)
    {
        a=one;
        b=two; 
        for (int counter=0; counter<rounds;counter++){
            int a_choices [rounds];                     //makes an array containing player 1's choices
            int b_choices [rounds];                     //makes an array containing player 2's choices
            cout<<"It is rounds "<<counter+1<<"\n";

            //Logic for 3x and 6x winning streak for player a
            if (a.streak==3 || a.streak==6)
            {
                cout<<"Player A won last round (now 3 in a row) with "<<a.m_current<<" and Player B used "<<b.m_current<<". Now, Player A can only choose "<<a.m_current<<" or a randomly generated selection for the next round.\n";
                cout<<a.name<<"Choose "<<a.m_current<<" or choose x.\n";
                cin>>weapon;
                a.set_weapon(weapon);
                if (a.m_current=="x")
                {
                    srand(time(NULL));                  //set seed
                    int randNum = (rand() % 3) - 1;     //chooses random number from -1 to 1
                    if(a.num_choice==randNum)           //rerolls if the user choice is is selected at random
                    {
                        int randNum = (rand() % 3) - 1;// -
                    }
                }
                cout<<b.name<<" Choose r, p or s.\n";
                cin>>weapon;
                b.set_weapon(weapon);
            }

            //Logic for 3x and 6x winning streak for player b
            else if (b.streak==3 || b.streak==6)
            {
                cout<<"Player B won last round (now 3 in a row) with "<<b.m_current<<" and Player A used "<<a.m_current<<". Now, Player B can only choose "<<b.m_current<<" or a randomly generated selection for the next round.\n";
                cout<<a.name<<" Choose r, p or s.\n";
                cin>>weapon;
                a.set_weapon(weapon); 
                cout<<b.name<<"Choose "<<b.m_current<<" or choose x.\n";
                if (b.m_current=="x")
                {
                    srand(time(NULL));
                    int randNum = (rand() % 3) - 1;
                    if(b.num_choice==randNum)
                    {
                        int randNum = (rand() % 3) - 1;
                    }
                }   
                cin>>weapon;
                b.set_weapon(weapon);
            }
            //Logic for game
           else
           {
                cout<<a.name<<" Choose r, p or s.\n";
                cin>>weapon;
                a.set_weapon(weapon);  
                cout<<b.name<<" Choose r, p or s.\n";
                cin>>weapon;
                b.set_weapon(weapon);
               // cout<<a.num_choice;
               // cout<<b.num_choice;
                cout<<"\n";
           }
            if (a.num_choice<0 && b.num_choice>0)       //if a chooses rock and b chooses scissors
            {
                cout<<a.name<<" wins\n";
                a.points++;                             //if player wins their points increase by 1
                b.streak=0;                             //if player loses their streak is set to 0
                a.streak++;                             //if player wins their streak is increased by 1
            }
            else if (a.num_choice==0 && b.num_choice<0) //if player a chooses paper and player b chooses rock
            {
                cout<<a.name<<" wins\n";
                a.points++;
                b.streak=0;
                a.streak++;
            }
            else if (b.num_choice<0 && a.num_choice>0)  //if player b chooses rock and player a chooses scissors
            {
                cout<<b.name<<" wins\n";
                b.points++;
                a.streak=0;
                b.streak++;
            }
             else if (a.num_choice==0 && b.num_choice>0) //if player a chooses paper and player b chooses scissors
            {
                cout<<b.name<<" wins\n";
                b.points++;
                a.streak=0;
                b.streak++;

            }
            else if (a.num_choice>0 && b.num_choice==0)  //if player a chooses scissors and player b chooses paper
            {
                cout<<a.name<<" wins\n";
                a.points++;
                b.streak=0;
                a.streak++;
            }
            else if (b.num_choice==0 && a.num_choice<0) //if player b chooses paper and player a chooses rock
            {
                
                cout<<b.name<<" wins\n";
                b.points++;
                a.streak=0;
                b.streak++;
            }
            else                                        //if player a and player b choose the same weapon
            {
                cout<<"nobody wins\n";  
            }
            
            a_choices[counter]=a.num_choice;            //creates an array of player a's choices
            b_choices[counter]=b.num_choice;            //creates an array of player b's choices
        
            //streak logic for player a
            if (a.streak>0)
            {
                if (a_choices[counter-1]==a_choices[counter-2] && a_choices[counter-2]==a_choices[counter-3]) //run if statement if the players last 3 moves has been the same
                {   
                    if (counter>3)
                    {
                        //cout<<"\nMULTIPLIER";
                        a.points =a.points*2;           //doubles the players points
                    }
                } 
                //cout<<"streeeeak";
               if(a.streak==2)
                {
                    a.points =a.points*1.2;
                }
                else if(a.streak==3)
                {
                   a.points= a.points*1.5;
                }
                else if(a.streak==4)
                {
                   a.points= a.points*1.8;
                }
                else if(a.streak==5)
                {
                   a.points=  a.points*2;    
                }
                 else if(a.streak==6)
                {
                   a.points=  a.points*2.5;
                }
                else if(a.streak==7)
                {
                    a.points= a.points*3;    
                }
            }
            //streak logic for player b
            else if (b.streak>0)
            {
                if(b.streak==2)
                {
                    b.points =b.points*1.2;
                    //cout<<"test"<<b.score;
                }
                else if(b.streak==3)
                {
                   b.points= b.points*1.5;
                }
                else if(b.streak==4)
                {
                   b.points= b.points*1.8;
                }
                else if(b.streak==5)
                {
                   b.points= b.points*2;    
                }
                 else if(b.streak==6)
                {
                   b.points= b.points*2.5;
                }
                else if(b.streak==7)
                {
                    b.points= b.points*3;    
                }
            }
            cout<<"Player 1 has "<<a.points<<" Player 2 has "<<b.points<<"\n";  
        }
    return "working";
    }
};

void Player::set_name(string x)                 //function setting player name
{
name=x;
}
void Player::set_weapon(string w)               //function setting player weapon
{
    m_current=w;
                                                //logic that converts player choice into a number for comparrison
    if (m_current=="r"){
        num_choice=-1;
    }
    if (m_current=="p"){
        num_choice=0;
    }
    if (m_current=="s"){
        num_choice=1;
    }
}
int main(){
  std::string name1;                            //initialize variable type string for the user's name
  std::string name2;
  string weapon;
  int rounds;
  std::cout<< "Welcome to Rock, Paper, Scissors"<<"\n";
  std::cout << "What is your name, player 1? "; //ask the user for their name
  getline (std::cin, name1);
  Player player1;                               //creates the Player object "player1"
  player1.set_name(name1);                      //calls the set_name function
  std::cout << "What is your name, player 2? "; //ask the user for their name
  getline (std::cin, name2);
  Player player2;                               //creates the Player object "player2"
  player2.set_name(name2);                      //calls the set_name function
  std::cout << "How many rounds would you like to play? "; 
  std::cin>>rounds;
  Game new_game;                                //Create new game object
  new_game.start_game(player1,player2,rounds);  //calls the start game function
    return 0;
}