import java.io.*;
  import java.util.*;

  public class Main{
      public static void main(String[] args)throws IOException{
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          StringBuilder sb = new StringBuilder();
          int M=Integer.parseInt(br.readLine());

          boolean[] answer = new boolean[21];

          for(int i=0;i<M;i++){
              String input_temp = br.readLine();
              String[] input=input_temp.split(" ");
              String ment=input[0];

              if(ment.equals("add")){
                  int n=Integer.parseInt(input[1]);
                  answer[n]=true;
              }else if(ment.equals("remove")){
                  int n=Integer.parseInt(input[1]);
                  answer[n]=false;
              }else if(ment.equals("check")){
                  int n=Integer.parseInt(input[1]);
                  sb.append(answer[n] ? 1 : 0).append('\n');
              }else if(ment.equals("toggle")){
                  int n=Integer.parseInt(input[1]);
                  answer[n] = !answer[n];
              }else if(ment.equals("all")){
                  Arrays.fill(answer, 1, 21, true);
              }else if(ment.equals("empty")){
                  Arrays.fill(answer, 1, 21, false);
              }
          }
          System.out.print(sb);
      }
  }