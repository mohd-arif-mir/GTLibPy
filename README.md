![cover_logo](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/cover_logo.jpg?raw=true "")

_GTLib**Py**_ is **[Game Trainer](https://en.wikipedia.org/wiki/Trainer_(games)) library/module for _Python in windows_** it provides all the necessary methods to make simple game trainer in
windows using **WIN32-API** with ease.
It uses only **WIN32-API** methods because this is intended to work on **Windows** system only
and not shall be portable or to target other OS like **_Linux_,_MAC OS_** etc.

**NOTE** : This ain't memory scanning,hooking,analyzing library, it won't provide methods for scanning/signature or dumping RAW memory.
 
 **UNDERHOOD WORKING** : _GTLib**Py**_ is actually a wrapper module over [GTLibc](https://github.com/haseeb-heaven/GTLibc) which actually does all the work beneath,this module just converts _Python_ **datatypes,data-structures** to _C-Type_ **data** and passes them to **GTLibc** library and shows result afterwards.
So this has all the features which **GTLibc** had _FindGame,ReadAddress,WriteAddress,SetCheatCodes_ etc.

**AIM** : The aim of this library is only to provide the most efficient way of creating game trainer 
and to provide a layer on top of **WIN-32 API** _cumbersome_ methods and to make reading/writing ,finding Game process easier and convenient.

## **_Your support is needed to keep this project alive, Feel free to donate._**
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/haseebmir91)

# Main Components :

## Finding game : 

Using **GT_FindGameProcess()** method.

![finding_game_process](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/finding_game_process.jpg?raw=true "")


Using **GT_FindGameWindow()** method.

![finding_game_window](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/finding_game_window.jpg?raw=true "")


## Reading Values : 

using **GT_ReadAddress()** or **GT_ReadAddressoffset()** methods.

![reading_memory](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/reading_memory.jpg?raw=true "")

## Writing Values : 

using **GT_WriteAddress()** or **GT_WriteAddressOffset()** methods.

![writing_memory](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/writing_memory.jpg?raw=true "")

## Creating Hot-keys :

using **GT_HotKeysPressed()** **_MACRO_** or **GT_IsKeyPressed()/GT_IsKeyToggled()** methods.

![hotkeys](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/hotkeys.jpg?raw=true "")

# Additional Components :

## Applying cheat codes : 

using **GT_SetCheatCode()** method.

![set_cheat_code](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/set_cheat_code.jpg?raw=true "")

## Searching offset area : 

using **GT_SearchOffsetArea()** method.

![search_offset_area](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/search_offset_area.jpg?raw=true "")


## Automation scripting  : 

using **GT_DoMousePress()** and **GT_DoKeyPress()** methods.


# GTLibPy Logs and errors :

## Error/Exception Handling :

All the error/exception handling is done by library itself like if you tried read or write from **Invalid Memory section** or if process id,game handle/HWND are invalid  it will automatically handle error.So you don't have to check for any error by yourself

![game_not_found](https://github.com/haseeb-heaven/GTLibc/blob/master/resources/game_not_found.jpg?raw=true "")


![reading_invalid_memory](https://github.com/haseeb-heaven/GTLibc/blob/master/resources/reading_invalid_memory.jpg?raw=true "")


![writing_invalid_memory](https://github.com/haseeb-heaven/GTLibc/blob/master/resources/writing_invalid_memory.jpg?raw=true "")


## Methods Accessibility :

All **Public** and **Semi-Public** methods are accessible . But **Private** methods are not and library will throw error if you tried to access them.

![private_method_error](https://github.com/haseeb-heaven/GTLibc/blob/master/resources/private_method_error.jpg?raw=true "")

## Library Logs :

Logs are **disabled** by default but if you want library to maintain logs use **GT_EnableLogs()** method to **enable** logs.
or if you want to **disable** logs again you can use **GT_DisableLogs()** method.

![enable_disable_logs](https://github.com/haseeb-heaven/GTLibPy/blob/master/resources/enable_disable_logs.jpg?raw=true "")


# Trainer Demo :
As a demo of this module IGI 1 Trainer is included to show demo of all the **GT**LiPy methods and how to use them in making simple game trainer.

**DOCUMENTATION INFO :**
All Public and Semi-Private methods are well documented.
but private methods are not documented as it was not necessary to do so.

**VERSION INFO :**<br/>
GTLibPy Version : V 1.0<br/>  
Dated : 31/05/2019.<br/>

Written and maintained by HaseeB Mir (haseebmir.hm@gmail.com)
