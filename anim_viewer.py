from pico2d import *
open_canvas()
os.chdir('c:\\github\\2Dprogramming\\Drill04')
character=load_image('moving_character.png')
x,y=400,300
frame=0
while(True):
    clear_canvas()
    character.clip_draw(frame*137+1,0,135,135,x,y)
    frame=(frame+1)%6
    update_canvas()
    get_events()
close_canvas()