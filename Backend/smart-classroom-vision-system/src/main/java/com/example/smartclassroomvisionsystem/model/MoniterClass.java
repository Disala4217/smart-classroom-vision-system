package com.example.smartclassroomvisionsystem.model;
import java.sql.Timestamp;
public class MoniterClass {
    private int classId;
    private String subject;
    private Timestamp datetime;
    private String status;
    private int studentId;
    private String studentName;
    private double attendance;
    private int attendedTime;
    private double engagementLevel;
    public MoniterClass(int classId, String subject, Timestamp datetime, String status,
                        int studentId, String studentName, double attendance,
                        int attendedTime, double engagementLevel) {
        this.classId = classId;
        this.subject = subject;
        this.datetime = datetime;
        this.status = status;
        this.studentId = studentId;
        this.studentName = studentName;
        this.attendance = attendance;
        this.attendedTime = attendedTime;
        this.engagementLevel = engagementLevel;
    }

    @Override
    public String toString() {
        return "Class ID: " + classId + ", Subject: " + subject + ", Date & Time: " + datetime + ", Status: " + status +
                ", Student ID: " + studentId + ", Student Name: " + studentName +
                ", Attendance: " + attendance + "%, Engagement Level: " + engagementLevel + "%";
    }
}

