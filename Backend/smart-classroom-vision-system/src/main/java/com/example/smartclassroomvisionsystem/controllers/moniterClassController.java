package com.example.smartclassroomvisionsystem.controllers;

import com.example.smartclassroomvisionsystem.model.MoniterClass;
import com.example.smartclassroomvisionsystem.services.MoniterClassService;
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
public class moniterClassController {

    MoniterClassService moniter = new MoniterClassService();

    @PostMapping("/MoniterClass")
    public ResponseEntity<Map<String, Object>> handleLogin(@RequestBody Map<String, String> data) {
        String teacherId = data.get("ID");

        if (teacherId != null) {
            List<MoniterClass> classDetails = moniter.getClassDetails(teacherId);

            if (classDetails.isEmpty()) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body(Map.of("error", "No classes found for the teacher"));
            }

            return ResponseEntity.ok(Map.of("classDetails", classDetails));
        } else {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Invalid teacher ID"));
        }
    }
}
