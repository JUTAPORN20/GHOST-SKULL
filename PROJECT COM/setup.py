import cx_Freeze

executables = [cx_Freeze.Executable("PROJECT_GAME.py")]
packages= ["pygame"]
cx_Freeze.setup(
    name='GHOST SKULL',
    version = "1.0",
    description = "My Game Project",
    author= 'Juthaporn',
    executables = executables
    )
