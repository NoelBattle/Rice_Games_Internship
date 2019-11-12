#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>
using namespace std;
class Player
{
    private:
    string name;
    int num_choice;
    public:
  string m_current;
    
    double newp;
    int wins;
    double points;
    int streak=0;
    double score=0.0;
    void set_name(string);  //member function setting the player's name
    void setpoints(double points)
    {
    newp=points;
   // return "TESTTEST";
    }


    string get_name()      //function that displays the player's name
    {
        return name;
    }
    int get_numchoice()
    {
        return num_choice;
    }
     void set_weapon(string);//sets the player's weapon
};
class Game
{   
    int counter;
    Player a;
    Player b;
    Player p;
    string weapon;
    int choices[];
    public:
    
  /* streak_func
     * @param Player &P -> This is the player object
     * This function occurs when a player wins 3 times in a row, randomizing the 
     */
    void streak_func(Player &P){
        p=P;
         cout<<p.get_name()<<" won last round (now 3 in a row) with "<<p.m_current<<" and the other player used "<<b.m_current<<". Now,"<<p.get_name()<<"can only choose "<<a.m_current<<" or a randomly generated selection for the next round.\n";
                cout<<p.get_name()<<"Choose "<<p.m_current<<" or choose x.\n";
                cin>>weapon;
                p.set_weapon(weapon);
                if (p.m_current=="x")
                {
                    srand(time(NULL));                  //set seed
                    int randNum = (rand() % 3) - 1;     //chooses random number from -1 to 1
                    if(p.get_numchoice()==randNum)           //rerolls if the user choice is is selected at random
                    {
                        int randNum = (rand() % 3) - 1;// -
                    }
                }
               
    }
      /* streak_points
     * @param Player &P -> This is the player object
     * @param int *choice -> This is the player's choice'
     * @param int counter ->this is aa round counter
     * This function is used determine the player's points after they are on a winning streak
     
     */
    void streak_points(Player &P, int *choice, int counter){
         p=P;
         if (choice[counter-1]==choice[counter-2] && choice[counter-2]==choice[counter-3]) //run if statement if the players last 3 moves has been the same
                {   
                    if (counter>3)
                    {
                        //cout<<"\nMULTIPLIER";
                        p.setpoints(p.points*2);           //doubles the players points
                    }
                }      
        if(p.streak==2)
            {
                cout<<"streeeeak"<<"\n";
                p.points=p.points*1.2;
                p.setpoints(p.points);
                   // cout<<"sssss"<<p.newp;
                   // cout<<"tttt"<<a.newp;
                   // cout<<"uuu"<<b.newp; 
                }
                else if(p.streak==3)
                {
                   p.setpoints(p.points*1.5);
                }
                else if(p.streak==4)
                {
                   p.setpoints(p.points*1.8);
                }
                else if(p.streak==5)
                {
                   p.setpoints(p.points*2);    
                }
                 else if(p.streak==6)
                {
                   p.setpoints(p.points*2.5);  
                }
                else if(p.streak==7)
                {
                    p.setpoints(p.points*3);
                    //cout<<"Player 1 has "<<a.points<<" Player 2 has "<<b.points<<"\n";
                }
            if (a.streak>0)
                {
                    a.newp=p.newp;
                }
            if (b.streak>0)
                {
                    b.newp=p.newp;
                }
              cout<<"streaak Player 1 has "<<a.newp<<" Player 2 has "<<b.newp<<"\n";   
    }
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
        a.newp=0.0;
        b.newp=0.0;
        for (int counter=0; counter<rounds;counter++){
            int a_choices [rounds];                     //makes an array containing player 1's choices
            int b_choices [rounds];                     //makes an array containing player 2's choices
            cout<<"It is rounds "<<counter+1<<"\n";

            //Logic for 3x and 6x winning streak for player a
            if (a.streak==3 || a.streak==6)
            {
                streak_func(a);
                cout<<b.get_name()<<" Choose r, p or s.\n";
                cin>>weapon;
                b.set_weapon(weapon);
            }
            //Logic for 3x and 6x winning streak for player b
            else if (b.streak==3 || b.streak==6)
            {
                streak_func(a);
                cout<<"Player B won last round (now 3 in a row) with "<<b.m_current<<" and Player A used "<<a.m_current<<". Now, Player B can only choose "<<b.m_current<<" or a randomly generated selection for the next round.\n";
                cout<<a.get_name()<<" Choose r, p or s.\n";
                cin>>weapon;
                a.set_weapon(weapon); 
            }
            //Logic for game
           else
           {
                cout<<a.get_name()<<" Choose r, p or s.\n";
                cin>>weapon;
                a.set_weapon(weapon);  
                cout<<b.get_name()<<" Choose r, p or s.\n";
                cin>>weapon;
                b.set_weapon(weapon);
               // cout<<a.num_choice;
               // cout<<b.num_choice;
                cout<<"\n";
           }
            if (a.get_numchoice()<0 && b.get_numchoice()>0)       //if a chooses rock and b chooses scissors
            {
                cout<<a.get_name()<<" wins\n";
                a.points++;
                a.setpoints(a.points++);                             //if player wins their points increase by 1
                b.streak=0;                             //if player loses their streak is set to 0
                a.streak++;                             //if player wins their streak is increased by 1
            }
            else if (a.get_numchoice()==0 && b.get_numchoice()<0) //if player a chooses paper and player b chooses rock
            {
                cout<<a.get_name()<<" wins\n";
                a.points++;
                a.setpoints(a.points);
                b.streak=0;
                a.streak++;
            }
            else if (b.get_numchoice()<0 && a.get_numchoice()>0)  //if player b chooses rock and player a chooses scissors
            {
                cout<<b.get_name()<<" wins\n";
                b.points++;
                b.setpoints(b.points);
                a.streak=0;
                b.streak++;
            }
             else if (a.get_numchoice()==0 && b.get_numchoice()>0) //if player a chooses paper and player b chooses scissors
            {
                cout<<b.get_name()<<" wins\n";
                b.points++;
               b.setpoints(b.points);
                a.streak=0;
                b.streak++;
            }
            else if (a.get_numchoice()>0 && b.get_numchoice()==0)  //if player a chooses scissors and player b chooses paper
            {
                cout<<a.get_name()<<" wins\n";
                a.points++;
                a.setpoints(a.points);
                b.streak=0;
                a.streak++;
            }
            else if (b.get_numchoice()==0 && a.get_numchoice()<0) //if player b chooses paper and player a chooses rock
            {
                
                cout<<b.get_name()<<" wins\n";
                b.points++;
                b.setpoints(b.points);
                a.streak=0;
                b.streak++;
            }
            else                                        //if player a and player b choose the same weapon
            {
                cout<<"nobody wins\n";  
            }
            //cout<<"Player 1 has "<<a.newp<<" Player 2 has "<<b.newp<<"\n";
            a_choices[counter]=a.get_numchoice();            //creates an array of player a's choices
            b_choices[counter]=b.get_numchoice(); //creates an array of player b's choices
           
           
            //streak logic for player a
            if (a.streak>0)
            {
              streak_points(a,a_choices,counter);
              //cout<<"Player 1 has "<<a.points<<" Player 2 has "<<b.points<<"\n";  
            }
            //streak logic for player b
            else if (b.streak>0)
            {
             streak_points(b,b_choices,counter);
            // cout<<"Player 1 has "<<a.points<<" Player 2 has "<<b.points<<"\n";  
            }
           else
           {
           cout<<"Player 1 has "<<a.newp<<" Player 2 has "<<b.newp<<"\n";
           }

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
  string name1;                            //initialize variable type string for the user's name
  string name2;
  string weapon;
  int rounds;
  cout<< "Welcome to Rock, Paper, Scissors"<<"\n";
  cout << "What is your name, player 1? "; //ask the user for their name
  getline (cin, name1);
  Player player1;                               //creates the Player object "player1"
  player1.set_name(name1);                      //calls the set_name function
  cout << "What is your name, player 2? "; //ask the user for their name
  getline (cin, name2);
  Player player2;                               //creates the Player object "player2"
  player2.set_name(name2);                      //calls the set_name function
  cout << "How many rounds would you like to play? "; 
  cin>>rounds;
  Game new_game;                                //Create new game object
  new_game.start_game(player1,player2,rounds);  //calls the start game function
    return 0;
}