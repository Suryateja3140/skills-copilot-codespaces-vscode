# Vinidata Assessment

Implemented using Python

Libraries used:

1. Pandas

Part 1:

1. Find Playerwise Loyalty points earned by Players in the following slots:-
    a. 2nd October Slot S1
    b. 16th October Slot S2
    b. 18th October Slot S1
    b. 26th October Slot S2

a. 2nd October Slot S1

-> Filtered all the user Ids who belongs to given slot
-> Now with same filtered user Ids and time slot I have got the corresponding withDraw amount from WithDraw Table.
-> Now I combined this table(filtered table data) to Deposit table and got Deposit Amount details for the Filtered User IDs.
-> After completing above steps list of userIds is empty so not able to calculate the loyalty points and followed same procedure for other slots mentioned.

To run the code:

-> We can Open Python supported IDE eg: Pycharm
-> Download all the files provided in this repository
-> run main.py file.
