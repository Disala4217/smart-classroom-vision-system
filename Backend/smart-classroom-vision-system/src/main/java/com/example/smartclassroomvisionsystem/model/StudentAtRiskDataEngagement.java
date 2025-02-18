package com.example.smartclassroomvisionsystem.model;

public class StudentAtRiskDataEngagement {
    private String studentId;
    private String name;
    private double engagement;

    public StudentAtRiskDataEngagement(String studentId, String name, double engagement) {
        this.studentId = studentId;
        this.name = name;
        this.engagement = engagement;
    }

    public String toString() {
        return "ID: " + studentId + ", Name: " + name + ", Engagement: " + engagement + "%";
    }
}
