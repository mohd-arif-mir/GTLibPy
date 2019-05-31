"""IGI 1 Trainer in Python using GTLibPy module.
Features.
Unlimited Health,ammo and clips."""
from GT_LibPy import *

#Get clips static address.
def GetClipsAddress():
	clips_static_pointer = 0x00671890
	clips_addr_off = [0x0,0x4C4] 
	game_base_address = GT_GetGameBaseAddress(GT_GetProcessID())
	clips_base_pointer = GT_ReadPointerOffset(game_base_address,clips_static_pointer)
	clips_address = GT_ReadPointerOffsets(clips_base_pointer,clips_addr_off,len(clips_addr_off)) + 0x144
	return clips_address

#Get human static address.
def GetHumanBaseAddress(game_base_address):
    human_static_pointer = 0x0016E210;
    human_address_offsets = [0x8,0x7CC,0x14];

    human_base_pointer = GT_ReadPointerOffset(game_base_address,human_static_pointer);
    human_base_address = GT_ReadPointerOffsets(human_base_pointer,human_address_offsets,len(human_address_offsets)) + 0x348;

    return human_base_address

#Set unlimited ammo.
def SetAmmo(game_base_address):
	unlimited_ammo = 0x7FFFFFFF
	weapon_base_address = GetHumanBaseAddress(game_base_address)	
	weapons_offsets = [0x0,0xC,0x18,0x24,0x30,0x3C,0x48,0x54,0x60,0x6C]
	if GT_WriteAddressOffsets(weapon_base_address,weapons_offsets,len(weapons_offsets),unlimited_ammo):
		print("[+]Unlimited ammo enabled")

#Set unlimited clips.
def SetClips(game_base_address):
	unlimited_clips = 0xFFFFFF
	clips_address = GetClipsAddress()
	if GT_WriteAddress(clips_address,unlimited_clips):
		print("[+]Unlimited clips enabled")

#Set unlimited health.
def SetHealth(game_base_address):
    unlimited_health = 0xFFFFFFFF
    health_address = GetHumanBaseAddress(game_base_address) - 0xF4
    if GT_WriteAddress(health_address,unlimited_health):
        print("[+]unlimited health enabled")

#Main method
def main():	
	print("IGI Trainer +3.")
	print("F1 - Unlimited health")
	print("F2 - Unlimited ammo")
	print("F3 - Unlimited clips")
	print("F5 - Exit")

	try:
		game_name = "IGI"
		handle = GT_FindGameProcess(game_name)

		if handle:
			while True:
				pid = GT_GetProcessID()
				game_base_address = GT_GetGameBaseAddress(pid)

				#Hotkeys trainer options.
				if GT_IsKeyToggled(VK_F1):
					SetHealth(game_base_address)
				elif GT_IsKeyToggled(VK_F2):
					SetAmmo(game_base_address)	
				elif GT_IsKeyToggled(VK_F3):
					SetClips(game_base_address)
				elif GT_IsKeyToggled(VK_F5):
					break
		print("Trainer made using GT_LibPy :)")								
	except Exception as ex:
		print("Exception occured : ",ex)		

if __name__ == '__main__':
	main()