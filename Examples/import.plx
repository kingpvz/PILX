/This is an example of importing modules.
/Some features and commands might only be available after certain modules are imported. In this example, we will use the "maths" module to find factorial of the number 5!
/If we try to use an ! operator (factorial operator) before importing, we will get an error. However, after we import it, it will work!
/The syntax for importing the maths module looks like this:
>i maths
/Notice that you can't put ";" on the end of such line, as it would be treated as part of the module's name.
/We import using the insert operator (>)
/To import a module, we use the "i" command, which stands for import.
/Next, we need a space, to divide the command in two parts, in the second part, we write the name of the module we'd like to import.
/Now, let's find the factorial!
+val=5;
+!val;
[out]val;
/And here we are! Simple as that!