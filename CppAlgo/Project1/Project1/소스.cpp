#include <stdio.h>
const int maxR = 100;
const int maxC = 100;
int N, M, K, ans;

typedef struct FISH{
	int big,y,x,s,d;
};
FISH data[maxR][maxC] = { 0, };

// 상하우좌
int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,1,-1 };

void trans(int y, int x) {
	int time;
	time = 0;
	while (time < data[y][x].s) {	
		if (data[y][x].d < 2) {
			data[y][x].y += dy[data[y][x].d];			
			if (data[y][x].y==N or data[y][x].y==-1) {
				data[y][x].y -= dy[data[y][x].d];
				data[y][x].d += data[y][x].d % 2 ? -1 : 1;
				data[y][x].y += dy[data[y][x].d];
			}
		}
		else {
			data[y][x].x += dx[data[y][x].d];
			if (data[y][x].x == M or data[y][x].x == -1) {
				data[y][x].x -= dx[data[y][x].d];
				data[y][x].d += data[y][x].d % 2 ? -1 : 1;
				data[y][x].x += dx[data[y][x].d];
			}
		}
		time++;
	}	
}
void moving() {
	FISH tempdata[maxR][maxC] = { 0, };
	for (int y = 0; y < N; ++y)
		for (int x = 0; x < M; ++x) {
			if (!data[y][x].big == 0) {
				trans(y, x);
				//물고기가 있으면서
				if (tempdata[data[y][x].y][data[y][x].x].big) {
					//물고기의 크기가 더 큰놈이면 큰놈으로 갱신
					if (tempdata[data[y][x].y][data[y][x].x].big < data[y][x].big) {
						tempdata[data[y][x].y][data[y][x].x] = data[y][x];
					}
				}
				//물고기가 없으면
				else {
					tempdata[data[y][x].y][data[y][x].x] = data[y][x];
				}
			}
		}
	for (int y = 0; y < N; ++y){
		for (int x = 0; x < M; ++x) {
			data[y][x] = tempdata[y][x];
		}
	}
}
int kill(int x) {
	for (int y = 0; y < N; ++y) {
		if (data[y][x].big) {
			ans += data[y][x].big;
			data[y][x].big = 0;
			return 0;
		}
	}
	return 0;
}

//int main() {	
//	scanf("%d %d %d", &n, &m, &k);	
//	int r, c, s, d, z;
//	for (int i = 0; i < k; ++i) {
//		scanf("%d %d %d %d %d", &r, &c, &s, &d, &z);
//		r--; c--; d--;
//		data[r][c] = { z,r,c,s,d };		   	
//	}
//	int now_x;
//	ans, now_x = 0, 0;
//	while (now_x != m) {
//		kill(now_x);
//		moving();
//		now_x++;
//	}			
//	printf("%d", ans);
//}
