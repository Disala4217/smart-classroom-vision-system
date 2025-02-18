package com.example.smartclassroomvisionsystem.services;

import com.example.smartclassroomvisionsystem.DataBaseConnection;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class attendanceDataService {
    public List<String> GetStudentNames(String Grade) {
        List<String> studentNames = new ArrayList<>();

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT name FROM student WHERE grade = ? ORDER BY id ASC";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                studentNames.add(resultSet.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return studentNames;
    }
    public List<String> GetStudentID(String Grade) {
        List<String> studentNames = new ArrayList<>();

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT ID FROM student WHERE grade = ? ORDER BY id ASC";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                studentNames.add(resultSet.getString("ID"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return studentNames;
    }
    public List<String> GetClassesForGrade(String Grade) {
        List<String> classes = new ArrayList<>();

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT CONCAT(Class_id, ' - ', subject, ' - ', teacher_id) AS class_info " +
                    "FROM class WHERE grade = ? ORDER BY datetime ASC";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                classes.add(resultSet.getString("class_info"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return classes;
    }

    public List<String> GetStudentsAttendedForClasses(String Grade) {
        List<String> classAttendance = new ArrayList<>();

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT \n" +
                    "c.Class_id AS class_id, \n" +
                    "GROUP_CONCAT(s.id ORDER BY s.id ASC) AS students_attended \n" +
                    "FROM attendance a JOIN student s ON a.student_id = s.id JOIN class c ON a.class_id = c.Class_id WHERE a.attendance = ? GROUP BY c.Class_id ORDER BY c.datetime ASC";

            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                String classId = resultSet.getString("class_id");
                String studentsAttended = resultSet.getString("students_attended");

                String classDetails = classId + " : " + studentsAttended;
                classAttendance.add(classDetails);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return classAttendance;
    }
    public List<String> GetStudentsEngagementForClasses(String Grade) {
        List<String> classAttendance = new ArrayList<>();

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT " +
                    "a.student_id, " +
                    "a.class_id, " +
                    "a.engagement_level " +
                    "FROM attendance a " +
                    "INNER JOIN class c ON a.class_id = c.Class_id " +
                    "WHERE c.grade = ?";

            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                String studentId = resultSet.getString("student_id");
                String classId = resultSet.getString("class_id");
                String engagementLevel = resultSet.getString("engagement_level");

                String classDetails = classId + "-" + studentId + "-" + engagementLevel;
                classAttendance.add(classDetails);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return classAttendance;
    }

    public String totalattendence(String Grade) {

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT \n" +
                    "    c.grade, \n" +
                    "    SUM(a.attendance) AS total_attendance\n" +
                    "FROM \n" +
                    "    class c\n" +
                    "JOIN \n" +
                    "    attendance a ON c.Class_id = a.class_id\n" +
                    "WHERE \n" +
                    "    c.grade = ?  \n" +
                    "GROUP BY \n" +
                    "    c.grade;\n";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);


            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                return resultSet.getString("total_attendance");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
    public String totalEngagment(String Grade) {
        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT SUM(a.engagement_level) AS total_engagement\n" +
                    "FROM attendance a\n" +
                    "JOIN class c ON a.class_id = c.Class_id\n" +
                    "WHERE c.grade = ?;";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getString("total_engagement");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
    public String totalStudent(String Grade) {

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT grade, COUNT(*) AS student_count\n" +
                    "FROM student\n" +
                    "WHERE grade = ?\n" +
                    "GROUP BY grade;";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getString("student_count");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
    public String totalclasses(String Grade) {

        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT grade, COUNT(*) AS class_count\n" +
                    "FROM class\n" +
                    "WHERE grade = ? \n" +
                    "GROUP BY grade;\n";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, Grade);
            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                return resultSet.getString("class_count");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
}
