from gl import Render, color, V2, V3
from obj import Obj, Texture

from shaders import *

r = Render(1000,1000)

r.active_texture = Texture('./models/model.bmp')
r.active_texture2 = Texture('./models/model.bmp')


luz = V3(0,0,1)
r.light = luz / np.linalg.norm(luz)

r.active_shader = toon

r.loadModel('./models/model.obj', V3(500,500,0), V3(300,300,300))

r.glFinish('output.bmp')

r.glClear()
r.active_shader = invertedSkin

r.loadModel('./models/model.obj', V3(500,500,0), V3(300,300,300))

r.glFinish('output2.bmp')

r.glClear()
r.active_shader = predominantColor

r.loadModel('./models/model.obj', V3(500,500,0), V3(300,300,300))

r.glFinish('outpu3.bmp')








