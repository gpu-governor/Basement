#### Measuring the Standard Screen
I f you’re going to be moving the cursor around, it helps to
know the dimensions of your terminal screen. Not every terminal is going to
be exactly like yours, and it’s an especially bad thing to assume that all termi-
nals follow the dimensions of the standard PC text screen’s 25 rows by 80
columns.
#### The Size of the Window Is Y by X
To discover the size of any window in NCurses, the following function can be
used:
`getmaxyx(win,y,x)`
The getmaxyx() function returns the dimensions of the window win in
rows and columns, where y is the row and x is the column. That the function
is named getmaxyx() should help you remember that Y, or rows, comes first.
The win argument is the name of a specific window in NCurses. For the ter-
minal screen, you use the standard screen window, which is named stdscr.
The y and x arguments are int variables (not pointers) that will hold 
the maximum number of rows and columns in the named window

```screensize.c
1 #include <ncurses.h>
2
3 int main(void)
4 {
5 int x,y;
6 
7 initscr();
8 
9 getmaxyx(stdscr,y,x);
10 printw(“Window size is %d rows, %d columns.\n”,y,x);
11 refresh();
12 getch();
13
14 endwin();
15 return 0;
16 }
```
Here’s what I see for output:
```Windows size is 24 rows, 80 columns.
```
That’s my terminal window’s size; yours may be different. Because my terminal window is in a graphical window in a GUI, I can resize it. When I do and
make the window wider, rerunning the program reports the new results:
```Windows size is 24 rows, 85 columns. ```
The point here is to remember that it’s a bad thing to guess the terminal’s
size. Write your code so that your program uses `getmaxyx()` to determine
the screen size and save those values in variables; do not use constants!