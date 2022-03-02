# Adversarial Search based on Game of Nym
___

The code is based on the implementation of Min-Max algorithm using Alpha-Beta pruning for time-complexity 
optimization during the search. The cod eimplements a game which involved two players, one is AI based and the other is 
a human player.

### Game of Nym: 

* **Overview:** Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from 
distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of 
objects provided they all come from the same heap or pile. Depending on the version being played, the goal of the 
game is either to avoid taking the last object or to take the last object.

* **Reference:** https://en.wikipedia.org/wiki/Nim


### Min-Max Algorithm:

* **Overview:** Minimax (sometimes MinMax, MM[1] or saddle point[2]) is a decision rule used in artificial intelligence, decision 
theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) 
scenario. When dealing with gains, it is referred to as "maximin"—to maximize the minimum gain. Originally 
formulated for n-player zero-sum game theory, covering both the cases where players take alternate moves and 
those where they make simultaneous moves, it has also been extended to more complex games and to general 
decision-making in the presence of uncertainty.

* **Reference:** https://en.wikipedia.org/wiki/Minimax

### Alpha-Beta Pruning:

* **Overview:** Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated 
by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine 
playing of two-player games (Tic-tac-toe, Chess, Connect 4, etc.). It stops evaluating a move when at least one 
possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be 
evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes 
away branches that cannot possibly influence the final decision.

* **Reference:** https://en.wikipedia.org/wiki/Alpha–beta_pruning


### Code structure:

* **algorithms.py:** Contains the min-max and alpha-beta pruning algorithms library.
* **main.py:** Contains the game implementation.


## Constraints:

**The game still needs to be optimally implemented, It stills does not work properly**