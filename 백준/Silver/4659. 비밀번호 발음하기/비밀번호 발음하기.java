import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
//a,e,i,o,u 하나 반드시 포함
//모음or 자음이 3개 연속 x
//같은 글자 2번 연속 x, but ee/oo는 가능
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            String pw = br.readLine();
            if(pw.equals("end")) break;
            
            boolean hasVowel = false;
            int consecV=0, consecC=0;
            char prev=0;
            boolean ok=true;
            
            for(int i=0;i<pw.length();i++){
                char ch=pw.charAt(i);
                boolean v = isVowel(ch);
                
                if(v){consecV++; consecC=0; hasVowel=true;}
                else {consecC++; consecV=0;}
                
                if(consecV>=3||consecC>=3){ok=false; break;}
                
                if(i>0&&ch==prev && ch!='e'&&ch!='o'){
                    ok=false;
                    break;
                } 
                prev=ch;
            }
            
            if(!hasVowel) ok=false;
            
            System.out.println("<"+pw+">"+(ok?" is acceptable." :" is not acceptable."));
        }
    } 
    
    public static boolean isVowel(char ch){
        return ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u';
    }
}