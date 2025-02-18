package com.example.smartclassroomvisionsystem.services;
import com.example.smartclassroomvisionsystem.DataBaseConnection;
import com.example.smartclassroomvisionsystem.model.StudentAtRiskData;
import com.example.smartclassroomvisionsystem.model.StudentAtRiskDataAttendence;
import com.example.smartclassroomvisionsystem.model.StudentAtRiskDataEngagement;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
public class StudentAtRiskService {
    public static List<StudentAtRiskData> getStudentsAtRisk(String grade) {
        List<StudentAtRiskData> studentsAtRisk = new ArrayList<>();
        String query = "SELECT s.id, s.name, " +
                "COALESCE((SUM(a.attendance) / NULLIF(COUNT(a.class_id), 0)) * 100, 0) AS avgAttendance, " +
                "COALESCE((SUM(a.engagement_level) / NULLIF(COUNT(a.class_id), 0)), 0) AS avgEngagement " +
                "FROM student s " +
                "LEFT JOIN attendance a ON s.id = a.student_id " +
                "LEFT JOIN class c ON a.class_id = c.Class_id " +
                "WHERE s.grade = ? " +
                "GROUP BY s.id, s.name " +
                "ORDER BY avgAttendance ASC, avgEngagement ASC " +
                "LIMIT 10;";
        try (Connection connection = DataBaseConnection.connect();
             PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setString(1, grade);
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                studentsAtRisk.add(new StudentAtRiskData(
                        rs.getString("id"),
                        rs.getString("name"),
                        rs.getDouble("avgAttendance"),
                        rs.getDouble("avgEngagement")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        System.out.println(studentsAtRisk);
        return studentsAtRisk;
    }
    public static List<StudentAtRiskDataEngagement> getStudentsAtRiskEngagement(String grade) {
        List<StudentAtRiskDataEngagement> studentsAtRisk = new ArrayList<>();
        String query = "SELECT s.id, s.name, " +
                "COALESCE((SUM(a.engagement_level) / NULLIF(COUNT(a.class_id), 0)), 0) AS avgEngagement " +
                "FROM student s " +
                "LEFT JOIN attendance a ON s.id = a.student_id " +
                "LEFT JOIN class c ON a.class_id = c.Class_id " +
                "WHERE s.grade = ? " +
                "GROUP BY s.id, s.name " +
                "ORDER BY avgEngagement ASC " +
                "LIMIT 10;";
        try (Connection connection = DataBaseConnection.connect();
             PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setString(1, grade);
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                studentsAtRisk.add(new StudentAtRiskDataEngagement(
                        rs.getString("id"),
                        rs.getString("name"),
                        rs.getDouble("avgEngagement")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        System.out.println(studentsAtRisk);
        return studentsAtRisk;
    }
    public static List<StudentAtRiskDataAttendence> getStudentsAtRiskAttendance(String grade) {
        List<StudentAtRiskDataAttendence> studentsAtRisk = new ArrayList<>();
        String query = "SELECT s.id, s.name, " +
                "COALESCE((SUM(a.attendance) / NULLIF(COUNT(a.class_id), 0)) * 100, 0) AS avgAttendance " +
                "FROM student s " +
                "LEFT JOIN attendance a ON s.id = a.student_id " +
                "LEFT JOIN class c ON a.class_id = c.Class_id " +
                "WHERE s.grade = ? " +
                "GROUP BY s.id, s.name " +
                "ORDER BY avgAttendance ASC " +
                "LIMIT 10;";
        try (Connection connection = DataBaseConnection.connect();
             PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setString(1, grade);
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                studentsAtRisk.add(new StudentAtRiskDataAttendence(
                        rs.getString("id"),
                        rs.getString("name"),
                        rs.getDouble("avgAttendance")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        System.out.println(studentsAtRisk);
        return studentsAtRisk;
    }
}
