#include<stdio.h>
#include<math.h>
main()
{
    double x1,x2,a,b,c,z;
    scanf("%lf%lf%lf",&a,&b,&c);
    z=b*b-4*a*c;
    if(z>=0)
       {
        x1=(-b+sqrt(z))/(2*a);
        x2=(-b-sqrt(z))/(2*a);
        printf("%lf %lf",x1,x2);
       }
    else
        printf("fff");
}
