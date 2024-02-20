#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
import os
from std_msgs.msg import Int16
from std_msgs.msg import String

frame = Tk()
frame.title("GUI")
frame.geometry("400x300")

rospy.init_node("Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

pub_arduino = rospy.Publisher("BTN_LED", Int16, queue_size=10)
sub_arduino = rospy.Subscriber("BTN_LED", Int16, callback = ())

pub_motion = rospy.Publisher("Motion", String, queue_size=10)

def Talker(val):
	cmd_val = Int16(val)
	rospy.loginfo(cmd_val)
	pub_arduino.publish(cmd_val)

def fw():
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	text = 'Forward'
	pub_motion.publish(text)
	
def bw():
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	text = 'Backward'
	pub_motion.publish(text)
	
def OnPen():
	os.system('rosservice call turtle1/set_pen 255 255 255 3 0')
	Talker(1)
	
def OffPen():
	os.system('rosservice call turtle1/set_pen 255 255 255 3 1')
	Talker(0)
	
def rr():
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= -1.0
	pub.publish(cmd)
	text = 'Turn Right'
	pub_motion.publish(text)
	pub_arduino.publish(0)
	
def rl():
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= 1.0
	pub.publish(cmd)
	text = 'Turn Left'
	pub_motion.publish(text)

B1 = Button(text = "Forward", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "Backward", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "Turn Right", command=rr)
B3.place(x=128, y=80)

B4 = Button(text = "Turn Left", command=rl)
B4.place(x=20, y=80)

B5 = Button(text = "PenOn", command=OnPen)
B5.place(x=20, y=200)

B6 = Button(text = "PenOff", command=OffPen)
B6.place(x=128, y=200)

frame.mainloop()
