public class Test2 extends Test1{
    public Test2(String day, int num){
        super(num);
        System.out.println(day+"에 라면을 먹었다.");
    }
    @Override
    public void ramen(){
        System.out.println("더 맛있었다.");
    }
}
