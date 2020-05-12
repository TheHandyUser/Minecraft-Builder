from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import mcpi.minecraft as minecraft
import mcpi.block as blocks

if __name__ == "__main__":
    def createHouse(log):
        mc = minecraft.Minecraft.create()
        x, y, z = mc.player.getPos()

        log.delete(1.0, END)

        log.insert(END, "House builder ready.\n")
        log.insert(END, "Your Location: " + str(x) + ", " + str(y) + ", " + str(z) + "\n")

        log.insert(END, "Clearing The Area...\n")
        mc.setBlocks(x, y, z, x+16, y+16, z+16, blocks.AIR)
        mc.setBlocks(x, y, z, x+16, y, z+16, blocks.GRASS)

        log.insert(END, "Making The Walls...\n")
        mc.setBlocks(x+4, y, z+4, x+12, y+5, z+12, blocks.WOOD_PLANKS)
        mc.setBlocks(x+5, y , z+5, x+11, y+5, z+11, blocks.AIR)

        log.insert(END, "Creating The Base...\n")
        #mc.setBlocks(x+4, y, z+4, x+12, y, z+12, blocks.WOOD_PLANKS)
        #mc.setBlocks(x+5, y+1, z+5, x+11, y+1, z+11, blocks.CARPET_ORANGE)
        mc.setBlocks(x+4, y, z+4, x+12, y, z+12, blocks.WOOD_PLANKS)
        mc.setBlocks(x+5, y, z+5, x+11, y, z+11, blocks.WOOL)
        mc.setBlock(x+8, y, z+8, blocks.GLOWSTONE_BLOCK)
        mc.setBlock(x+11, y, z+11, blocks.GLOWSTONE_BLOCK)
        mc.setBlock(x+11, y, z+5, blocks.GLOWSTONE_BLOCK)
        mc.setBlock(x+5, y, z+5, blocks.GLOWSTONE_BLOCK)
        mc.setBlock(x+5, y, z+11, blocks.GLOWSTONE_BLOCK)

        log.insert(END, "Making Support Structures...\n")
        mc.setBlocks(x+4, y, z+4, x+4, y+5, z+4,blocks.WOOD)
        mc.setBlocks(x+12, y, z+12, x+12, y+5, z+12,blocks.WOOD)
        mc.setBlocks(x+4, y, z+12, x+4, y+5, z+12,blocks.WOOD)
        mc.setBlocks(x+12, y, z+4, x+12, y+5, z+4,blocks.WOOD)

        log.insert(END, "Creating Windows...\n")
        mc.setBlocks(x+6, y+2, z+4, x+10, y+3, z+4, blocks.GLASS)
        mc.setBlocks(x+6, y+2, z+12, x+10, y+3, z+12, blocks.GLASS)
        mc.setBlocks(x+4, y+1, z+8, x+4, y+2, z+8, blocks.AIR)
        #mc.setBlock(x+4, y+1, z+8, blocks.DOOR_IRON)
        mc.setBlocks(x+4, y+1, z+8, x+4, y+2, z+8, blocks.DOOR_WOOD)

        log.insert(END, "Creating The Top...\n")
        #mc.setBlocks(x+4, y+5, z+4, x+12, y+5, z+12, blocks.QUARTZ_BLOCK)
        mc.setBlocks(x+3, y+5, z+3, x+13, y+5, z+13, blocks.STONE)
        mc.setBlocks(x+4, y+6, z+4, x+12, y+6, z+12, blocks.STONE)
        mc.setBlocks(x+5, y+7, z+5, x+11, y+7, z+11, blocks.STONE)
        mc.setBlocks(x+6, y+8, z+6, x+10, y+8, z+10, blocks.STONE)
        mc.setBlocks(x+7, y+9, z+7, x+9, y+9, z+9, blocks.STONE)
        mc.setBlocks(x+4, y+5, z+4, x+12, y+5, z+12, blocks.AIR)
        mc.setBlocks(x+5, y+6, z+5, x+11, y+6, z+11, blocks.AIR)
        mc.setBlocks(x+6, y+7, z+6, x+10, y+7, z+10, blocks.AIR)
        mc.setBlocks(x+7, y+8, z+7, x+9, y+8, z+9, blocks.AIR)
        mc.setBlocks(x+7,y+5,z+9,x+9,y+5,z+7, blocks.GLOWSTONE_BLOCK)
        mc.setBlocks(x+7,y+6,z+9,x+9,y+6,z+7, blocks.FENCE)
        mc.setBlocks(x+8,y+7,z+8,x+8,y+8,z+8, blocks.FENCE)
        mc.setBlocks(x+7,y+5,z+7,x+7,y+7,z+7, blocks.AIR)
        mc.setBlocks(x+9,y+5,z+9,x+9,y+7,z+9, blocks.AIR)
        mc.setBlocks(x+7,y+5,z+9,x+7,y+7,z+9, blocks.AIR)
        mc.setBlocks(x+9,y+5,z+7,x+9,y+7,z+7, blocks.AIR)
    

    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("ubuntu")
    root.title("House Creator")

    log = Text(root, width='40', height='10')
    btn = ttk.Button(root, text="Build House", command=lambda: createHouse(log))
    span = Label(root)
    span2 = Label(root)
    span3 = Label(root)
    progress = ttk.Progressbar(root, orient=HORIZONTAL, mode="indeterminate", length=320)

    span.pack()
    btn.pack(anchor=CENTER)
    span2.pack()
    log.pack()
    span3.pack()
    progress.pack()

    progress.start(30)

    root.mainloop()
else:
    print("This is not a module.")