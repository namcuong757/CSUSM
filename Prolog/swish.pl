/*References:
 * https://www.doc.gold.ac.uk/~mas02gw/prolog_tutorial/prologpages/
 * 
 * */

/************
 * Facts
 * Always start with lowercase letter, end with full stop
 * You could use _ in facts (names), but please avoid math operators
*/

thanksgivingsoon.
sunny.
wanttoplay.

/*These are all facts. This whole page is your database for your facts & rules.
You can also ask questions/query about your database.*/

/*Now, on the right side, after the ?- ask your first query:
 * sunny.
 * Hit run and see if the answer is yes
 * the ?- means asking a question, it is already provided by this complier. 
 * You would need to write it in other compliers in format: ?- sunny.
*/

/*Now, ask query: ?- raining.
 * 
 *procedure `raining' does not exist*/

/*You can defind facts with arguments. (just like a function with input variables)
 * It is just relationship between items.
 * Relation names must begin with lowercase letter as well.*/

likes(mary,food).
likes(mary,wine).
likes(john,wine).
likes(john,mary).

/*Ask query: ?- likes(mary,food).*/

/*true*/

/*OK, some KOANS about facts: */

eats(fred,oranges).                           /* "Fred eats oranges" */
eats(fred,T-bonesteaks).                    /* "Fred eats T-bone steaks" */
eats(tony,apples).                          /* "Tony eats apples" */
eats(john,apples).                         /* "John eats apples" */

/*Ask some queries on the right side:
 * Does Fred eats T-bone steaks?
 * ?- eats(tony,pears). means what? What is the result?*/

/*means "Does tony eat pears" outpu is false*/

/*You can also link up two sentances with ,
 * Try query:
 * ?- eats(fred,_X),_X=oranges
 * What is the output? What is the meaning of this query?*/
/*output is true. Does Fred eat something where it is oranges*/

age(ian,2).                   /*  Ian is 2 */

/*will query ?- age(ian, two). give yes? Why?*/

/*no because the type is different string vs int*/

/*************
 * Variables
 * With only the facts, we cannot really do anything productive with this PL.
 * Just like other PLs, we need variables.
 * Variables have to start with a CAPITAL letter
 * The process of matching items with variables is known as unification.*/
/*
 * X: vairable X
 * Myvar: another legal variable
 * Myvar_current: also ok*/

/*What is the result of query ?- eats(fred,FoodX). ?
 *Make sure you press next button to see all the results.
 *In other editors, you would type ; to represent show next result.*/

/*FoodX = oranges
  FoodX = _1316-bonesteaks*/

/***********
 * Rules
 * Each rule can have several variations -- clauses.
 * Rules provide ways to get inferences about facts.
 */

/*Operator :- means if*/
mortal(X) :- 
    human(X).  /*X is mortal if X is human*/
human(petter).  /*give a fact that petter is a human*/

/*mortal(petter).*/ /*Ask query: is petter mortal?*/
/*What is the result of your query?*/
/*true*/

/*mortal(X).*/ /*Ask query: who is mortal?*/
/*X=Peter*/ /*What is the result of your query?*/

/*One rule can have several variations.
 * The following example shows 3 ways that some thing is fun*/

fun(X) :-                      /* an item is fun if */ 
        red(X),                /* the item is red */
        car(X).                /* and it is a car */
fun(X) :-                      /*  or an item is fun if */
        blue(X),               /* the item is blue */
        bike(X).               /* and it is a bike */
fun(ice_cream).                /* and ice cream is also fun. */

/*Together with some facts:*/
car(vw_beatle).
car(ford_escort).
bike(harley_davidson).
red(vw_beatle).
red(ford_escort).
blue(harley_davidson).

/*fun(harley_davidson).*/ /*Ask query: is harley_davidson fun?*/
/*true*/ /*What is the result of your query?*/
/*What are the logical steps that Prolog took to find the answer for you?
 * Hint: start matching from the first fun clause.*/
/*it firstly check if harley_davidson is a bike or not
 * then if it is true then it will check if is it a blue bike then if both conditions
 * return true it will finally return true*/

/*fun(X).*/ /*Ask query: What is fun?*/

/****************
 * Recursion
 */
/*some facts:*/
move(home,taxi,halifax). /*__your answer here___*/
move(halifax,train,gatwick). /*__your answer here___*/
move(gatwick,plane,rome). /*__your answer here___*/

/*on_route is a recursive predicate*/
on_route(rome).
on_route(Place):-       /*what does this mean?*/ /*__your answer here___*/
	move(Place,_Method,NewPlace), /*__your answer here___*/
	on_route(NewPlace).  /*__your answer here___*/

/* Query ?- on_route(home). is asking whether you can reach rome from home*/
/*What are the steps that Prolog can use to find the answer for you?*/
/*__your answer here___*/

/*Change _Method to Method, what will happen?*/
/*By adding _ in front of a variable, we make it an anonymous variable and let the complier know 
 * this var is not important so stop complaining about it.
 * Does this remind you of some thing from F#?*/

/*****************
 * List
 */
[a,b,c,d,e,f,g]. /*a list with simple facts*/
/*__your answer here___*/ /*an empty list*/
/*__your answer here___*/ /*a list with 3 names as facts*/

/*Just like F#, list in Prolog matches Head and Tail.*/
p([H|T], H, T). /*bind/unify list [...] with head item H, and tail item T*/
/*__your answer here___*/ /*What is the meaning of query ?-p([a,b,c], X, Y). ?*/
/*__your answer here___*/ /*Output?*/

/*write queries to cut H and T out from the above 3 lists.*/
/*__your answer here___*/

/*Search an item from a list, write down the meaning of each line:*/
inList(Item,[Item|Rest]). /*__your answer here___*/
inList(Item,[IgnoreHead|Tail]) :- /*__your answer here___*/
    	inList(Item,Tail). /*__your answer here___*/

/*Write a query that test if apple is in the list [apple, pear, banana]*/
/*__your answer here___*/
/*What are the steps that Prolog can use to find the answer for you?*/
/*__your answer here___*/
/*Write a query that test if apple is in the list [pear, apple, banana]*/
/*__your answer here___*/
/*What are the steps that Prolog can use to find the answer for you?*/
/*__your answer here___*/

/*Does this example reminds you of some thing from F#?*/
/*__your answer here___*/