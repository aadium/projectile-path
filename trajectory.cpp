#include <iostream>
#include <cmath>
#include "trajectory.h"

void pequation(float angleinit, float vinit, float g)
{
    float angle_rad = angleinit * M_PI/180;
    std::cout << "Path Equation: " << tan(angle_rad) << "x - " << (g / 2 * pow((vinit * cos(angle_rad)), 2)) << "x^2" << std::endl;
}

float tflight(float angleinit, float vinit, float g)
{
    float angle_rad = angleinit * M_PI/180;
    float tflight;
    tflight = 2 * ((vinit * sin(angle_rad))/g);
    return tflight;
}

float hmax(float angleinit, float vinit, float g)
{
    float angle_rad = angleinit * M_PI/180;
    float hmax;
    hmax = (pow((vinit * sin(angle_rad)), 2)/(2 * g));
    return hmax;
}

float hrange(float angleinit, float vinit, float g)
{
    float angle_rad = angleinit * M_PI/180;
    float hrange;
    hrange = pow(vinit, 2) * sin(2 * angle_rad) / g;
    return hrange;
}

float rangemax(float vinit, float g)
{
    float rangemax;
    rangemax = pow(vinit, 2) / g;
    return rangemax;
}
