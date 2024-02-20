#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;
std_msgs::Int16 Button;
std_msgs::Int16 LED_control;

const int BTN1 = 2;
const int BTN2 = 3; 
const int BTN3 = 4;
const int ledPin = 13;


ros::Publisher BTN_pub("BTN_LED", &Button );

ros::Subscriber<std_msgs::Int16> LED_sub("BTN_LED", &LED_control );


void setup() 
{
  pinMode(ledPin, OUTPUT);
  pinMode(BTN1, INPUT);
  pinMode(BTN2, INPUT);
  pinMode(BTN3, INPUT);
  nh.initNode();
  nh.advertise(BTN_pub);
  nh.subscribe(LED_sub);
}

void LED_control(const std_msgs::Int16& cmd_msg)
{
  int value = cmd_msg.data;
  ledPin.digitalWrite(value)
}

void BTN_control()
{
  if BTN3 =1{
    if BTN1 = 1 && BTN2 =1{
      num = 1;
    }
    else BTN1 = 0 && BTN2 =1{
      num = 2;
    }
    else BTN1 = 1 && BTN2 =0{
      num = 3;
    }
  }
  else BTN3 =0{
    if BTN1 = 1 && BTN2 =1{
      num = 4;
    }
    else BTN1 = 0 && BTN2 =1{
      num = 2;
    }
    else BTN1 = 1 && BTN2 =0{
      num = 3;
    }
  }
  Button.data = num;
  pub.publish();
  nh.spinOnce();
  delay(500);
}
