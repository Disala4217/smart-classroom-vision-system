package com.example.smartclassroomvisionsystem.controllers;
import com.example.smartclassroomvisionsystem.model.attendaceData;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;
@RestController
@RequestMapping("/api")
public class EngagmentController {
    attendaceData ADS=new attendaceData();
    @PostMapping("/Engagement")
    public ResponseEntity<Map<String, String>> handleLogin(@RequestBody Map<String, String> data) {
        String Grade = data.get("grade");
        System.out.println(Grade);
        if (Grade != null) {
            ADS.EngagmentDetail(Grade);
            String names=ADS.getStudentNames().toString();
            String IDs=ADS.getStudentIDs().toString();
            String classes=ADS.getClasses().toString();
            String Engagement=ADS.getEngagement().toString();
            Map<String, String> response = Map.of("names",names,"IDs",IDs,"Classes",classes,"Engagement",Engagement );
            System.out.println(response);
            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Invalid credentials"));
        }
    }
}
