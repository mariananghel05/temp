# temp
xwininfo -name [nume[Astronomie] - show window info exist one with nume
xwininfo -root - show info about root window
xwininfo -children [id] shows window childrens

xdotool - for usingit

grep -o = only matching 
                      name            only matching   just first line

ex : xwininfo -name Astronomie | grep -o 0x[0-9]* | head -1


1::
a:=Clipboard, Clipboard="I see genie"	;save your current clipboard to a variable and set the clipboard to text
Send, ^v	;paste
Clipboard:=a	;restore original clipboard
Return
