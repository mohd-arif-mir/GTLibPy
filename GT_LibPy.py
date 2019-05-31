"""
BRIEF : GTLibPy is module to make game trainer in Python it provide all the necessary methods to make simple game trainer in
windows using win32-API with ease.
It uses only WIN32 API methods because this is intended to work on Windows system only
and not shall be portable or to target other OS like Linux,MAC OS etc.
From the beginning of trainer development till end, it provides all necessary methods needed for game trainer.

UNDERHOOD WORKING : GTLibPy is actually a wrapper module over GTLibc which actually does all the work beneath,
this module just converts Python datatypes,data-structures to C-Type data and passes them to GTLibc library and shows result afterwards.
So this has all the features which GTLibc had FindGame,ReadAddress,WriteAddress,SetCheatCodes etc.

*****************************
*******Main components.******
*****************************

1)Finding game --> use GT_FindGameProcess()  or GT_FindGameWindow() method.
2)Reading values Health,XP,Ammos from game --> use GT_ReadAddress() or GT_ReadAddressoffset() methods.
3)Writing values Health,XP,Ammos to  game --> use GT_WriteAddress() or GT_WriteAddressOffset() methods.
4)Creating Hot-keys for trainer --> use GT_HotKeysPressed() MACRO or GT_IsKeyPressed()/GT_IsKeyToggled() methods.

*****************************
****Additional components.***
*****************************

5)Additional Automation of scripting for trainer --> use GT_DoMousePress() and GT_DoKeyPress() methods.
6)Cheat code applying tool included in this module --> use GT_SetCheatCode() method.
7)Offset area searching tool included in this module --> use GT_SearchOffsetArea() method.

***********************************************
****Advanced components for Game Hacking.*****
**********************************************
WILL BE ADDED IN FUTURE VERSIONS.

NOTE : This ain't memory scanning,hooking,analyzing module, it won't provide methods for scanning/signature or dumping RAW memory.

AIM : The aim of this module is only to provide the most efficient way of creating game trainer
and to provide a layer on top of WIN-32 API cumbersome methods and to make reading/writing ,finding Game process easier and convenient.

DOCUMENTATION INFO :
All Public and Semi-Private methods are well documented.
but private methods are not documented as it was not necessary to do so.

VERSION INFO :
GTLIBPY Version : V 1.0

V 1.0 -> Dated : 31/05/2019

Written by Ha5eeB Mir (haseebmir.hm@gmail.com)
"""

#Import ctypes module and load GTLibc library.
from ctypes import *
gtlib = CDLL('GTLibc.so')

#Error messages constants.
INVALID_INPUT__ERR = "Input type is invalid"
EMPTY_INPUT_ERR = "Input is empty"

#Keyboard keys constants.
VK_BACK,VK_TAB,VK_ESCAPE = 0x08,0x09,0x1B
VK_RETURN,VK_CONTROL,VK_MENU = 0x0D,0x11,0x12
VK_CAPITAL,VK_SPACE = 0x14,0x20
VK_SHIFT,VK_LSHIFT,VK_RSHIFT = 0x10,0xA0,0xA1
VK_LCONTROL,VK_RCONTROL = 0xA2,0xA3
VK_LMENU,VK_RMENU = 0xA4,0xA5
VK_LEFT,VK_UP,VK_RIGHT,VK_DOWN = 0x25,0x26,0x27,0x28
VK_F1,VK_F2,VK_F3,VK_F4,VK_F5,VK_F6,VK_F7,VK_F8,VK_F9,VK_F10,VK_F11,VK_F12 = 0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7A,0x7B

#Mouse key constants.
FROM_LEFT_1ST_BUTTON_PRESSED,RIGHTMOST_BUTTON_PRESSED,FROM_LEFT_2ND_BUTTON_PRESSED,FROM_LEFT_3RD_BUTTON_PRESSED,FROM_LEFT_4TH_BUTTON_PRESSED = 0x0001,0x0002,0x0004,0x0008,0x0010 

"""****************************************************************************
************************-PUBLIC-METHODS-***************************************
****************************************************************************"""

"""
 * @description - Find game by process name.
 * @param - Game name in string or bytes format (CASE INSENSTIVE). and without '.exe' extension.
 * @return - If game found it returns HANDLE to game otherwise returns None
 * NOTE : Process name is name of your .exe file loaded in Memory.
"""

