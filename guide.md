MCCCC Software Distribution
===========================

Greetings. This repository stores the work of Minecraft ComputerCraft
Community.

---------------------------------------------------------------------

Basic File Structure
--------------------

The file structure of MCCCCSD is like *nix file structure.

```
/
	/lib 	-> libraries			\
	/home	-> user home directory	|- Inherited from *nix
	/etc 	-> configurations		|
	/bin 	-> binaries				/
	/doc 	-> documents			\- Custom structure
	/trash 	-> trash bin			/
```

This file structure would be deployed by `init.lua`.

Shell
-----

The default shell of MCCCCSD is `msh`. It is designed to be a POSIX
compatiable shell.

By default, when shell starts, it would run script which is stored in
`/home/__CURRENT_USER/.mshrc`. the variable `__CURRENT_USER` is set by
`/bin/login`.

Shell would reserves these variables:

* `__PATH` for PATH
* `__CURRENT_USER` for current username
* `__CWD` for current working directory
* `__PWDS` for parent working directories
* `__SHELL_VERSION` for shell version

Package Manager
---------------

The package manager of the system is `cci`.

Package manager would reserves these variables:

* `__PM_REPO_LIST`		-> Repository list
* `__PM_SOFTWARE_LIST`	-> Software list cached in disk
* `__PM_INSTALLED_LIST`	-> A cache from software list for installed packages
* `__PM_LOCKED_LIST`	-> A cache from software list for locked packages
* `__PM_VERSION`		-> for package manager version

"Window" Manager
----------------

The window manager of the system is `x-`. Note that for a normal computer,
it has no color. And for any type of computers in ComputerCraft, it has
no offical graphics interface. Thus this "window" manager only provides
a simple, text based components.

