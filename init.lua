--- init.lua
--- Author: dousha
--- init.lua is a component of Minecraft ComputerCraft Community Software
--- Distribution (MCCCCSD), licensed under GPLv3.
--- This file is designed to depoly a general file structure like Linux.
---
--- Note: this script is for CraftOS of ComputerCraft, it is NOT compatible 
--- with general Lua interpreters.

local rootList = {"home", "lib", "etc"} --> dir.s need to be created
--- home : user directory
--- lib  : libraries
--- etc  : configurations
local fsMode = {} --> checking result setted by checkFS()

function checkFS() --> void
	for i = 1, #(rootList) do
		fsMode[rootList[i]] = fs.exists(rootList[i])
	end
end


function init() --> bool, but never used
	print("This script will deploy a Linux-like file structure")
	print("in current working directory.")
	print("If you want to install it globally, please run this")
	print("file in the root directory.")
	print("Press <Enter> to start deployment. Or hold <Ctrl>-<T>")
	print("to cancel.")
	read()
	print("Checking the file system")
	if(fs.isReadOnly(".")) then
		print("Permission denied.")
		print("Please run this script in a WRITEABLE folder")
		print("Script will now exit.")
		return false
	end
	checkFS()
	for i = 1, #(fsMode) do
		if(!fsMode[i]) then
			print("Depolying " + rootList[i])
			fs.makeDir(rootList[i])
		end
	end
	print("Depolyment success")
	return true
end

---- main

init()

