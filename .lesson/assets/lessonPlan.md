# Exercise 01: Creating Command Line Menus

## Learning Objectives
1. Students will understand how to use `while`, `print` and `input` to construct a simple menu interface.
2. Students will use *selection* and *subroutines* to direct the flow of the code
3. Students will apply libraries to improve the User Experience (UX)
4. Students will have an understanding of using the `pass` code to create placeholder elements in code

## Overview
This entire session should take around an hour to deliver, the ideal methodology would be to get students to implement each chunk of code, making sure to run and test them. Discussing what works, what doesn't and thinking about how an end user with little technical skill would feel about using this program.

Students should be directed through each subheading, with some focus being given to the additions to the code at each stage. It would be beneficial to break down and reiterate the commands being brought in and the techniques being discussed.

Once each subheading has been discussed set students the task, this should take most students between 20-30 minutes to ensure that all the fiddly detail is fully implemented. A good extension would be to ask students that have completed the work to research how to change text colour in the terminal *only* using the standard library.

Remember, the point of this lesson is to demonstrate to student how the skills they know and love can be used to create an effective user interface without them having planned much further ahead than this. It is also an opportunity to teach them how menus and interfaces worked before the GUI and would combine well with the UI aspect of the Operating System theory work.

## Delivering the content in class

1. **Jump in the Delorean** (15 minutes) Demonstrate menu based user interfaces with the students, model the development of the initial code and explain how the skills learned previously are being used to support a straightforward menu system. Allow the students time to build the code.


2. **If statements for the Win** (15 minutes) Model the build of the if statements, paying particular attention to writing blind-calls for subroutines that have not yet been defined and why that's important. Take some time to justify the final else and why it's important to have an error message that is clear. Allow the students time to build the code.


3. **Using the Time and OS Libraries for Niceness** (15 minutes) Model the build, ensuring that you discuss why it's important to import libraries at the start of the code rather than in the body. Demonstrate what happens without `time.sleep(1)` and why that's problematic. Make some effort to develop an understanding in your students that 1 second of pausing execution *feels* longer and that they need to test their software to ensure the waiting isn't excrutiating. Allow the students time to build the code.

4. **Subroutines Make it Simpler to Plan** (15 minutes) Explain why it is difficult to write subroutines and loops as placeholders - remember that Python does not like constructs without meaningful code in their bodies. Discuss the benefit of using the `pass` command and how this allows students to build structure without having to think too far ahead. Allow the students time to build the code.

5. **Extend and Improve** (Guidance: 10 Minutes) Ask students to attempt to improve or extend the code, this could include more menu options, actually writing code in the subroutines, etc.