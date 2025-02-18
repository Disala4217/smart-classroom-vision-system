package com.example.smartclassroomvisionsystem.model;

public class StudentAtRiskData {
    private String studentId;
    private String name;
    private double attendance;
    private double engagement;

    public StudentAtRiskData(String studentId, String name, double attendance, double engagement) {
        this.studentId = studentId;
        this.name = name;
        this.attendance = attendance;
        this.engagement = engagement;
    }

    public String toString() {
        return "ID: " + studentId + ", Name: " + name + ", Attendance: " + attendance + "%, Engagement: " + engagement + "%";
    }


}
