package com.example.smartclassroomvisionsystem.services;
import com.example.smartclassroomvisionsystem.DataBaseConnection;
import com.example.smartclassroomvisionsystem.model.MoniterClass;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
public class MoniterClassService {
    public static List<MoniterClass> getClassDetails(String teacherId) {
        List<MoniterClass> monitorClasses = new ArrayList<>();
        String query = "SELECT c.`Class_id`, c.`subject`, c.`datetime`, c.`Status`, \n" +
                "       a.`student_id`, s.`name` AS `student_name`, a.`attendance`, a.`attended_time`, a.`engagement_level`\n" +
                "FROM `class` c\n" +
                "JOIN `attendance` a ON c.`Class_id` = a.`class_id`\n" +
                "JOIN `student` s ON a.`student_id` = s.`id`\n" +
                "WHERE c.`Status` = 'started' \n" +
                "AND c.`teacher_id` = ?\n" +
                "ORDER BY c.`datetime` DESC\n" +
                "LIMIT 1;";

        try (Connection connection = DataBaseConnection.connect();
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setString(1, teacherId);
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                monitorClasses.add(new MoniterClass(
                        rs.getInt("Class_id"),
                        rs.getString("subject"),
                        rs.getTimestamp("datetime"),
                        rs.getString("Status"),
                        rs.getInt("student_id"),
                        rs.getString("student_name"),
                        rs.getDouble("attendance"),
                        rs.getInt("attended_time"),
                        rs.getDouble("engagement_level")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace(); }
        System.out.println(monitorClasses);
        return monitorClasses;
    }
}
