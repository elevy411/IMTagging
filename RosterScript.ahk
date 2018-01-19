^!i::

mS = C:\Users\Admin\Desktop\IM Rosters\
mF = .txt

A = CoedFrisbee
B = MenFrisbee
C = CoedSoccer
D = MenSoccer
E = WaterPolo
F = CoedHockey
G = MenHockey
H = Coed16
I = Men16
K = Men12
L = Playoffs Both
M = Playoffs 0
N = Playoffs 1
O = Playoffs 2



Gui, Add, DropDownList, vrosterChoice, |%A%|%B%|%C%|%D%|%E%|%F%|%G%|%H%|%I%|%K%||%L%||%M%||%N%||%O%||
Gui, Add, Button, default, OK
Gui, Show
return

ButtonOK:
	Gui, Submit
	selection :=  mS . rosterChoice . mF

	;MsgBox % selection

	Ros := Object()
	Loop, read, %selection%
	{
		Ros.Insert(A_LoopReadLine)
	}
	for index, element in Ros
	{
		Send % "@" . element
		Sleep 500
		Send % "{enter}"
		Sleep 500
		Send % " "
	}
ExitApp
return

;sourceFile = %mS%%rosterChoice%%mF%

;MsgBox % sourceFile

GuiEscape:
GuiClose:
	ExitApp
