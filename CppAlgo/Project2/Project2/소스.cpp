#include <stdio.h>
int holl[11][4];
int data[100][100];
int dp[102][102][4];
int visited[100][100][4];
int ans,N;
int dy[4] = {0,0,-1,1};
int dx[4] = {1,-1,0,0};

void init(int N) {
	for (int y = 0; y < N+2; y++) {
		for (int x = 0; x < N+2; x++) {
			for (int d = 0; d < 4; d++) {
				dp[y][x][d] = -1;
				if (y<N and x<N) visited[y][x][d] = 0;
			}
		}
	}
}
int turn(int d, int nxd) {
	if (d == 0 && (nxd == 1 || nxd == 2 || nxd == 5))
		return ((d % 2) ? d - 1 : d + 1);
	if (d == 1 && (nxd == 3 || nxd == 4 || nxd == 5))
		return ((d % 2) ? d - 1 : d + 1);
	if (d == 2 && (nxd == 1 || nxd == 4 || nxd == 5)) 
		return ((d % 2) ? d - 1 : d + 1);
	if (d == 3 && (nxd == 2 || nxd == 3 || nxd == 5)) 
		return ((d % 2) ? d - 1 : d + 1);
	if ((d == 0 && nxd == 3) || (d == 1 && nxd == 2))
		return 3;
	if ((d == 0 && nxd == 4) || (d == 1 && nxd == 1))
		return 2;
	if ((d == 2 && nxd == 3) || (d == 3 && nxd == 4))
		return 1;
	if ((d == 2 && nxd == 2) || (d == 3 && nxd == 1))
		return 0;
}

int solve(int sy, int sx, int d) {
	//우좌상하
	int tempdp[102][102][4];
	
	for (int y = 0; y < N+2; y++) {
		for (int x = 0; x < N+2; x++) {
			for (int d = 0; d < 4; d++) {
				tempdp[y][x][d] = 0;
			}
		}
	}
	int y, x, ny, nx,flag;
	int res;
	y = sy;
	x = sx;
	tempdp[y+1][x+1][d] = 1;
	res = 0;
	flag = 1;
	while (1) {			
		y += dy[d];
		x += dx[d];
		tempdp[y+1][x+1][d] = 1;
		//dp 에 추가
		if (!data[y][x] and tempdp[y+1][x+1][d] and tempdp[y+1][x+1][(d % 2) ? d - 1 : d + 1] and !dp[y+1][x+1][(d % 2) ? d - 1 : d + 1]) {
			dp[y+1][x+1][(d % 2) ? d - 1 : d + 1] = res;
		}			
		// 만약 인덱스를 넘어서 벽에 닿았다면
		if (y == N || x == N || y == -1 || x == -1) {
			res += 1;
			d += (d % 2) ? -1 : 1;
			continue;
		}
		//블랙홀이나 시작점이면 리턴
		if ((y == sy && x == sx) || data[y][x] == -1 ){
			return res;
		}
		if (flag and !data[y][x] and dp[y + 1][x + 1][d] != -1) {
			res += dp[y + 1][x + 1][d];
			flag = 0;
			d += (d % 2) ? -1 : 1;
			continue;
		}
		// 만약 블록이라면
		if (data[y][x]>=1 && data[y][x]<6) {
			d = turn(d, data[y][x]);
			res += 1;
		}		
		//웜홀일 경우
		else if (data[y][x]>=6 && data[y][x]<=10) {
			if (y == holl[data[y][x]][0] && x == holl[data[y][x]][1]) {
				ny = holl[data[y][x]][2];
				nx = holl[data[y][x]][3];
				y = ny;
				x = nx;
			}
			else {
				ny = holl[data[y][x]][0];
				nx = holl[data[y][x]][1];
				y = ny;
				x = nx;
			}
		}						   		 
	}		   	  
}
int main() {
	int T,tp,result;
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		result = 0;
		scanf("%d", &N);
		init(N);
		for (int i = 0; i < 11; i++) {
			for (int j = 0; j < 4; j++) {
				holl[i][j] = -1;
			}
		}
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				scanf("%d", &data[y][x]);
				if (data[y][x]>=5 and data[y][x]< 11) {
					if (holl[data[y][x]][0] != -1) {
						holl[data[y][x]][2] = y;
						holl[data[y][x]][3] = x;
					}
					else {
						holl[data[y][x]][0] = y;
						holl[data[y][x]][1] = x;
					}
				}
			}
		}
 		for (int y = 0; y < N; y++){
			for (int x = 0; x < N; x++) {
				for (int d = 0; d < 4; d++) {
					/*if (!dp[d][y][x]) {

					}*/
					//if (y == 0 and x == 4 and d == 0) {
					//	printf("hi");
					//}
					if (!data[y][x] and dp[y+1][x+1][d]==-1) {
						tp = solve(y, x, d);
						if (tp > result) result = tp;
					}
				}
			}
		}
		printf("#%d %d\n",tc + 1, result);	
	}
	return 0;
}