-- I relly wanna get a better editor
-- CCI package manager
-- ----------
-- Author: dousha@github.com
-- Usage: cci ...
-- License: GPL v3
-- ----------

-- ---- Public variables ----
repoFilePath = "./repo.list"
packageFilePath = "./pdb.list"
packageDbPath = "./lpdb.list"
argv = {...}
-- ---- ----

function printUsage() -- return void
	print("cci - ComputerCraft Installation Package Manager")
	print("Usages:")
	print("    cci [-aidhlrs][-Li] ...")
	print("    cci [-h]")
	print("        Display this help info")
	print("    cci -l")
	print("        List installed packages")
	print("    cci -[a|d][r] <name> <uri> [protocol=http]")
	print("        Add or delete a repo")
	print("    cci -[ai|d] <name>")
	print("        Install or remove a package")
	print("    cci -r repoName=all ...")
	print("        Refresh package list. By default, it refreshs all of available repos")
	print("    cci -Li <path>")
	print("        Install a package from local drive")
	print("    cci -s <name> repoName=all ...")
	print("        Search for a package. By default, it searchs all of available repos")
	print("For further details, read the man page of cci")
end

function split(src, separator) -- return table
	local nFindStartIndex = 1
	local nSplitIndex = 1
	local nSplitArray = {}
	while true do
		local nFindLastIndex = string.find(src, separator, nFindStartIndex)
		if not nFindLastIndex then
			nSplitArray[nSplitIndex] = string.sub(src, nFindStartIndex, string.len(src))
			break
		end
		nSplitArray[nSplitIndex] = string.sub(src, nFindStartIndex, nFindLastIndex - 1)
		nFindStartIndex = nFindLastIndex + string.len(separator)
		nSplitIndex = nSplitIndex + 1
	end
	return nSplitArray
end

function serializeRepoString(name, addr, isEnabled, protocol) -- return string
	return (name .. ":" .. addr .. ":" .. isEnabled .. ":" .. protocol)
end

function serializeRepoStringT(T) -- return string
	return serializeRepoString(T[1], T[2], T[3], T[4])
end

function readRepo() -- return table
	-- repository list will be stored in /disk/repo.list
	-- in this format
	-- name:uri:isEnabled:protocol
	-- e.g.:
	-- a repo via Internet with HTTP protocol
	-- example:http://www.example.com/repo.list:true:http
	-- a repo via Rednet with rednetPkg protocol (not recommended)
	-- rednet:hostname:true:rednetPkg
	
	if fs.exists(repoFilePath) then
		fileHandler = fs.open(repoFilePath)
		if fileHandler == nil then
			fileHandler.close()
			print("[X] Cannot open ./repo.list!: Permission denied")
			return nil
		end
		local curLine = ""
		local curTable = {}
		local totalTable = {}
		for i, curLine in fileHandler.lines() do
			curTable = split(curLine, ":")
			totalTable[i] = curTable
		end
		fileHandler.close()
		return totalTable
	else
		print("[X] Cannot open ./repo.list!: File not found")
		print("[i] You can try `cci -ar repoName repoURI repoProtocol=http'")
		return nil
	end
end

function saveRepo(repoTable) -- return void
	fileHandler = fs.open(repoFilePath, "w")
	curSerializedLine = ""
	for i, v in repoTable do
		curSerializedLine = serializeRepoStringT(v)
		fs.writeLine(curSerializedLine)
	end
	fileHandler.close()
end

function deleteRepo(repoName) -- return void
	fileHandler = fs.open(repoFilePath, "w")
	curSerializedLine = ""
	for i, v in fileHandler.lines() do
		if v[1] ~= repoName then
			
		end
	end
end

function serializePackageString(name, version, size, hash) -- return string
	return (name .. ":" .. version .. ":" .. size .. ":" hash)
end

function serializePackageStringT(T) -- return string
	return serializePackageString(T[1], T[2], T[3], T[4])
end

function readPackageList() -- return table
	-- package list will be stored in /disk/pdb.list
	-- in this format
	-- packageName:version:size(byte):md5checksum16
	-- e.g.:
	-- package:0.0.1:1700:4FBA0258E0C56300
	
	if fs.exists(packageFilePath) then
		curTable = {}
		curLine = ""
		totalTable = {}
		i = 1
		fileHandler = fs.open(packageFilePath, "r")
		if fileHandler == nil then
			print("[X] Cannot open ./pdb.list: Permission denied")
		end
		for curLine in fileHandler.lines() do
			curTable = split(curLine)
			totalTable[i] = curTable
			i = i + 1
		end
		fileHandler.close()
		return totalTable
	else
		print("[X] Cannot open ./pdb.list")
		print("[i] You should execute `cci -r' first to create")
		print("this file.")
		return nil
	end
