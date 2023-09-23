from pico2d import *
open_canvas()
os.chdir('c:\\github\\2Dprogramming\\Drill04')
character=load_image('moving_character.png')
x,y=400,300
frame=0
while(True):
    clear_canvas()
    character.clip_draw((frame%6)*137+1,(frame//6)*137,135,135,x,y)
    frame=(frame+1)%24
    print(frame)
    update_canvas()
    delay(0.1)
    get_events()
close_canvas()