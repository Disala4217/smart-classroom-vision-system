package com.example.smartclassroomvisionsystem.model;
public class StudentAtRiskDataAttendence {
    private String studentId;
    private String name;
    private double attendance;
    public StudentAtRiskDataAttendence(String studentId, String name, double attendance) {
        this.studentId = studentId;
        this.name = name;
        this.attendance = attendance;
    }
    public String toString() {
        return "ID: " + studentId + ", Name: " + name + ", Attendance: " + attendance + "%";
    }
}