def GT_FindGameProcess(game_name):
	game_handle = None
	exe_extension = ".exe"	
	try:
		if type(game_name) != type(str()) and type(game_name) != type(bytes()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(game_name)) + ",Expected : " + str(type(str())))
		elif not game_name:
			raise ValueError(EMPTY_INPUT_ERR)
		elif game_name.find(exe_extension):
			game_name = game_name.replace(exe_extension,"")

		if type(game_name) == type(str()):
			game_name = c_char_p(game_name.encode('UTF-8'))
		game_handle = gtlib.GT_FindGameProcess(game_name)
	except Exception as ex:
		print("Exception occurred in 'GT_FindGameProcess' : ",ex)
	return game_handle	

"""
 * @description - Find game by window name.
 * @param - window name in string or bytes format format (CASE INSENSITIVE).
 * @return - if game window found then it returns HANDLE to that window otherwise returns None
 * NOTE : Windows name is name of your Game Process Window not the .exe file.
"""

def GT_FindGameWindow(window_name):
	game_window = None
	try:
		if type(window_name) != type(str()) and type(window_name) != type(bytes()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(window_name)) + ",Expected : " + str(type(str())))
		elif not window_name:
			raise ValueError(EMPTY_INPUT_ERR)

		if type(window_name) == type(str()):
			window_name = c_char_p(window_name.encode('UTF-8'))			
		game_window = gtlib.GT_FindGameWindow(window_name)
	except Exception as ex:
		print("Exception occurred in 'GT_FindGameWindow' : ",ex)
	return game_window		

"""
 * @description - Read value from provided address.
 * @param - Address from where to read.
 * @return - If read succeeded then it returns pointer to value otherwise returns None.
"""

def GT_ReadAddress(address):
	read_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		
		read_address = gtlib.GT_ReadAddress
		read_address.restype = c_void_p
		read_status = read_address(address)
	except Exception as ex:
		print("Exception occurred in 'GT_ReadAddress' : ",ex)	 
	return read_status

"""
 * @description - Read value from provided address with offset.
 * @param - Address and offset.
 * @return - If read succeeded then it returns pointer to value otherwise returns None.
"""

def GT_ReadAddressOffset(address,offset): 	
	read_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offset) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offset)) + ",Expected : " + str(type(int())))
		read_address_offset = gtlib.GT_ReadAddressOffset
		read_address_offset.restype = c_void_p
		read_status = read_address_offset(address,offset)
	except Exception as ex:
		print("Exception occurred in 'GT_ReadAddressOffset' : ",ex)	 
	return read_status

"""
 * @description - Read value from provided address with provided offsets.
 * @param - Address, offsets and size of offsets.
 * @return - If read succeeded then it returns pointer to list of values otherwise returns None
"""

def GT_ReadAddressOffsets(address,offsets,offsets_len):
	read_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offsets) not in {type(list()),type(set()),type(tuple())}:
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offsets)) + ",Expected : " + str(type(list())))
		elif offsets_len <= 0:
			raise ValueError("Input offsets has invalid length")	
		offsets_array = c_int * offsets_len
		offsets = offsets_array(*offsets)
		read_address_offsets = gtlib.GT_ReadAddressOffsets
		read_address_offsets.argstype = [c_void_p,offsets,offsets_array(*offsets),c_ulong]
		read_address_offsets.restype = POINTER(c_void_p * offsets_len)
		read_status = read_address_offsets(address,offsets,sizeof(offsets))

	except Exception as ex:
		print("Exception occurred in 'GT_ReadAddressOffsets' : ",ex)	 
	return read_status

"""
 * @description - Read pointer's address from provided address with offset.
 * @param - Address and offset
 * @return - If read succeeded then it returns pointer to value otherwise returns None.
"""

def GT_ReadPointerOffset(address,offset):
	read_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offset) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offset)) + ",Expected : " + str(type(int())))
		read_pointer_offset = gtlib.GT_ReadPointerOffset
		read_pointer_offset.restype = c_void_p
		read_status = read_pointer_offset(address,offset)			
	except Exception as ex:
		print("Exception occurred in 'GT_ReadPointerOffset' : ",ex)	 
	return read_status	

"""
 * @description - Read pointer's address from provided address with provided offsets.
 * @param - Address,offsets and size of offsets.
 * @return - If read succeeded then it returns address of pointer otherwise returns None.
"""

