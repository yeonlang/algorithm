#include <stdio.h>
int data[100][100];
int holl[11][4] = { -1, };
int dp[100][100][4] = { 0, };
int visited[100][100][4] = { 0, };
int ans;

void solve(int y, int x, int d) {
	

}

int main() {
	int T,N;
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc) {
		scanf("%d", &N);
		for (int y = 0; y < N; ++y)
			for (int x = 0; x < N; ++x) {
				scanf("%d", &data[y][x]);
				if (5 < data[y][x] <= 10) {
					if (holl[data[y][x]][0] != -1){
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
	for (int y = 6; y < 11; ++y) {
		for (int x = 0; x < 4; ++x) {
			printf("%d ", holl[y][x]);
		}
		printf("\n");
	}

	/*for (int y = 0; y < N; ++y){
		for (int x = 0; x < N; ++x) {
			for (int d = 0; d < 4; ++d) {
				if (!dp[d][y][x]) {

				}
			}			
		}
	}		
	*/
}






