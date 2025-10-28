import java.util.*;
import java.io.*;
//1 : 켜, 0 : 꺼
//자연수 : 1이상, 스위치 개수 이하
//남(1)+받은수가 스위치번호의 배수 -> 스위치 상태 바굼
//여(2)+자기가 받은 수의 스위치를 중심으로 좌우가 대칭 + 가장 많은 스위치를 포함하는 구간을 찾아 구간에 속한 스위치 상태를 바꿈
// -> 이 구간에 속한 스위치 개수는 홀수
class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n =Integer.parseInt(br.readLine()); //스위치 개수
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] switchh = new int[n+1];//스위치 상태
        switchh[0]=-100;

        for(int i=1;i<n+1;i++){
            switchh[i] = Integer.parseInt(st.nextToken());
        }

        int studentCount=Integer.parseInt(br.readLine()); //학생수
        for(int i=0;i<studentCount;i++){
            st = new StringTokenizer(br.readLine());
            int gender=Integer.parseInt(st.nextToken());//성별
            int number=Integer.parseInt(st.nextToken());//받은 숫자

            if(gender==1){
                //남자
                for(int j=1;j<n+1;j++){
                    if(j%number==0) {
                        switchh[j] = switchh[j]^1;
                    }
                }
            }else if(gender==2){
                //여자
                switchh[number]=switchh[number]^1;
                int left=number-1;
                int right=number+1;
                while(left>=1&&right<=n) {
                    if(switchh[left]==switchh[right]){
                        switchh[left]=switchh[left]^1;
                        switchh[right]=switchh[right]^1;
                        left-=1;
                        right+=1;
                    }else break;
                }

            }
        }
//0 1 1 1 0 1 0 1
        for(int i=1;i<n+1;i++){
            //스위치들의 마지막 생태 출력
            System.out.print(switchh[i]+" ");
            if(i%20==0) System.out.println();
        }

    }

}