def GT_ReadPointerOffsets(address,offsets,offsets_len):
	read_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offsets) not in {type(list()),type(set()),type(tuple())}:
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offsets)) + ",Expected : " + str(type(list())))
		elif offsets_len <= 0:
			raise ValueError("Input offsets has invalid length")
		offsets_array = c_int * offsets_len
		offsets = offsets_array(*offsets)
		read_pointer_offsets = gtlib.GT_ReadPointerOffsets
		read_pointer_offsets.argstype = [c_void_p,offsets_array(*offsets),c_ulong]
		read_pointer_offsets.restype = c_void_p
		read_status = read_pointer_offsets(address,offsets,sizeof(offsets)) 
	except Exception as ex:
		print("Exception occurred in 'GT_ReadPointerOffsets' : ",ex)	 
	return read_status

"""
 * @description - Write value at provided address.
 * @param - Address and value.
 * @return - If write is succeeded then it returns TRUE otherwise returns FALSE
"""

def GT_WriteAddress(address,value):
	write_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		write_status = gtlib.GT_WriteAddress(address,GT_GetValueAddress(value))	
	except Exception as ex:
		print("Exception occurred in 'GT_WriteAddress' : ",ex)	 
	return write_status

"""
 * @description - Write value at provided address with offset.
 * @param - Address,offset and value.
 * @return - If write succeeded then it returns TRUE otherwise returns FALSE.
"""

def GT_WriteAddressOffset(address,offset,value):
	write_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offset) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offset)) + ",Expected : " + str(type(int())))
		write_status = gtlib.GT_WriteAddressOffset(address,offset,GT_GetValueAddress(value))	
	except Exception as ex:
		print("Exception occurred in 'GT_WriteAddressOffset' : ",ex)	 
	return write_status

"""
 * @description - Write value at provided address with provided offsets.
 * @param - Address,offset,length of offsets and value.
 * @return - If write succeeded then it returns TRUE otherwise returns FALSE.
"""

def GT_WriteAddressOffsets(address,offsets,offsets_len,value):
	write_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offsets) not in {type(list()),type(set()),type(tuple())}:
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offsets)) + ",Expected : " + str(type(list())))
		elif offsets_len <= 0:
			raise ValueError("Input offsets has invalid length")

		offsets_array = c_int * offsets_len
		offsets = offsets_array(*offsets)
		write_address_offsets = gtlib.GT_WriteAddressOffsets
		write_address_offsets.argstype = [c_void_p,offsets_array(*offsets),c_ulong,c_void_p]
		write_status = write_address_offsets(address,offsets,sizeof(offsets),GT_GetValueAddress(value))	
	except Exception as ex:
		print("Exception occurred in 'GT_WriteAddressOffsets' : ",ex)	 
	return write_status

"""
 * @description - Write value at pointer's address with offset.
 * @param - Address,offset and value.
 * @return - If write succeeded then it returns TRUE otherwise returns FALSE.
"""

def GT_WritePointerOffset(address,offset,value):
	write_status= None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offset) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offset)) + ",Expected : " + str(type(int())))
		write_status = gtlib.GT_WritePointerOffset(address,offset,GT_GetValueAddress(value))	
	except Exception as ex:
		print("Exception occurred in 'GT_WritePointerOffset' : ",ex)	 
	return write_status

"""
 * @description - Write value at pointer's address with offsets.
 * @param - Address,offsets,length of offsets and value.
 * and Pointer to value to be written.
 * @return - If write succeeded then it returns TRUE otherwise returns FALSE.
"""

def GT_WritePointerOffsets(address,offsets,offsets_len,value):
	write_status = None
	try:
		if type(address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(address)) + ",Expected : " + str(type(int())))
		elif type(offsets) not in {type(list()),type(set()),type(tuple())}:
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offsets)) + ",Expected : " + str(type(list())))
		elif offsets_len <= 0:
			raise ValueError("Input offsets has invalid length")

		offsets_array = c_int * offsets_len
		offsets = offsets_array(*offsets)
		write_pointer_offsets = gtlib.GT_WritePointerOffsets
		write_pointer_offsets.argstype = [c_void_p,offsets_array(*offsets),c_ulong,c_void_p]
		write_status = write_pointer_offsets(address,offsets,sizeof(offsets),GetValueAddress(value))	
	except Exception as ex:
		print("Exception occurred in 'GT_WritePointerOffsets' : ",ex)	 
	return write_status

