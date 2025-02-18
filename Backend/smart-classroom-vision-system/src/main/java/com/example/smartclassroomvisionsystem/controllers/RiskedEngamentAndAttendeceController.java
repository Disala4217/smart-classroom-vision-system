package com.example.smartclassroomvisionsystem.controllers;
import com.example.smartclassroomvisionsystem.model.StudentAtRiskDataAttendence;
import com.example.smartclassroomvisionsystem.model.StudentAtRiskDataEngagement;
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
public class RiskedEngamentAndAttendeceController {
    @PostMapping("/RiskEandA")
    public ResponseEntity<Map<String, String>> handleLogin(@RequestBody Map<String, String> data) {
        String ID = data.get("ID");
        String Grade = data.get("grade");
        String Engagment=getStudentsAtRiskEngagment(Grade);
        String Attendence=getStudentsAtRiskAttendence(Grade);
        System.out.println(ID);
        System.out.println(Grade);
        if (ID != null) {
            Map<String, String> response = Map.of("engagment",Engagment,"Attendence",Attendence);
            System.out.println(response);
            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Invalid credentials"));
        }
    }
    public String getStudentsAtRiskEngagment(String grade) {
        List<StudentAtRiskDataEngagement> studentsAtRisk = StudentAtRiskService.getStudentsAtRiskEngagement(grade);
        if (studentsAtRisk.isEmpty()) {
            return "No students found at risk for grade " + grade;
        }
        StringBuilder result = new StringBuilder("Students at Risk for Grade " + grade + ":\n");
        for (StudentAtRiskDataEngagement student : studentsAtRisk) {
            result.append(student.toString()).append("\n");
        }
        return result.toString();
    }
    public String getStudentsAtRiskAttendence(String grade) {
        List<StudentAtRiskDataAttendence> studentsAtRisk = StudentAtRiskService.getStudentsAtRiskAttendance(grade);
        if (studentsAtRisk.isEmpty()) {
            return "No students found at risk for grade " + grade;
        }
        StringBuilder result = new StringBuilder("Students at Risk for Grade " + grade + ":\n");
        for (StudentAtRiskDataAttendence student : studentsAtRisk) {
            result.append(student.toString()).append("\n");
        }
        return result.toString();
    }
}