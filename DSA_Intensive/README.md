This repository intends to tbe the first step towards the beginnig of dominion of data structures and algorithms for comprehending machine learning and projecting for our future roles as a full stack developer. Data structures is the type of data and methods utilized in programming for organizing data in continguous memory for instance. Some of the most common data structures to be utiized is arrays, or lists in python.

Knowing when and how to apply algorithms require good knowledge of the languagem the criteria and better learning prblem solving. This concept is loosely called algorithmic thinking. This form of thinking is a concept that comes up frequently in big tech's technical interviews. So, understanding this is the good pathway towards a solid job, but also this paves way for the fulfillment of our big goals.


Qualities about algorithms:
1) follows a certain set of guidelines
2) must have a clear problem statement
3) muat contain a specific set of instructions in a correct order
4) each step must be explicitly clear
5) algorithms should produce a result
6) should eventually finish, and not run indefinitely
7) needs to be a sorted series of values
8) needs to be distinct and specific.
9) result must be produced consistently. It should work the same everytime.

Steps to take to build an alogrithm:
1) use the same steps each time we take steps
2) how the input is defined and what the output is defined when the search is done
3) have it be sequential
4) have it return a result


Time Complexity
This defines how long takes for an operation to search for the desired value and find it in the shortest amount of time. This concept usually describes how efficient the search algorithm is. Running the algorithm for effective evaluation should take its best scenario and its worst case scenario. It should take into consideration how fast and how slow its target valued is found through a series of performance testing. You do this usually by giving it small as well as large values and data sets in order to find its time complexity. 

Big O notation:
Theoretical definition of the complecity of an algorithm as a function of the size. O is order of magnitude of complexity, which lets us know how long it takes to find the value or position. Here are the types of notations:

O(1) -> search in constant time. It is equally fast and slwo regardless of hoe many inputs it is given

O(n) -> search in linear time. The operation search is consequential to the amount of values, or n, given. As the values given grows larger, the operation also takes larger. This does have a benefit, though. This has the benefit of having usually shorter searches when the data is sorted, which is commonly done on alorithmic searching. It does it much better than binary [O(log n)].

O(log n) -> binary search. This could also be called sublinear time operations or notations. These are great due to levelling out as operations begin to expand and amplify, giving us better operation on large structures. 

O(n**2) -> search in quadratic time, or squared notation. The reason it is called quadratic time is due to the nature of the search: you perform this search on a squared amount of n given. This type of search is performed in two dimensional arrays(matrices or grids); so for instance, you are given a matrix with a 3x3 layout, meaning you have to search through 3 numbers in a set of 3 subsets. You could also call this 3^2, hence the name. This is usually the worst case for many algorithms. 

O(n ** 3) cubic runtime

O(n log n) -> quasilinear runtime. You perform linear search compounded on top of a binary search. These are usually found in sorting algorithms. Merge Sort is a good example of a O(n log n). 

Space complexity:
Amount of memory that the operation takes in the computer. There should be a good ratio of time and space complexity. Operations should take good time, but should also take fewer memory in order for the best efficiency to be obtained


Linear Search:
Searches for the value located in a sequential fashion. The higher the value, the longer the operation and the longer that it takes in time. 

Binary Search:
The algorithm is something to search for. This does not return the value we are looking for, instead it returns the position where the value is located. It takes a sorted list of values and returns the position of the value if the list if it exists. Or it makes case to express that it does not exists. In contrast to linear search, binary search takes significantly longer in a sequential search in comparison to linear search


All of these are considered polynomial runtimes, where n ** k is usually polynomial runtimes, in contrast to the next type of algorithms. These are exponential runtimes.

Exponential runtimes:
This is a performance of algorithms on top of algorithms. This could also be called brute forcing, where you search one by one, rinse and repeat until you find it, and then you repeat that process exponentially. This is characteristically impossible to resolve in a short amount of time.

O(n!) -> factorial time search: this indicates the number of combinations that are needed to solve for any given to effectuate the function, compounded to the sum of the previous operations. Example:
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720

Data Structures:
Data structures are structures that contain data in an ordered fashion. Data structures, such as arrays, are stored continguously in memory, meaning that it is sequentially placed wherever it is allocated in memory. Some example of data structures are: arrays, lists, strings, objects, dictionaries, etc. Each one is developed not only with its own quirks and characteristics(such as the data type, and structure capacity), but also with its own logic for manipulating and selecting its data. These will be discussed individually as we continue down the road.

Lists
Lists is an object exclusive to Python. it is an array-like object that stores heterogeneous data as well as homogenous data. Lists in Python are mutable, meaning that its original structure can be changed without having to create a duplicate. In order to search for objects inside of a list, we can search by index (list[x] where x is the position located inside of the list), or by iterating through the list(with a for loop or a while loop) and setting conditions to find a specific input or value contained inside of a list. The elements are not stored continguously in memory as it would on an array, instead, a reference is stored to where the ACTUAL data in memory is located. So, if my list is in x place in memory, the content inside of the list is a reference to another place that is not x. That place is where the value given to the data is actually stored.

List methods:
1) Append: this is a builtin method that adds a value to a give position if input, otherwise, it adds the value to the end. Appending is usually a constant time operation, or O(1).
2) Extend: this builtin method allows us to extend the contents of our list by inserting the contents of another list at the end of the first one.
3) Delete: thre are several methods to delete an item from a position

Linked Lists:
Linked Lists are linear lists that contains nodes. Nodes are bytes of data that contain two pieces of information: the first one being the actual data stored in it and the second is a reference to the next node on the list if it exists. The content of the list has two specific nodes that are defined by their position on the list: the head node, which is the first element of a linked list, that stands before all of the remaining nodes on the list; and the tail node, which is the final element of a linked list, and therefore, has a null reference to the next element on the list since there is none. Nodes are also called self-referential objects, which refers to itself instead of to another. The advantage of linked lists is that it can better insert data at specific reference points

Thre are several linked lists: singly linked lists and doubly linked lists. The difference between them is that there are two links in the doubly linked lists now, the first being a reference to the element that comes after it, and a refernece to the element that came before it. With this, we also get an additional quirk for the head and tail nodes: head has a null previous reference, whereas tail has a null next reference. Meaning, that the head can point to the next element, but not the previous one, while tail can point to the previous element, but not the next one.

Arrays:
it is a continguous memory block filled with data, that stores data to  block of memory and can be searched by looking for the reference point in memory(a pointer). The compiler chooses the place in memory where it can be stored depending on the size. This means that data is homogenous and that sizes are fixed. 