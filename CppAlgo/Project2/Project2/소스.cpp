#include <stdio.h>
int data[100][100];
int holl[11][4];
int dp[100][100][4];
int visited[100][100][4];
int ans;

void init(int N) {
	for (int y = 0; y < N; ++y) {
		for (int x = 0; x < N; ++x) {
			for (int d = 0; x < 4; ++d) {
				dp[y][x][d] = 0;
				visited[y][x][d] = 0;
			}
		}
	}
}
int solve(int sy, int sx, int d) {
	int tempdp[100][100][4];
	int y, x = sy,sx;
	int res;

	while (1) {		
		res = 0;
		y += dy[d];
		x += dx[d];
		// 만약 인덱스를 넘어서 벽에 닿았다면
		if (1) {
			y -= dy[d];
			x -= dx[d];
			d += d % 2 ? -1 : 1;
			res = res*2 - 1;
			return res;
		}
		// 만약 벽이라면
		if (1 < data[y][x] < 6) {

		}		
		// 
		else if (6 <= data[y][x] <= 10) {

		}
		else {

		}
						   		 

	}
	





	
}
//우좌상하
int dy[] = { 0,0,1,-1 };
int dx[] = { 1,-1,0,0 };

int main() {
	int T, N;
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc) {
		scanf("%d", &N);
		for (int i = 0; i < 11; ++i) {
			for (int j = 0; j < 4; ++j) {
				holl[i][j] = -1;
			}
		}
		for (int y = 0; y < N; ++y) {
			for (int x = 0; x < N; ++x) {
				scanf("%d", &data[y][x]);
				if (5 < data[y][x] < 11) {
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
		for (int y = 0; y < N; ++y){
			for (int x = 0; x < N; ++x) {
				for (int d = 0; d < 4; ++d) {
					if (!dp[d][y][x]) {

					}
				}
			}
		}
		init(N);
	}

}