package com.example.smartclassroomvisionsystem.controllers;
import com.example.smartclassroomvisionsystem.model.StudentAtRiskData;
import com.example.smartclassroomvisionsystem.model.attendaceData;
import com.example.smartclassroomvisionsystem.services.StudentAtRiskService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;
import java.util.Map;
@RestController
@RequestMapping("/api")
public class DashboardController {
    attendaceData ADS=new attendaceData();
    @PostMapping("/DashBoard")
    public ResponseEntity<Map<String, String>> handleLogin(@RequestBody Map<String, String> data) {
        String ID = data.get("ID");
        String Grade = data.get("grade");
        System.out.println(ID);
        System.out.println(Grade);
        ADS.setGrade(Grade);
        ADS.modelVariableFiller();
        String AverageAttended = String.valueOf(ADS.attendaceSummeryData());
        String AverageNotAttended = String.valueOf(100 - ADS.attendaceSummeryData());
        String AverageEngagement=String.valueOf(ADS.Engagment());
        String AverageNotEngagement=String.valueOf(100 - ADS.Engagment());
        String riskedStudents=getStudentsAtRisk(Grade);
        if (ID != null) {
            Map<String, String> response = Map.of("Attended", AverageAttended, "NotAttended", AverageNotAttended, "Engaged",AverageEngagement,"NotEngaged",AverageNotEngagement,"Risked",riskedStudents );
           System.out.println(response);
            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Invalid credentials"));
        }
    }
    public String getStudentsAtRisk(String grade) {
        List<StudentAtRiskData> studentsAtRisk = StudentAtRiskService.getStudentsAtRisk(grade);
        if (studentsAtRisk.isEmpty()) {
            return "No students found at risk for grade " + grade;
        }
        StringBuilder result = new StringBuilder("Students at Risk for Grade " + grade + ":\n");
        for (StudentAtRiskData student : studentsAtRisk) {
            result.append(student.toString()).append("\n");
        }
        return result.toString();
    }
}