"""
 * @description - Get base address of current game.
 * @param - Process ID of current game.
 * @return - On success it returns base address of game otherwise returns None.
"""

def GT_GetGameBaseAddress(process_id):
	base_address = None
	try:
		if type(process_id) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(process_id)) + ",Expected : " + str(type(int())))
		base_address = gtlib.GT_GetGameBaseAddress(process_id)	
	except Exception as ex:
		print("Exception occurred in 'GT_GetGameBaseAddress' : ",ex)	 
	return base_address	

"""
 * @description -  Get process ID of game from memory.
 * @return - If game found returns processID of current game otherwise returns None.
"""

def GT_GetProcessID():
 	pid = gtlib.GT_GetProcessID()
 	return pid

"""
 * @description -  Get current game name from memory.
 * @return - If game found returns game name otherwise returns None.
"""

def GT_GetGameName():
	get_game_name = gtlib.GT_GetGameName
	get_game_name.restype = c_char_p
	game_name = get_game_name()
	if game_name:
		game_name = game_name.decode('UTF-8')
	return game_name

"""
 * @description - Get game handle from HWND (handle to window).
 * @param - Handle to current window of game.
 * @return - Handle to process on success otherwise returns None.
 * NOTE : HANDLE is handle to Game's process and HWND is handle to Game's window.
"""

def GT_GetGameHandle4mHWND(hwnd):
	game_handle = None
	try:
		if type(hwnd) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(hwnd)) + ",Expected : " + str(type(int())))
		game_handle = gtlib.GT_GetGameHandle4mHWND(hwnd)	
	except Exception as ex:
		print("Exception occurred in 'GT_GetGameHandle4mHWND' : ",ex)	 
	return game_handle

"""
 * @description - Get processID of game from HWND (handle to window).
 * @param - Handle to current window of game.
 * @return - On success it returns game's process ID otherwise returns None.
 * NOTE : HANDLE is handle to Game's process and HWND is handle to Game's window.
"""

def GT_GetProcessID4mHWND(hwnd):
	pid = None
	try:
		if type(hwnd) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(hwnd)) + ",Expected : " + str(type(int())))
		pid = gtlib.GT_GetProcessID4mHWND(hwnd)
	except Exception as ex:
		print("Exception occurred in 'GT_GetGameHandle4mHWND' : ",ex)	 
	return pid

"""
 * INFO : Hot keys can be in combination of like GT_HotKeysDown(VK_CONTROL,VK_F1) or GT_HotKeysDown(LSHIFT,'F')
 * @description - check for Hot keys combinations pressed or not.
 * @param - Combination of hot keys using virtual key_codes or characters A-Z,a-z.
 * @return - If keys pressed it will return TRUE otherwise returns FALSE.
"""

def GT_HotKeysPressed(*keys_list):
	keys_limit = 10 #Limit upto 10 Hotkeys.
	keys = ["key%d"%x for x in range(keys_limit)]
	for x in range(keys_limit):
		keys[x] = keys_list[x] if x < len(keys_list) else 0
	return gtlib.GT_HotKeysDown(keys[0],keys[1],keys[2],keys[3],keys[4],keys[5],keys[6],keys[7],keys[8],keys[9],0x0)	

"""
 * @description - Check if provided key is pressed or not.
 * @param - virtual key_code. ex : (VK_SHIFT).
 * @return - If key is pressed it returns TRUE otherwise returns FALSE.
 * NOTE : This method must be in main game running loop or any continuous loop.
"""

def GT_IsKeyPressed(key):
	key_state = gtlib.GT_IsKeyPressed(key)
	return key_state

"""
 * @description - Check if provided key is toggled or not.
 * @param - virtual key_code. ex : (VK_SHIFT).
 * @return - If key is toggled it returns TRUE otherwise returns FALSE.
 * NOTE : This method must be in main game running loop or any continuous loop.
"""

def GT_IsKeyToggled(key):
	key_state = gtlib.GT_IsKeyToggled(key)
	return key_state

"""****************************************************************************
*******************-SEMI-PRIVATE-METHODS-**************************************
****************************************************************************"""

"""
 * INFO : Send Mouse input to current game.
 * @description - Send mouse input control to game.
 * @param - mouse code in INT format. ex : use these pre-defined macros FROM_LEFT_1ST_BUTTON_PRESSED or RIGHTMOST_BUTTON_PRESSED.
 * NOTE : This will be useful if you want to create some automated scripting for your game.
 """

