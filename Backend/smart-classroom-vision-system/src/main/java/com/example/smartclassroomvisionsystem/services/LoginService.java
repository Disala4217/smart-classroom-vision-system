package com.example.smartclassroomvisionsystem.services;
import com.example.smartclassroomvisionsystem.DataBaseConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
public class LoginService {
    public String LoginUser(String ID, String password) {
        try (Connection connection = DataBaseConnection.connect()) {
            String query = "SELECT name FROM teacher WHERE id = ? AND password = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, ID);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getString("name");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
    public String GetRole(String ID) {
        String role = null;
        try (Connection connection = DataBaseConnection.connect();
             PreparedStatement statement = connection.prepareStatement("SELECT role FROM teacher WHERE id = ?")) {
            statement.setString(1, ID);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    role = resultSet.getString("role");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return role;
    }
    public String GetGrade(String ID) {
        String Grade = null;
        try (Connection connection = DataBaseConnection.connect();
             PreparedStatement statement = connection.prepareStatement("SELECT Grade FROM teacher WHERE id = ?")) {
            statement.setString(1, ID);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    Grade = resultSet.getString("Grade");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return Grade;
    }
}
