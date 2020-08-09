from gl import Render, color, V2, V3
from obj import Obj, Texture

from shaders import *

r = Render(1000,1000)

r.active_texture = Texture('./models/model.bmp')
#r.active_texture2 = Texture('./models/earthNight.bmp')

r.active_shader = prdominantColor

luz = V3(1,0,1)
r.light = luz / np.linalg.norm(luz)

r.loadModel('./models/model.obj', V3(500,500,0), V3(300,300,300))

r.glFinish('output.bmp')