def GT_DoMousePress(mouse_code):
	gtlib.GT_DoMousePress(mouse_code)

"""
 * INFO : Send Keyboard input to current game.
 * @description - Send keyboard input control to game.
 * @param - Virtual key_code in INT format. ex : VK_CONTROL,VK_SHIFT. (see 'https://docs.microsoft.com/en-us/windows/desktop/inputdev/virtual-key-codes' for full list of Key codes.)
 * NOTE : This will be useful if you want to create some automated scripting for your game.
"""

def GT_DoKeyPress(key_code):
	gtlib.GT_DoKeyPress(key_code)

"""
 * @description - Apply provided cheat code to current game.
 * @param - cheat code in string format.
"""
def GT_SetCheatCode(cheat_code):
	try:
		if type(cheat_code) != type(str()) and cheat_code != type(bytes()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(cheat_code)) + ",Expected : " + str(type(str())))
		elif not cheat_code:
			raise ValueError(EMPTY_INPUT_ERR)

		if type(cheat_code) == type(str()):
			cheat_code = c_char_p(cheat_code.encode('UTF-8'))			
		gtlib.GT_SetCheatCode(cheat_code)
	except Exception as ex:
		print("Exception occurred in 'GT_SetCheatCode' : ",ex)

"""
 * INFO : Search any value in current offset i.e. (base_address + offset) for finding new heath/ammos/weapons in game.
 * @description -  Search value in offset area.
 * @param - base address of Ammo/health/clips,offset limit,offset size and value for searching.
 * @return - If value found it returns its address and offset in formatted string otherwise returns None
"""

def GT_SearchOffsetArea(base_address,offset_limit,offset_size,offset_value):
	search_status = ""
	try:
		if type(base_address) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(base_address)) + ",Expected : " + str(type(int())))
		elif  type(offset_limit) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offset_limit)) + ",Expected : " + str(type(int())))
		elif  type(offset_size) != type(int()):
			raise TypeError(INVALID_INPUT__ERR + " " + str(type(offset_size)) + ",Expected : " + str(type(int())))
		elif offset_size <= 0:
			raise ValueError("Input offset size must be greater than 1") 
		search_offset = gtlib.GT_SearchOffsetArea
		search_offset.restype = c_char_p
		search_status = gtlib.GT_SearchOffsetArea(base_address,offset_limit,offset_size,offset_value)	
	except Exception as ex:
		print("Exception occurred in 'GT_SearchOffsetArea' : ",ex)	 
	return search_status	

"""
 * @description - Get Handle to current game's process.
 * @return - If game found it return Handle to current game's process otherwise returns None.
"""

def GT_GetGameHandle():
	game_handle = gtlib.GT_GetGameHandle()
	return game_handle

"""
 * @description - Get Handle to current game's window.
 * @return - If game found it return Handle to current game's windows otherwise returns None.
"""

def GT_GetGameHWND():
	game_window = gtlib.GT_GetGameHWND()
	return game_window

"""
 * INFO : Whether library should maintain logs internally (enable this if you want this feature).
 * @description - Enable logs in library.
 * @return - Returns TRUE if enabled is success otherwise returns FALSE.
"""

def GT_EnableLogs():
	log_status = gtlib.GT_EnableLogs()
	return log_status

"""
 * @description - Disable logs in library.
 * @return - Returns TRUE if disable is success otherwise returns FALSE.
"""

def GT_DisableLogs():
	log_status = gtlib.GT_DisableLogs()
	return log_status

"""****************************************************************************
************************-PRIVATE-METHODS-**************************************
****************************************************************************"""
#Private Helper method to dereference value from any datatype.
def GT_Dereference(addr,c_typ):
	assert(type(addr) == type(int())),"GT_Dereference : address is invalid"
	deref_value = c_char_p(addr).value if c_typ == c_char_p else cast(addr,POINTER(c_typ))[0]
	return deref_value

#Private helper method to get address of value.
def GT_GetValueAddress(value):
	value_address = 0x00000000
	assert(value),"GT_GetValueAddress : value is none"
	if type(value) == type(str()):
		value_address = c_char_p(value.encode('UTF-8'))
	elif type(value) == type(int()):
		value = c_int(value)
	elif type(value) == type(float()):
		value = c_float(value)

	if not value_address:	
		value_address = c_void_p(addressof(value))
	return value_address