end

function savePackageList(packageTable)
	fileHandler = fs.open(packageFilePath, "w")
	curDeserializedLine = ""
	for i, v in packageTable do
		curSerializedLine = serializePackageStringT(v)
		fileHandler.writeLine(curSerializedLine)
	end
	fileHandler.close()
end

function readPackageDb()

end

function appendPackageDb(str)

end

function modifyPackageStatus()

end

function searchPackage(name) -- return table
	local packageList = readPackageList()
	local matchList = {}
	local j = 1
	if packageList == nil then
		return nil -- warning is given
	else
		for i, v in packageList do
			local deserializedPakageList = split(v, ":")
			if _, string.find(v[1], name) > 0 then
				matchList[j] = v[1]
				j = j + 1
			end
		end
		if #matchList > 0 then
			for u, w in matchList do
				print()
			end
		else
		
		end
	end
end

function installPackage(path) -- return boolean

end

function removePackage(path) -- return boolean

end

-- @Deprecated
function refreshListViaRednet(hostname) -- return boolean
	-- Seriously, I don't know why I've done this
	
end

function refreshListViaInternet(uri) -- return boolean

end

function refreshList(serializedRepoString) -- return boolean
	local serializedRepoTable = split(serializedRepoString, ":")
	if serializedRepoTable[3] == true then
		if serializedRepoTable[4] == "http" then
			local result = refreshListViaInternet(serializedRepoTable[2])
		elseif serializedRepoTable[4] == "rednetPkg" then
			local result = refreshListViaRednet(serializedRepoTable[2])
		else
			local result = false
			print("[!] Repository " .. serializedRepoTable[1] .. " has invalid protocol! Ignoring.")
		end
		if result == false then
			print("[X] Error occurred When refreshing repository " .. serializedRepoTable[1] .. "!")
		end
	end
end

function refreshListAll() -- return void
	local repoList = readLocalPackageList()
	if repoList == nil then
		return -- warning is given
	else
		for i, v in repoList do
			refreshList(v)
		end
	end
end

function getPackage(name) -- return boolean

end

function makePackage() -- return boolean
	-- generally, just put everything and it's dependencies
	-- into one directory, like what mac does!
	-- but, wait, there's only a dependencies list in the package
	-- won't be some real files
	
end

-- ---- Main area ----
if #argv < 1 then
	printUsage()
	return
else
	if argv[1] == "-h" then
		printUsage()
	elseif argv[1] == "-ar" then
		if #argv == 3 then
			-- by default, protocol is http
			local repoList = readRepo()
			if repoList == nil then
				return -- warning is given when calling function
			else
				local oldRepoSize = #repoList
				convertedString = argv[2] .. ":" .. argv[3] .. ":http"
				repoList[oldRepoSize + 1] = convertedString
				assert(oldRepoSize >= #repoList, "[X] Magika!")
			end
		elseif #argv == 4 then
			-- deprecated, though
			local repoList = readRepo()
			if repoList == nil then
				return -- warning is given when calling function
			else
				local oldRepoSize = #repoList
				convertedString = argv[2] .. ":" .. argv[3] .. ":" .. argv[4]
				repoList[oldRepoSize + 1] = convertedString
				assert(oldRepoSize >= #repoList, "[X] Magika!")
			end
		else
			print("cci -ar <name> <uri> <protocol=http>")
			print("Did you forget something?")
		end
	elseif argv[1] == "-dr" then
		deleteRepo(argv[2])
	elseif argv[1] == "-a" or argv[1] == "-i" then
		local upperBound = #argv
		local i = 2
		while i < upperBound do
			installPackage(argv[i])
			i = i + 1
		end
	elseif argv[1] == "-d" then
		local upperBound = #argv
		local i = 2
		while i < upperBound do
			removePackage(argv[i])
			i = i + 1
		end
	elseif argv[1] == "-Li" then
		
	elseif argv[1] == "-r" then
		if #argv == 1 then
			local result = refreshListAll()
		else
			
		end
	elseif argv[1] == "-s" then
		if #argv > 2 then
			print("[!] Sorry, but I can only search ONE package for one time")
		else
			searchPackage(argv[2])
		end
	else
		printUsage()
	end
end
