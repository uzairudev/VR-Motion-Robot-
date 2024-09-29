#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Pose2D
from std_msgs.msg import String
from turtlesim.srv import TeleportAbsolute
import numpy as np
import csv

class turtleMove:

    def __init__(self):
        rospy.init_node('robotics_work', anonymous=True)
        rospy.wait_for_service('/turtle1/teleport_absolute')
        s = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        s(3.898438, 3.898438, 1.57)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pub2 = rospy.Publisher('/turtle1/cmd_pose2', Pose2D, queue_size=10)
        self.rate = rospy.Rate(90)
        self.twist = Twist()
        self.pose = Pose2D()

        bf = "backandforth.csv"
        rf = "rotate.csv"
        ram = "randomWalk.csv"
        csvPath = "/home/ioh/catkin_ws/src/robotics/scripts/Csv_data/" + bf
        data = self.loadCsv(csvPath)

        sec = [int(row[1]) for row in data[1:]]
        nsec = [int(row[2]) for row in data[1:]]
        positionX = [float(row[4]) for row in data[1:]]
        positionY = [float(row[6]) for row in data[1:]]
        normX = self.norm(positionX)
        normY = self.norm(positionY)
        rotation = [np.deg2rad(360-float(row[8])) for row in data[1:]]
        normRad = self.normR(rotation)
        time = self.calTime(sec, nsec)
        timeD = self.calD(time)
        # xD = self.calD(positionX)
        # yD = self.calD(positionY)
        xD = self.calD(normX)
        yD = self.calD(normY)
        # euclid = [np.sqrt((x**2) + (y**2)) for (x, y) in zip(xD, yD)]
        # rD = self.calD(normRad)
        rD = self.calDRad(normRad)
        speedY = self.calSpeed(timeD, yD)
        speedX = self.calSpeed(timeD, xD)
        # speedE = self.calSpeed(timeD, euclid)
        speedR = self.calSpeed(timeD, rD)
        # print(speedR)

        minusX = [-row for row in speedX]
        xDash, yDash = self.rot(speedY, minusX, rD)

        for i in range(len(speedR)):
            # self.odom2(0, 0, speedR[i], timeD[i])
            # self.odom2(xDash[i], -yDash[i], 0, timeD[i])
            # self.odom2(xDash[i], -yDash[i], speedR[i], timeD[i])
            self.odom2(speedX[i], speedY[i], speedR[i], timeD[i])
            # self.odom2(speedY[i], -speedX[i], 0, timeD[i])
            # s(normX[i], normY[i], normRad[i])
            # self.odom3(normX[i], normY[i], normRad[i])
            # self.rate.sleep()

    def loadCsv(self, path):
        with open(path) as f:
            reader = csv.reader(f)
            l = [row for row in reader]
        return l

    def calTime(self, sec, nsec):
        startTime = sec[0]
        startTimeN = nsec[0]
        sec = [row-startTime for row in sec]
        nsec = [(row-startTimeN)/(10**9) for row in nsec]
        time = [x + y for (x, y) in zip(sec, nsec)]
        return time

    def calD(self, d):
        D = [y - x for (x, y) in zip(d[0:-2], d[1:])]
        return D

    def calDRad(self, data):
        DR = []
        for i in range(len(data)-1):
            z = data[i+1]-data[i]
            # print(z)
            if abs(z) > 0.5*np.pi:
                DR.append(2*np.pi - z)
            else:
                DR.append(z)
        return DR

    def calSpeed(self, time, D):
        S = []
        # S = [y / x for (x, y) in zip(time, D)]
        for i in range(len(time)):
            z = D[i]/time[i]
            # if abs(z) > 1.0:
                # print(np.rad2deg(D[i]))
            S.append(z)
        return S

    def odom2(self, x, y, z, t):
        self.twist.linear.x = x
        self.twist.linear.y = y
        self.twist.angular.z = z
        self.pub.publish(self.twist)
        rospy.sleep(t)

    def odom3(self, x, y, z):
        self.pose.x = x
        self.pose.y = y
        self.pose.theta = z
        self.pub2.publish(self.pose)
        # rospy.sleep(t)

    def norm(self, data):
        normD = [(row-data[0])*2.5+3.898438 for row in data]
        return normD

    def normR(self, data):
        normRad = []
        for row in data:
            if (row-data[0]) > 1.5*np.pi:
                normRad.append((row-data[0])+np.pi/2-2*np.pi)
            else:
                normRad.append((row-data[0])+np.pi/2)
        return normRad

    def rot(self, x, y, theata):
        xDash = [i*np.cos(k)+j*np.sin(k) for (i, j, k) in zip(x, y, theata)]
        yDash = [i*np.sin(k)-j*np.cos(k) for (i, j, k) in zip(x, y, theata)]
        return xDash, yDash

if __name__ == '__main__':

    run = turtleMove()
