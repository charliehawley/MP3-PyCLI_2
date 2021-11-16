# GONE ROGUE - the procedurally generated CLI action fighter

The year is 1980. Miami is burning, Post-Its just hit the shelves, the MGM is on fire and somebody just shot John Lennon.

The world is chaotic and unpredictable. Will there be peace? Will there be revolution? Can capitalism survive?

In an unstable world, two buddies sought to create a new world that reflected the turbulence around them.

Enter procedural generation, a way of producing 'randomised' worlds from stable rules.

This is the world of Rogue, the original Roguelike game that bore an entire genre
dedicated to those seeking to witness the illusion of control shattering before them.

It gave them something they had never seen before. The game had agency, a life of its own.

Now, 40 years later, entropy has flaunted its inescapable will and laid waste to the optimism of the 20th Century.

The only cure? Surrendering yourself to endless possibility.

Some can follow their instincts and get their hands dirty, 
others fall behind trying to reason with the chaos.

How will you fare in the bloody world of GONE ROGUE?
___

1 enemy

1 prize

1 exit

level is a class where the __init__ creates each entity and randomizes its positional index

All tiles show what they are (Hero, Enemy, Prize, Stairs, empty space)

start on random index, sprite is name[0].upper() 
actions are performed with user input: W,A,S, or D followed by ↩

w = Up
a = Left
s = Down
d = Right

Enemy icon: Entity('#enemy', 2)
this will ensure enemy.icon is #

Base attributes = HP: 10, Damage: 2-3
Enemy attributes = HP: 5, Damage: 1

Loot = Big ol' Sword: +5 damage, Dagger: +2 damage, Ice Wand: freeze enemy, Lunch: +5 HP

0-6 because 10 felt big and long to navigate

TO DOs:
- exit function, in case user wants to restart and doesn't know how
- add amulet room? or hide stairs under boss? nope, stairs print last.
- choose not to go down? choice y/n change check_pos to "walk"
- level 2 exit sometimes creates input loop
	- entities sometimes spawn under first position on last level 
- remove stairs incentive
- print level title above map
- check dialogue format is standard throughout


OUT OF SCOPE?

- clear battle notifications after battle
- hp stops at zero
- Print enemy HP for level beneath map
- music? sound effects?
- Compass?  C: ^ > v < x		where x means sprite is within one move of an object
- Q to fight
- freeze state on entities, miss attack turn
- Event listeners for movement
- Difficulty: hard lowers hero hp 
	- testing showed that game is well balanced currently at 15hp, 10hp probs too hard
- Enemy moves: (to move enemy closer to hero (needs to account for negative values))
    if (enemy[x]-hero[x]) > (enemy[y]-hero[y]):
	    enemy[x] += 1
    else:
	    enemy[y] += 1
- easter egg indexes
- expand item pool

## KNOWN BUGS

- spawn on ents on level 3
- level 2 sometimes creates an input loop on level exit (interaction with stairs)

## FIXED BUGS

- menu glitch
- loot after spawn

## DEPLOYMENT

- create account on heroku.com
- verify account
- create password
- click create a new app
- choose an app name and region
- go to 'settings'
- add buildpacks: 
    - python
    - node.js
- go to 'deploy'
- if you're using github, choose github as your deployment method
- in the 'App connected to GitHub, search and select the app to deploy
- in the 'Automatic Deploys' section, you can choose to set up automatic deployment of any updates to the main branch of your GitHub repository
- you can then click the 'Deploy Branch' button and watch Heroku build your app in the terminal below
- once Heroku has finished this process, it will provide you with a link to the deployed app






acknowledgements:
Thanks to game testers Sam McGoun and Tom Healey

I read Matt B's Calico Jack src code for inspiration on this project:
os.system('cls' if os.name == 'nt' else 'clear')

clear last line:
https://stackoverflow.com/questions/44565704/how-to-clear-only-last-one-line-in-python-output-console

titles generated at:
https://patorjk.com/software/taag/#p=testall&h=0&v=3&f=Bloody&t=gone%20rogue
