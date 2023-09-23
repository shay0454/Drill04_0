from pico2d import *
open_canvas()
os.chdir('c:\\github\\2Dprogramming\\Drill04')
ch1=load_image('moving_character.png')
ch1_size=[137,137]
ch1_frame,ch1_per=24,[6,6,6,6]
ch=load_image('character_v2.png')
ch_size=[32,32]
ch_frame,ch_per=[13,8],[13,8,10,10,10,6,4,7]
x,y=400,300
frame,frame_per=0,0
while(True):
    clear_canvas()
    width,height=ch_size
    ch.clip_draw((frame%ch_frame[0])*ch_size[0],(frame//ch_frame[0])*ch_size[1],width,height,x,y)
    if((frame)%13-1==ch_per[frame_per]-1):
        frame+=13-ch_per[frame_per]
        frame_per=(frame_per+1)%len(ch_per)
    frame=(frame+1)%(ch_frame[0]*ch_frame[1])
    print(frame)
    update_canvas()
    delay(0.1)
    get_events()
close_canvas()