package com.example.smartclassroomvisionsystem.controllers;

import com.example.smartclassroomvisionsystem.model.StudentAtRiskData;
import com.example.smartclassroomvisionsystem.model.attendaceData;
import com.example.smartclassroomvisionsystem.services.LoginService;
import com.example.smartclassroomvisionsystem.services.StudentAtRiskService;
import com.example.smartclassroomvisionsystem.services.attendanceDataService;
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
public class AttendanceController {
    attendaceData ADS=new attendaceData();
    @PostMapping("/Attendance")
    public ResponseEntity<Map<String, String>> handleLogin(@RequestBody Map<String, String> data) {
        String Grade = data.get("grade");
        System.out.println(Grade);

        if (Grade != null) {
            ADS.AttendenceDetail(Grade);
            String names=ADS.getStudentNames().toString();
            String IDs=ADS.getStudentIDs().toString();
            String classes=ADS.getClasses().toString();
            String Attendance=ADS.getClassAttendance().toString();
            Map<String, String> response = Map.of("names",names,"IDs",IDs,"Classes",classes,"Attendance",Attendance );
            System.out.println(response);
            return ResponseEntity.ok(response); // Send the response with the additional data
        } else {
            // If login fails, return an unauthorized status
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Invalid credentials"));
        }
    }

}
