

import java.io.*;
import java.util.*;

// 코드 실행은 되지만 런타임 에러났다. 처리속도가 느리다는 뜻.
public class Main {
    public static void main(String[] arg) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 원본 행렬 저장
        int A[][] = new int[N+1][N+1];
        for(int i=1 ; i <= N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1 ; j <= N;j++){
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //합 행렬 저장
        int S[][] = new int[N+1][N+1];
        for (int i=1; i<= N; i++){
            for(int j=1 ; j <= N;j++){
                S[i][j] = S[i][j-1] + S[i-1][j] - S[i-1][j-1] + A[i][j];
            }
        }

        // 질의 결과 발표
        int result[] = new int[M];
        for (int q=0; q < M; q++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            result[q] = S[x2][y2]-S[x1-1][y2]-S[x2][y1-1] + S[x1-1][y1-1];
        }
        for(int i=0; i < M; i++){
            System.out.println(result[i]);
        }
    } 
}
