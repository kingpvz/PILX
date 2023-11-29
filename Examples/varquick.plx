/This example shows how you can quickly operate with numeric variables
/To begin, create a variable with the + operator and assign it a numeral value.
+var=10;
/You can add 1 by using another + after the first one!
++var;
/Keep in mind to not assign another value here, or an error will be thrown!
/Now we are stroing "11" in var, let's take a look:
[out]var;
/We can also subtract 1 using "-" after the + operator.
+-var;
/Now we are back on "10"
[out]var;
/There are more operations we can try. Using the * operator, we can multiply the value by itself (square it):
+*var;
[out]var;
/Now we are at "100"
/Last operation is the power up (raise to the power of itself) - the "^" operator, however, this one should only be used with smaller numbers.
/Using it with bigger numbers may cause it to be set to the "maximum integer" value, as you can see below:
+var=567;
+^var;
[out]var;
/This above is the "biggest integer", you can go above it, but no longer can you raise its power.
/Let's try it with a little lower numbers:
+var=4;
+^var;
[out]var;
/Keep in mind you can only perform these operations on numeral variables!