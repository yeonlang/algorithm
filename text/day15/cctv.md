``` c
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int N,M;
int my_map[8][8];
int map_origin[8][8];
int dir = 0;
int dy[4]={-1,0,1,0};
int dx[4]={0,1,0,-1};//상,우,하,좌

int minmin = 98765;
vector<int> A;
map<int, int> DB;
vector<struct camera_info> camera_stack;

struct camera_info{
    int x=0;
    int y=0;
    int camera_num = 0;
};

bool map_recovery()
{
    for(int y=0;y<8;y++)
        for(int x=0;x<8;x++)
        {
            my_map[y][x]=map_origin[y][x];
        }
    return true;
}

int CCTV_CHECK()
{
    int safe_count = 0;
    for(int y=0;y<N;y++)
        for (int x =0;x<M;x++)
        {
            if (my_map[y][x]==0)
            {
                safe_count=safe_count+1;
            }
        }
    return safe_count;

}
bool is_safe(int y,int x)
{
    if (x>-1 && y>-1 && y<N && x<M)
    {
        if (my_map[y][x]!=6)
            return true;
        else
            return false;
    }
    else
        return false;
}

bool camera1(int act_num,int x,int y)
{
    if(act_num==1)//상
    {
        dir = 0;
        my_map[y][x] = -1;
        if(is_safe(y+dy[dir],x+dx[dir]))
        {
            camera1(act_num,x+dx[dir],y+dy[dir]);
            return true;
        }   
        else
            return false;
    }
    if(act_num==2)//우
    {
        dir = 1;
        my_map[y][x] = -1;
        if(is_safe(y+dy[dir],x+dx[dir]))
        {
            camera1(act_num,x+dx[dir],y+dy[dir]);
            return true;
        }
        else
            return false;
    }
    if(act_num==3)//하
    {
        dir = 2;
        my_map[y][x] = -1;
        if(is_safe(y+dy[dir],x+dx[dir]))
        {
            camera1(act_num,x+dx[dir],y+dy[dir]);
            return true;
        }
        else
            return false;
    }
    if(act_num==4)//좌
    {
        dir = 3;
        my_map[y][x] = -1;
        if(is_safe(y+dy[dir],x+dx[dir]))
        {
            camera1(act_num,x+dx[dir],y+dy[dir]);
            return true;
        }
        else
            return false;
    }
    else
        return false;
    
}

bool camera2(int act_num,int x,int y)
{
    if(act_num==1)//상하
    {
        camera1(1,x,y);
        camera1(3,x,y);
        return true;
    }
    else if(act_num==2)//좌우
    {
        camera1(2,x,y);
        camera1(4,x,y);
        return true;
    }
    else
        return false;
    
}

bool camera3(int act_num,int x,int y)
{
    if(act_num==1)//상 우
    {
        camera1(1,x,y);
        camera1(2,x,y);
        return true;
    }
    else if(act_num==2) // 우 하
    {
        camera1(2,x,y);
        camera1(3,x,y);
        return true;
    }
    else if(act_num==3) // 하 좌
    {
        camera1(3,x,y);
        camera1(4,x,y);
        return true;
    }
    else if(act_num==4) // 좌 상
    {
        camera1(4,x,y);
        camera1(1,x,y);
        return true;
    }
    else
        return false;
}

bool camera4(int act_num,int x,int y)
{
    if(act_num==1)//좌상우
    {
        camera1(4,x,y);
        camera1(1,x,y);
        camera1(2,x,y);
        return true;
    }
    else if(act_num==2)//상 우 하
    {
        camera1(1,x,y);
        camera1(2,x,y);
        camera1(3,x,y);
        return true;
    }
    else if(act_num==3)// 우 하 좌
    {
        camera1(2,x,y);
        camera1(3,x,y);
        camera1(4,x,y);
        return true;
    }
    else if(act_num==4)// 하 좌 상
    {
        camera1(3,x,y);
        camera1(4,x,y);
        camera1(1,x,y);
        return true;
    }
    else
        return false;
}

bool camera5(int act_num,int x,int y)
{
    if(act_num==1)
    {
        camera1(1,x,y);
        camera1(2,x,y);
        camera1(3,x,y);
        camera1(4,x,y);
        return true;
    }
    else
        return false;
}

bool camera_act(int camera_num, int act_num,int x, int y)
{
    if (camera_num==1)
        return camera1(act_num,x,y);
    else if(camera_num==2)
        return camera2(act_num,x,y);
    else if(camera_num==3)
        return camera3(act_num,x,y);
    else if(camera_num==4)
        return camera4(act_num,x,y);
    else if(camera_num==5)
        return camera5(act_num,x,y);
    else
        return false;
}

void go(int index,int N, int max_index)
{
    if(index == max_index)
    {
        // A(순열) 충전 완료 원하는 동작 시작
        // [A[0]~A[index])

        // for (int i =0;i<index;i++)
        // {
        //     cout<<A[i]<<" ";
        // }
        // cout<<"\n"; 순열 확인
    
        for (int c=0;c<index;c++)
        {
            struct camera_info check_camera = camera_stack[c];
            bool OK = camera_act(check_camera.camera_num,A[c],check_camera.x,check_camera.y);
            if(OK==false)
            {
                map_recovery();
                return;
            }
        }

        int this_count = CCTV_CHECK();

        if(minmin>this_count)
            minmin=this_count;

        map_recovery();
        return;
    }

    for (int d=0;d<100;d++)
    {
        if(DB[d]>0)
        {
            DB[d]=DB[d]-1;
            A[index]=d;

            go(index+1,N,max_index);
            DB[d]=DB[d]+1;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin>>N;
    cin>>M;
    int number_of_camera=0; // 카메라 개수
    for(int y=0;y<N;y++)
    {
        for(int x=0;x<M;x++)
        {
            int c;
            cin>>c;
            my_map[y][x] = c; // my_map[행][열]
            if(my_map[y][x]==1 || my_map[y][x]==2||my_map[y][x]==3||my_map[y][x]==4||my_map[y][x]==5)
            {
                number_of_camera=number_of_camera+1;
                struct camera_info this_camera;
                this_camera.camera_num=my_map[y][x];
                this_camera.x=x;
                this_camera.y=y;
                camera_stack.push_back(this_camera);
            }
        }
    }// 맵 만들기 완성

    for(int y=0;y<N;y++)
    {
        for(int x=0;x<M;x++)
        {
            map_origin[y][x]=my_map[y][x];
        }
    }// 맵 복사

    int max_act_num=4;
    int max_index = number_of_camera;
    for(int i=1;i<=max_act_num;i++)
    {
        DB[i]=max_index;
    }
    for(int i=0;i<max_index;i++)
    {
        A.push_back(0);
    }
    go(0,max_act_num,max_index);
    

    cout<<minmin;
}
```

