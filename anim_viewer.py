from pico2d import *
open_canvas()
os.chdir('c:\\github\\2Dprogramming\\Drill04')
ch=load_image('character_v2.png')
ch_size=[32,32] #cilp 크기
ch_frame,ch_nums=[13,8],[7,4,6,10,10,10,8,13] # 시트에서 클립의 최대 가로,세로 개수, 각 세로의 개수
x,y=400,300 #위치
frame,ch_nums_index=0,0 # 본 프레임(하나의 타이머), ch_nums의 값을 쓰기 위한 index 저장 변수
while(True):
    clear_canvas()
    ch.clip_draw((frame%ch_frame[0])*ch_size[0],(frame//ch_frame[0])*ch_size[1],ch_size[0],ch_size[1],x,y)
    frame=(frame+1)%(ch_frame[0]*ch_frame[1])
    if((frame)%ch_frame[0]==ch_nums[ch_nums_index]%ch_frame[0]):
        frame+=ch_frame[0]-ch_nums[ch_nums_index]
        ch_nums_index=(ch_nums_index+1)%len(ch_nums)
    update_canvas()
    delay(0.05)
    get_events()

close_canvas()