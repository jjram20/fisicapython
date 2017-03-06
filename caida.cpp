#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
  ofstream archivo;
  archivo.open("caida.dat");
  //Valores iniciales
  float x=0;
  float y=40;
  float vx=1;
  float vy=0;
  float g=-9.8;
  float dt=0.1;
  for(float t=0;t<=10;t+=dt)
  {
    if (x>=0 && y>=0)
    {
      x=vx*dt+x;
      vy=g*dt+vy;
      y=y+vy*dt+g*pow(dt,2)/2;
      archivo << t << " " << x << " " << y << endl;
    }
    else
      break;
  }
  archivo.close();
  return 0;
}
