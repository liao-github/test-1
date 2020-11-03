class Triangle{
    int a,b,c;
    int zhouchang()
    {
        return a+b+c;
    }
    double mianji()
    {
        double p = 1.0*(a+b+c)/2;
        return  Math.sqrt(p*(p-a)*(p-b)*(p-c));
    }

}

class TestTriangle
{
    public static void main(String[] args)
    {
    Triangle T = new Triangle();
    T.a = 3;
    T.b = 4;
    T.c = 5;
    System.out.printf("%d %f",T.zhouchang(),T.mianji());
    }
}
